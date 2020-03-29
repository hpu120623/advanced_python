# 生成器函数，函数里只要有yield关键字，返回生成器对象
def gen_func():
    yield 1
    yield 2


# 惰性求值：延迟求值提供了可能
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    gen = gen_func()
    print(gen)
    for item in gen:
        print(item)
    print(fib(10))
    print(fib2(10))
    for num in gen_fib(10):
        print(num)
