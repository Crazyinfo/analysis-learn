# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:31:49 2019

@author: EV
"""

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4])
plt.show()

plt.plot([1,2,3,4], [1,4,9,16]) # x轴的数据，y轴的数据
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0,6,0,20]) # 设置坐标轴范围
plt.show()

t = np.arange(0, 5, 0.2) # 取0到5间的数字，步长为0.2
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


#使用关键字字符串绘图
data = {
        'a':np.arange(50),
        'c':np.random.randint(0,50,50), #按照给定的形状和范围产生随机整数
        'd':np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50) #按照给定形状产生一个多维数组，数组中的元素服从标准正态分布
data['d'] = np.abs(data['d']) * 100
plt.scatter(x='a',y='b',c='c',s='d',data=data) #散点图
'''
matplotlib.pylot.scatter(x, y, s=None, c=None, marker=None, cmap=None, 
norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, 
verts=None, edgecolors=None, hold=None, data=None, **kwargs)
'''
# s为大小，marker为显示的形状也可以是文字，c为颜色，alpha为透明度，edgecolor为边的颜色
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


#用分类变量绘图
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()