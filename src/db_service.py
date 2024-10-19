from abc import ABC, abstractmethod
from environs import Env

import redis


class UrlNotFoundException(Exception):
    detail = "Url not found!"


class DBService(ABC):
    @abstractmethod
    def set_url(self, url, short_url, expire_time):
        pass

    @abstractmethod
    def get_url(self, short_url):
        pass


class RedisDBService(DBService):
    def __init__(self, host, port, db):
        self.client = redis.Redis(host=host, port=port, db=db)

    def set_url(self, url, short_url, expire_time):
        self.client.set(
            short_url,
            url,
            ex=expire_time,
        )

    def get_url(self, short_url):
        url = self.client.get(short_url)
        if url is None:
            raise UrlNotFoundException
        return url.decode()


db_service = RedisDBService(host=Env().str('REDIS_LOCATION'), port=6379, db=0)
