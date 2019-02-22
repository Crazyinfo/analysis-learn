# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:30:02 2019

@author: EV
"""

import pandas as pd
import numpy as np

df = pd.read_excel('i_nuc.xls', sheet_name = 'Sheet7')
df = pd.DataFrame(df)
#print(df.head())
#print(df.数分.describe()) # 查看数分列的基本统计
#print(df.describe()) # 查看各列的基本统计
print(df.解几.size) # 计数
print(df.解几.max())
print(df.解几.min())
print(df.解几.sum())
print(df.解几.mean()) # 平均值或print(df['解几'].mean())
print(df.解几.var()) # 方差
print(df.解几.std()) # 标准差
print(df.解几.median()) # 中位数
print(df.median())
print(df.解几.mode()) # 众数
print(df.mode())
# 使用numpy求均值
print(np.mean(df['解几']))
print(np.average(df['解几']))

# 分组分析
print(df.groupby('班级')['军训', '英语', '体育'].mean())

# 分布分析
df['总分'] = df.英语+df.体育+df.军训+df.数分+df.高代+df.解几
bins = [min(df.总分)-1, 400, 450, max(df.总分)+1]
label = ['<=400', '400-450', '>=450']
df1 = pd.cut(df.总分, bins, labels=label)
df['总分分层'] = df1
print(df1.head())
print(df.groupby('总分分层')['总分'].agg({'人数':np.size}))

# 交叉分析
print(df.pivot_table(index=['班级', '姓名']))
print(df.pivot_table(['军训', '体育', '英语', '性别'], index=['班级', '姓名']))
print(df.pivot_table(values=['总分'], index=['总分分层'], columns=['性别'], aggfunc=[np.size, np.mean]))

# 结构分析
df2 = df.pivot_table(values=['总分'], index=['总分分层'], columns=['性别'], aggfunc=[np.sum])
print(df2)
print(df2.sum())
print(df2.sum(axis=1)) #按列合计
print(df2.div(df2.sum(axis=1), axis=0)) #按列占比
print(df2.div(df2.sum(axis=0), axis=1)) #按行占比

# 相关分析
print(df['高代'].corr(df['数分'])) # 两列的关系
print(df.loc[:, ['英语','体育','军训','解几','数分','高代']].corr()) # 求所有的相关系数