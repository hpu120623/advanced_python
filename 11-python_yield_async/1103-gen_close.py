def gen_func():
    # 1.可以产出值 2.可以接收值
    try:
        html = yield 'http://projectsedu.com'
    except Exception:
    # except BaseException:
    # except GeneratorExit:
    #GeneratorExit是继承baseexception，不是exception
        pass
    yield 2
    # return 'python'
# 1.生成器不只可以产出值，还可以接收值

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close() # 在
    # next(gen)
