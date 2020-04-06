# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 10:28
'''

from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 13, 14.2, 16, 20, 22, 25, 22, 23, 20, 17, 15]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置x轴，y轴的刻度
_xtick_labels = [i / 2 for i in range(2, 49)]
plt.xticks(_xtick_labels[::3])
plt.yticks(range(min(y), max(y) + 1))

# # 保存
# plt.savefig('text.png')

# 展示图形
plt.show()
