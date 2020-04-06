# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 21:07
'''
"""数组拼接"""
import numpy as np

t1 = np.array(range(12)).reshape((1,2,6))
t2 = np.array(range(12,24)).reshape((1,2,6))
# print(t1)
# print(t2)
t3 = np.vstack((t1,t2)) # vstack竖直拼接
t4 = np.hstack((t1,t2)) # hstack水平拼接
print(t3)
print('-'*50)
print(t4)