# Python抽象基类:abc模块
# Python是动态类型，是没有变量的类型的，只是一个符号，可以指向任何类型的对象，无法做类型检查，易出错
# 抽象基类：
#   1.在基础的类中，设定一些方法，所有继承该基类的类，都必要覆盖整个基类的方法
#   2.抽象基类是无法用来实例化的

class Language:
    def __init__(self, language_list):
        self.language_list = language_list

    def __len__(self):
        return len(self.language_list)

language_list = Language(['Python', 'Java', 'Scala', 'Go'])
print(hasattr(language_list, '__len__'))

# 第一种情况：我们再某些情况下希望判定某个对象的类型
from collections.abc import Sized
isinstance(language_list, Sized)

# 第二种情况：我们需要强制某个子类必须实现某些方法
# eg：实现了一个web框架，继承cache（redis，cache，memorycache）
# 需要设计一个抽象基类，指定子类必须实现某些方法

# 模拟一个抽象基类：
class CacheBase:
    def get(self, key):
        raise NotImplementedError
        # pass

    def set(self, key, value):
        raise NotImplementedError
        # pass

class RedisCache(CacheBase):
    # 如果不调用set方法，则会抛出异常
    def set(self, key, value):
        pass
    # pass

redis_cache = RedisCache()
redis_cache.set('key', 'value')
