# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 10:44
'''

import random
import matplotlib
from matplotlib import pyplot as plt

# 设置字体
font = {
    'family':'MicroSoft YaHei',
    'weight':'bold',
}
matplotlib.rc("font",**font)

x = range(120)
y = [random.randint(20,30) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

# 调整x轴的刻度
_xtick_lables = ['10点{}分'.format(i) for i in range(60)]
_xtick_lables += ['11点{}分'.format(i) for i in range(60)]

# 取步长，数字和字符串一一对应，数据的长度一样,rotation设置旋转的度数
plt.xticks(list(x)[::5], _xtick_lables[::5], rotation=45)

plt.yticks(range(15,40,5))
# 设置网格
plt.grid()
plt.show()
