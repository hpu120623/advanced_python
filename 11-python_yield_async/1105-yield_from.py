# python3.3添加了yield from语句
# chain将迭代的类型连接起来，做一个for循环

from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    'lan1': 'python',
    'lan2': 'python',
    'lan3': 'python'
}

# yield from iterable
def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value

for item in my_chain(my_list, my_dict, range(5, 8)):
# for item in chain(my_list, my_dict, range(5, 8)):
    print(item)

def g1(gen):
    yield from gen

def main():
    g = g1([1,2,3])
    g.send(None)

# 1.main调用g1（委托方生成器）gen子生成器
# yield from 会在调用方内部与子生成器建立一个通道，双向通道
