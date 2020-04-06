# coding=utf-8

'''
Author: Amos.Li
Email: hpu120623@126.com

date: 2020/4/5 17:58
'''
# 轴：axis

import numpy as np

file_path = './test_data.csv'
t1 = np.loadtxt(file_path,delimiter=',',dtype='int',unpack=True) # 按列展示
t2 = np.loadtxt(file_path,delimiter=',',dtype='int') # 不按列展示
# print(t1)
# print('='*50)
# print(t2)

# 取行
# print(t2[3])
# print(t2[:3])
# print(t2[[0,2,1]])

# 取列
# print(t2[:,0])

# 取连续的多列
# print(t2[:,2:])

# 取不连续的多列
# print(t2[:,[0,3]])

# 取多行和多列，第三行，第4列
# print(t2[2,3])

# 取第3行到第5行，第2列到第4列的结果
# print(t2[2:5,1:4])

t3 = np.array(range(24)).reshape((2,3,4))
print(t3)
t4 = t3.clip(10,18) # clip(10,18)将小于10的替换为10，大于18的替换为18
# print(t4)
t5 = np.where(t3<15,0,20) # np的三元运算符，把小于15的替换为0，大于15的替换为20
# print(t5)
print(t3[0,1,2])

