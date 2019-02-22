# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 00:06:39 2019

@author: EV
"""

import pandas as pd
import numpy
#df = pd.read_table('rz.txt', sep=" ")
#print(df.head())

#df = pd.read_csv('rz.csv', sep=",")
#print(df.head())

df = pd.read_excel('rz.xlsx', sep=",")
print(df)


# 重复值的处理
## bool值显示是否重复
print(df.duplicated())
## 指定列进行判断重复
print(df.duplicated('姓名'))
## 去除重复数据行
print(df.drop_duplicates())


# 缺失值处理
## 缺失数据的判断
print(df.isnull())
print(df.notnull())

## 缺失数据的处理
print(df.dropna()) #去除数据结构中值为空所对应的行

print(df.dropna(how='all')) # 当整行为空时才删除

print(df.fillna('?')) # 用？代替空值

print(df.fillna(method='pad')) # 用前一个数据值替代空值

print(df.fillna(method='bfill')) # 用后一个数据值替代空值，可用limit限制每行可以替代空值的数目

print(df.fillna(df.mean())) # 用平均值替代空值

print(df.fillna(df.mean()['高代':'解几'])) # 使用选择列的均值进行缺失值处理
#df.fillna(df.mean()['填补列名':'计算均值的列名']) # 用解几列的平均值填补高代列的空缺值

print(df.fillna({'数分':100, '高代':0}))
#df.fillna({'列名1':值1, '列名2':值2}) # 对不同的列填充不同的值

str1 = df['姓名'].astype(str)
print(str1.str.strip('赵'))
#strip() # 清楚字符型数据左右指定的字符，默认为空格||lstrip(),rstrip()


# 数据抽取
## 字段抽取：抽出某列上指定位置的数据做成新的列
print(df['学号'].astype(str))
str2 = df['学号'].astype(str)
print(str2.str.slice(0,6))

## 字段拆分：按指定的字符sep，拆分已有的字符串
df1 = pd.read_excel('i_nuc.xls', sheet_name='Sheet4')
print(df1)
print(df1['IP'].str.strip())
new = df1['IP'].str.split('.',1,True) # 按第一个‘.’分成两列，1表示新增列数
print(new)
new.columns = ['IP1', 'IP2-4'] # 给第一列、第二列增加列名称

## 重置索引：指定某列为索引，便于对其他数据进行操作
print(df.set_index('姓名'))
df2 = df.set_index('姓名')
print(df2.loc['成龙']) # 使用loc函数对成龙用户信息进行提取
### loc通过索引抽取行数据
### iloc通过索引号抽取行数据

## 记录抽取：根据一定的条件，对数据进行抽取
print(df1.电话==13322252452)
print(df1[df1.电话==13322252452])
print(df1[df1.电话>13500000000])
print(df1[df1.电话.between(13400000000,13999999999)])
print(df1[df1.电话==13322252452])
print(df1[df1.IP.isnull()])
print(df1[df1.IP.str.contains('222',na=False)])

## 随机抽样：随机从数据中按照一定的行数或者比例进行抽取数据
r = numpy.random.randint(0,10,3)
print(r) # 从0开始到10结束随机抽取3个，返回索引值序列
print(df1.loc[r,:])

## 通过索引抽取数据
### 通过索引名(标签)抽取数据
df3 = df1.set_index('学号') # 更改学号列为新的索引
print(df3)
print(df3.loc[2308024241: 2308024201]) # 选取a到b行的数据
print(df3.loc[:,'电话'].head()) # 选取电话列的数据，loc的第一个参数是行标签，第二个是列标签
### 通过索引号抽取数据
print(df1.iloc[1,0]) #选取第2行，第1列的值。返回单个值
print(df1.iloc[[0,2],:]) # 选取第1行和第3行的数据
print(df1.iloc[0:2,:]) # 选取第1行到第3行的数据(不包括第3行)
print(df1.iloc[:,1]) # 选取所有第2列的数据，返回一个Series
print(df1.iloc[:,1]) # 选取所有第2行的数据，返回一个Series

## 字典数据抽取：将字典数据抽取为dataframe
### 字典的key和value各做一列
d1 = {
      'a':'[1,2,3]',
      'b':'[0,1,2]'}
a1 = pd.DataFrame.from_dict(d1, orient='index')
a1.index.name = 'key'
b1 = a1.reset_index()
b1.columns = ['key','value']
print(b1)
### 字典里的每一个元素作为一列(同长)
d2 = {
      'a':[1,2,3],
      'b':[0,1,2]}
a2 = pd.DataFrame(d2)
print(a2)
### 字典里的每一个元素作为一列(不同长)
d3 = {
      'one':pd.Series([1,2,3]),
      'two':pd.Series([1,2,3,4])}
a4 = pd.DataFrame(d3)
print(a4)

# 插入记录concat

# 修改记录
## 整体替换
## 个别修改 
### 单值替换
### 指定列单值替换
### 多值替换

# 交换行或列
df5 = pd.DataFrame({'a':[1,2,3],'b':['a','b','c'],'c':['A','B','C']})
print(df5)
hang = [0,2,1]
print(df5.reindex(hang)) # 交换行
lie = ['a','c','b']
print(df5.reindex(columns=lie)) # 交换列

# 排名索引
