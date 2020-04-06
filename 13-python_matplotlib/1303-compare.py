# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 14:20
'''

import matplotlib
from matplotlib import pyplot as plt

# 设置字体
font = {
    'family':'MicroSoft YaHei',
    'weight':'bold',
}
matplotlib.rc("font",**font)

y_1 = [1,0,0,0,1,0,4,0,3,0,5,1,2,1,3,5,1]
y_2 = [2,1,0,3,0,4,3,0,2,0,3,0,5,1,0,2,1]

plt.figure(figsize=(30,10),dpi=80)

plt.plot(range(13,30), y_1, label='java')
plt.plot(range(13,30), y_2, label='python')

# 调整x轴的刻度
_xtick_lables = ['{}岁'.format(i) for i in range(13,30)]


# 取步长，数字和字符串一一对应，数据的长度一样,rotation设置旋转的度数
plt.xticks(range(13,30), _xtick_lables, rotation=45)

# 设置网格及透明度
plt.grid(alpha=0.5)

# 添加图例
plt.legend()

plt.show()