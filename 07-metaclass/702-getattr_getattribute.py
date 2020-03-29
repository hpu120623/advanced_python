# __getattr__在查找不到属性的时候调用
# __getattribute__
from datetime import date, datetime
class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        return 'not find attr'

if __name__ == '__main__':
    user = User('python', date(year=1987, month=1, day=1))
    print(user.age)
    print(user.name)