# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:00:12 2019

@author: EV
"""

import numpy as np
import matplotlib.pyplot as plt


my_array = np.array([1,2,3,4,5])
print(my_array)
print(my_array.shape)
print(my_array[0])
my_array[0] = -1
print(my_array)


my_new_array = np.zeros((5)) 
print(my_new_array)
#my_new_array = np.ones((5)) 
#print(my_new_array)

my_random_array = np.random.random((5))
print(my_random_array)

# 二维数组
my_2d_array = np.zeros((2, 3))
print(my_2d_array)

# 矩阵相乘
#dot()

# MD Array,
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
print(a[2,4]) # >>>25
print(a[0, 1:4]) # >>>[12 13 14]
print(a[1:4, 0]) # >>>[16 21 26]
print(a[::2,::2]) # >>>[[11 13 15]
                  #     [21 23 25]
                  #     [31 33 35]]
print(a[:, 1]) # >>>[12 17 22 27 32]


print(type(a)) # >>><class 'numpy.ndarray'>
print(a.dtype) # >>>int64
print(a.size) # >>>25
print(a.shape) # >>>(5, 5)
print(a.itemsize) # >>>8
print(a.ndim) # >>>2
print(a.nbytes) # >>>200


# Basic Operators
a = np.arange(25)
a = a.reshape((5, 5))

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5,5))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b)
print(a > b)

print(a.dot(b))


# dot, sum, min, max, cumsum
a = np.arange(10)

print(a.sum()) # >>>45
print(a.min()) # >>>0
print(a.max()) # >>>9
print(a.cumsum()) # >>>[ 0  1  3  6 10 15 21 28 36 45]


# 花式索引
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
print(b)

# 布尔屏蔽
# Boolean masking
a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a,b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()


# Incomplete Indexing缺省索引
a = np.arange(0, 100, 10)
b = a[:5]
c = a[a >= 50]
print(b) # >>>[ 0 10 20 30 40]
print(c) # >>>[50 60 70 80 90]


# Where函数
a = np.arange(0, 100, 10)
b = np.where(a < 50) 
c = np.where(a >= 50)[0]
print(b) # >>>(array([0, 1, 2, 3, 4]),)
print(c) # >>>[5 6 7 8 9]