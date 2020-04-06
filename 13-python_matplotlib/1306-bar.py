# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 15:49
'''
"""柱状图bar"""
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(5)
y1, y2 = np.random.randint(1, 25, size=(2, 5))
width = 0.25
plt.bar(x, y1, width, color='r')
plt.bar(x + width, y2, width, color='g')
plt.xticks(x + width, ['a', 'b', 'c', 'd', 'e'])
plt.show()
