# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:41:38 2019

@author: EV
"""

# 使用聚类分析：在没有划分类别的情况下，根据数据的相似度进行分组的一种方法，原则：
#    组内距离最小化而组间距离最大化
# 使用K-Means算法

# 基于RFM模型使用K-Means算法聚类航空小飞机行为特征数据


import pandas as pd

data = pd.read_excel('i_nuc.xls', index_col='Id', sheet_name='Sheet2') # 读取文件

k = 3 #聚类的类别
iteration = 500 #聚类最大循环次数
data_zs = 1.0 * (data - data.mean())/data.std() #数据标准化
#data_zs.to_excel('zsdata.xls', index=False) #数据写入，备用

from sklearn.cluster import KMeans
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration) #分为k类，并发数4

model.fit(data_zs) #开始聚类
print(model.fit(data_zs))

r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis=1) #横向连接(0是纵向)，得到聚类中心对应类别下的数目
r.columns = list(data.columns) + ['类别数目'] #重命名表头
print(r)
# 详细输出原始数据及其类别,model.labels_表示属于三类中的类别
r = pd.concat([data, pd.Series(model.labels_, index = data.index)], axis = 1)
r.columns = list(data.columns) + ['聚类类别']
print(r)
#r.to_excel('outputfile.xls') #数据写入，备用

def density_plot(data): #自定义作图函数
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
    p = data.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    [p[i].set_ylabel('密度') for i in range(k)]
    plt.xlabel('分解%s' % (i+1))
    plt.legend()
    return plt

for i in range(k):
    density_plot(data[r['聚类类别']]==i).savefig('pd_%s.png' % i)