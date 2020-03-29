class User:
    # __new__在生成实例前调用
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super().__new__(cls)

    # init是用来完善对象的
    # 如果new方法不返回对象向，则不会调用init
    def __init__(self, name):
        print('in init')
        self.name = name

if __name__ == '__main__':
    user = User('Python')