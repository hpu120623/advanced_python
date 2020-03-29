# 模拟一个抽象基类：
import abc
from collections.abc import *

class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
            raise NotImplementedError

    @abc.abstractmethod
    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    # 强制子类必须使用get，set方法
    # def get(self, key):
    #     print('已实现get')

    def set(self, key, value):
        print('已实现set')

redis_cache = RedisCache()
redis_cache.set('key', 'value')
