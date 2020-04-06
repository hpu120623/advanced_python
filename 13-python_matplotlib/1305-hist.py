# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 15:37
'''
"""直方图hist："""
import numpy as np
from matplotlib import pyplot as plt

plt.hist(np.random.rand(100), bins=10, color='b', alpha=0.5)
plt.show()
