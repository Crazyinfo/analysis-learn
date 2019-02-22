# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:05:09 2019

@author: EV
"""

import jieba
seg = jieba.cut("我来到华中科技大学", cut_all=True) # 全模式
print(", ".join(seg))
seg = jieba.cut("我来到华中科技大学") # 默认cut_all=False，即精确模式
print(", ".join(seg))
seg = jieba.cut_for_search("我来到华中科技大学") # 搜索引擎模式
print(", ".join(seg))


from collections import Counter

content = open('pachong.txt', encoding='utf-8').read()
print(Counter(content).most_common(10)) # 显示出现频率最高的前十词汇，但输出一般是符号等
con_words = [x for x in jieba.cut(content) if len(x) >= 2] # 进行过滤
print(Counter(con_words).most_common(10))

'''
有很多时候专有名词，像人名、地名等不可分的。这时可以自己自定义词典，以便包含jieba词库里面没有的词。虽然
jiebe有新词的识别能力，但是自行添加新词可以保证更高的正确率
命令格式：
jieba.load_userdict(file_name)
词典格式：
一词占一行；每行分为词语、词频(可省略)、词性(可省略)，用空格隔开(数字及空格均要半角)
'''
txt = '欧阳建国是创新办主任也是欢聚时代公司云计算方面的专家'
print(','.join(jieba.cut(txt)))
jieba.load_userdict('user_dict.txt')
print(','.join(jieba.cut(txt)))



# 文本词云图
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = open('pachong.txt', encoding='utf-8')
mylist = list(text)

word_list = [' '.join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)
wordcloud = WordCloud(font_path='simhei.ttf', background_color='white').generate(new_text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()


# 背景轮廓词云图的制作——抠廓图
from PIL import Image
import jieba
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
import matplotlib.pyplot as plt
content = open('pachong.txt', encoding='utf-8')
mylist = list(content)
word_list = [' '.join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)
#print(word_list, '\n\n', new_text)
pac_mask = imread('apchong.png')
wc = WordCloud(font_path='simhei.ttf', background_color='white', max_words=1000, mask=pac_mask).generate(new_text)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('ciyuntu文本.png') # 保存词云图

# 以上是根据文本生成词云，下面是根据词频生成词云
from PIL import Image
import jieba
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread
import matplotlib.pyplot as plt
from collections import Counter
content = open('pachong.txt', encoding='utf-8')
mylist = list(content)
word_list = [' '.join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)
con_words = [x for x in jieba.cut(new_text) if len(x) >= 2]
frequencies = Counter(con_words).most_common()
frequencies = dict(frequencies)
#print(frequencies)
wc = WordCloud(font_path='simhei.ttf', background_color='white', max_words=1000, mask=pac_mask).fit_words(frequencies)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('ciyuntu词频.png') # 保存词云图