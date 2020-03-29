# 区别is和==
# is判断两个对象的id是否相同
# ==
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(a is b) # False,a不是b
print(a == b) # True, a和b的值相等

c = 1
d = 1 # 区别数字、字符串和列表的不同
print(c is d)