# 垃圾回收和del语句
# Python的垃圾回收算法是采用引用计数
# 示例如下：内存中创建int为1，a和b同时指向1，那么1的计数器为2，del a后，a不存在，b还在
a = 1
b = a
del a
print(b)
print(a)

class A:
    def __del__(self):
        pass