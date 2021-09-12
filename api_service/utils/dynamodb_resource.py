from boto3.dynamodb.conditions import Key

from config import DynamoTableConfig
from utils.db_utils import get_dynamo_resource


class DynamoResource:

    def __init__(self, config: DynamoTableConfig):
        self._config = config
        self._endpoint = config.endpoint,
        self._region_name = config.region_name

    def __enter__(self):
        resource = get_dynamo_resource(self._config)
        self.table = resource.Table(self._config.table_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            raise

    def save_to_table(self, item_to_save):
        self.table.put_item(Item=item_to_save)

    def batch_save_to_table(self, list_of_items):
        if not isinstance(list_of_items, list):
            list_of_items = [list_of_items]
        with self.table.batch_writer() as batch:
            for item in list_of_items:
                batch.put_item(Item=item)

    def get_data_in_timeframe(self, name, from_time=None, to_time=None):
        items = self.table.query(KeyConditionExpression=Key('name').eq(name),
                                 QueryFilter=Key('t').between(from_time, to_time))
        # todo try except: no items found -> items['Items'] would rise an error / KeyError
        return items['Items']
