# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 23:06:55 2021

@author: DELL
"""

import jieba
import pandas as pd

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


filePath = 'E:\\lhy\\3-sophomore First\\Fundamentals of Data Science\\BIGBIGBIG\\lhy\\关键词_加权'

data=pd.read_excel(filePath+'\\人民央视_加权重点.xlsx')
dataDf=pd.DataFrame(data)
subjects=[str(a) for a in dataDf['评论'].tolist()]


words=set(line.strip() for line in open(filePath+'\\stopWords.txt', encoding='utf-8'))

alist=[]
for subject in subjects:
    blist=jieba.cut(subject)     
    for item in blist:
        if item not in words:
            if is_Chinese(item):
                alist.append(item)

content={}
for item in alist:
    content[item]=content.get(item,0)+1
#print(content)

contentDf = pd.DataFrame(pd.Series(content), columns = ['次数'])
contentDf = contentDf.reset_index().rename(columns = {'index':'词'})
contentDf.head()

contentDf = contentDf.sort_values(by = '次数', axis = 0,ascending = False)
contentDf.reset_index(drop=True)
print(contentDf)
contentDf.to_excel(filePath+'\\人民央视_加权重点_评论关键词.xlsx')
