from flask import request

from config import dynamo_config, api_config
from utils.send_to_calc_service import send_data_to_parse
from utils.dynamodb_resource import DynamoResource


def api_service_post(body: dict):
    # todo validate data
    # return 'not ok', 400 in case of eg. wrong data format
    dynamo_resource = DynamoResource(dynamo_config)
    try:
        with dynamo_resource as dynamo_table:
            dynamo_table.batch_save_to_table(body)
        return 'Accepted', 201
    except Exception as ex:
        return ex
        # I know Exception is to broad, it would rather catch some connection errors
        # todo handle ex


def api_service_get_data(data_point_name: str):
    # todo try except block to catch errors like connection-error, no-data-found, KeyError
    dynamo_resource = DynamoResource(dynamo_config)
    from_time = request.args.get('from')
    to_time = request.args.get('to')
    with dynamo_resource as dynamo_table:
        items = dynamo_table.get_data_in_timeframe(data_point_name, from_time, to_time)
    data_point_name_parsed = send_data_to_parse(api_config.calculations_service_url, items)
    return data_point_name_parsed
