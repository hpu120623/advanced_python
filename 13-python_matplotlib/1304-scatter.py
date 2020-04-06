# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 15:19
'''
"""散点图scatter："""
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(50)
y = x + 5*np.random.rand(50)
plt.scatter(x,y)
plt.show()