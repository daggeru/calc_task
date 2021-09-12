from abc import ABCMeta
from dataclasses import dataclass
from os import environ


@dataclass(frozen=True)
class CalculationsServiceConfig(metaclass=ABCMeta):
    host: str
    port: int

    @classmethod
    def read_env(cls):
        return cls(
            host=environ['APP_HOST'],
            port=int(environ['APP_PORT']),
        )


calc_config = CalculationsServiceConfig.read_env()
