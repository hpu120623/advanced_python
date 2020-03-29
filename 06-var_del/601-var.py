# Python的变量是一个指针，可以理解为便利贴，可以贴在任何地方

a = 1 # 内存中声明int对象，为1，a贴在1上
a = 'aabc' # 过程：先生成对象，然后变量贴在上面

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(a is b) # 判断a和b是否是同一个对象
print(id(a), id(b))
