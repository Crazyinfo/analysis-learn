# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df = pd.read_excel('rz.xlsx')
df1 = pd.DataFrame(df)
#print(df1)
#print(df1.shape)

df2 = df1.duplicated() #显示重复的行
#print(df2.tail())
#print(df1[df2])
df3 = df1.drop_duplicates() # 去除重复行
#print(df3)
#print(df3.shape)

#print(df3.isnull()) # 判断空值
#print(df3.isnull().any()) # 判断哪些列存在缺失值
#print(df3[df3.isnull().values==True]) # 显示存在缺失值的行
df4 = df3.fillna(0)
#print(df4)

df0 = df4.copy() # 为了数据安全，先复制一份

df0['解几'] = df4['解几'].astype(str).map(str.strip)

#print(df0)

for i in list(df0.columns):
	if df0[i].dtype == object:
		pass
		#print(i) # 输出不是int类型的列
'''
解几是因为前面处理空格时进行了格式转化，转为str
姓名和性别是str，后续不参加运算无需转化
体育和军训不是int是因为里面有缺考和作弊字段，应用0代替
'''
df0['解几'] = df4['解几'].astype(int) # 将解几转为int类型
ty = list(df0.体育)
j = 0
for i in ty:
	if type(i) != int:
		ty[j] = 0
	j = j + 1
#print(dy)
df0['体育'] = ty # 替换
# 同样的方法对军训
jx = list(df0.军训)
j = 0
for i in jx:
	if type(i) != int:
		jx[j] = 0
	j = j + 1
#print(jx)
df0['军训'] = jx # 替换
# 若数据量不多时，可以用df0.replace({'体育':'作弊','军训':'缺考'}, 0)
#print(df0)

# 计算总分并分类别
df5 = df0.copy()
df5['score'] = df5.英语+df5.体育+df5.军训+df5.数分+df5.高代+df5.解几
#print(df5.score.describe()) # 查看score的最大最小值以及总记录数等信息
# 分组的区域划分
bins = [df5.score.min()-1, 400, 450, df5.score.max()+1]
label = ['一般', '较好', '优秀']
df6 = pd.cut(df5.score, bins, right = False, labels = label)
df5['类别'] = df6
print(df5)

# 军训成绩较为随意，把各科成绩标准化再汇总，再分组
for i in list(df0.columns[4:]):
	df0[i] = (df0[i] - df0[i].min())/(df0[i].max() - df0[i].min()) # 数据标准化
#print(df0.tail())
df0['score'] = df0.英语+df0.体育+df0.军训+df0.数分+df0.高代+df0.解几
#print(df0.score.describe())
bins = [df0.score.min()-1, 3, 4, df0.score.max()+1]
label = ['一般', '较好', '优秀']
df_0 = pd.cut(df0.score, bins, right = False, labels = label)
df0['类别'] = df_0
print(df0)