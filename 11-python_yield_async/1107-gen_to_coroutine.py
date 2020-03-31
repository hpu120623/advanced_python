# 生成器是可以暂停的函数
import inspect
# def gen_func():
#     value = yield from [1,2,3]
#     # 1.返回值给调用方 2.调用放通过send方式返回值给gen
#     return 'python'


if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except Exception:
        pass
    print(inspect.getgeneratorstate(gen))