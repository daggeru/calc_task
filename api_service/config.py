from abc import ABCMeta
from dataclasses import dataclass
from os import environ
from typing import Optional


@dataclass(frozen=True)
class ApiServiceConfig(metaclass=ABCMeta):
    host: str
    port: int
    calculations_service_url: str

    @classmethod
    def read_env(cls):
        return cls(
            host=environ['APP_HOST'],
            port=int(environ['APP_PORT']),
            calculations_service_url=environ.get('CALC_SERVICE_URL', 'https://some.url')
        )


@dataclass(frozen=True)
class DynamoTableConfig(metaclass=ABCMeta):
    region_name: str
    table_name: str
    endpoint: Optional[str]

    @classmethod
    def read_env(cls):
        return cls(
            region_name=environ.get('DYNAMODB_REGION', 'eu-west-1'),
            table_name=environ.get('DYNAMODB_TABLE_NAME', 'customer-data'),
            endpoint=environ.get('AWS_DYNAMO_DB_URL'),
        )


api_config = ApiServiceConfig.read_env()
dynamo_config = DynamoTableConfig.read_env()
