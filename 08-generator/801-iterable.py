# 什么是迭代协议
# 迭代器是什么？迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，提供了一种惰性方式数据的方式
# []是__getitem__，list:__iter__
# 实现__iter__是可迭代对象，实现__iter__和__next__是迭代器

from collections.abc import Iterable, Iterator

class Language:
    def __init__(self, language_list):
        self.language_list = language_list

    def __iter__(self):
        return MyIterator(self.language_list)

    # def __getitem__(self, item):
    #     return self.language_list[item]


class MyIterator(Iterator):
    def __init__(self, language_list):
        self.iter_list = language_list
        self.index = 0

    # 真正返回迭代值的逻辑
    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except StopIteration:
            raise StopIteration
        self.index += 1
        return word

if __name__ == '__main__':
    language_list = Language(['Python', 'Java', 'Scala', 'Go'])
    my_iter = iter(language_list)
    while True:
       print(next(my_iter))