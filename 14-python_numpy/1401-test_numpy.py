# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 16:11
'''

import numpy as np

t1 = np.arange(10)
print(t1)
print(t1.shape)
t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)
t4 = np.arange(12)
print(t4.reshape((3,4)))
print('-'*10)
t5 = np.arange(30).reshape((2,3,5))
print(t5)
print(t5.reshape((1,30)))
# t6 = t5.reshape((t5.shape[0]*t5.shape[1],))
# print(t6)
print(t5.flatten())
print(t5+2) # 广播机制
print('='*20)
t7 = np.arange(5)
print(t5)
print(t7)
print(t5-t7)

t8 = np.arange(3).reshape((3,1))
print(t8)
print(t5-t8)

t9 = np.arange(10)
