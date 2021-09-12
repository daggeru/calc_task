import boto3 as boto3


def get_dynamo_resource(config):
    dynamo_resource = boto3.resource(service_name='dynamodb',
                                     endpoint_url=config.endpoint,
                                     region_name=config.region_name)
    return dynamo_resource
