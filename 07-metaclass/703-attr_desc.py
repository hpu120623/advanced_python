import numbers
from datetime import date, datetime


class IntField:
    # 数据描述符__get__,__set__
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 限定值为int类型
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if value < 0:
            raise ValueError('positive value need')
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    # 非数据描述符
    def __get__(self, instance, owner):
        pass


class User:
    age = IntField()


if __name__ == '__main__':
    user = User()
    # user.age = 'ab'
    user.age = 30
    user.age = -2
    print(user.age)
