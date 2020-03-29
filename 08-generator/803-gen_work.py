# Python中函数的工作原理

def foo():
    bar()
def bar():
    pass

"""
python.exe会用一个叫做PyEval_EvalFramEx(c函数)去执行foo函数，首先会储藏间一个栈帧，栈帧也是一个对象
当foo调用子函数bar，又会创建一个栈帧，所有的栈帧是分配在堆内存上
"""

import dis
print(dis.dis(bar))

