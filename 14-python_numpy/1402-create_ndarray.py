# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 17:41
'''
import random
import numpy as np

# 使用numpy生成数组，得到ndarray的数组类型
t1 = np.array([1,2,3,4,5])
print(t1)
print(type(t1))

t2 = np.array(range(5))
print(t2.dtype)

t3 = np.array(range(1,6,2),dtype='float')
print(t3)

t4 = np.array([1,0,1,0,1,1,0],dtype=bool)
print(t4)
print(t4.dtype)

# 调整数据类型
t5 = t4.astype('int8')
print(t5)

t6 = np.array([random.random() for i in range(10)])
print(t6)
print(t6.dtype)

t7 = np.round(t6,2)
print(t7)