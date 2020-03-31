def gen_func():
    # 1.可以产出值 2.可以接收值
    try:
        yield 'http://projectsedu.com'
    except Exception:
        pass

    yield 2

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, 'download error')