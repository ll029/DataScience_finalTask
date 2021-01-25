# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 00:38:33 2021

@author: DELL
"""

# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import operator
import pandas as pd
import jieba


def loadDataSet(filePath, file, column):


    data=pd.read_excel(filePath+file)
    dataDf=pd.DataFrame(data)
    subjects=[str(a) for a in dataDf[column].tolist()]

    words=set(line.strip() for line in open(filePath+'\\情感词.txt', encoding='utf-8'))

    dataset = [] 

    for subject in subjects:
        alist=[]
        blist=jieba.cut(subject)     
        for item in blist:
            if item in words:
                alist.append(item)
        dataset.append(alist)
    
    return dataset
 
 

def feature_select(list_words):
    #总词频统计
    doc_frequency=defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i]+=1
 
    #计算每个词的TF值
    word_tf={}  
    for i in doc_frequency:
        word_tf[i]=doc_frequency[i]/sum(doc_frequency.values())
 
    #计算每个词的IDF值
    doc_num=len(list_words)
    word_idf={} 
    word_doc=defaultdict(int) 
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i]+=1
    for i in doc_frequency:
        word_idf[i]=math.log(doc_num/(word_doc[i]+1))
 
    #计算每个词的TF*IDF的值
    word_tf_idf={}
    for i in doc_frequency:
        word_tf_idf[i]=word_tf[i]*word_idf[i]
 
    # 对字典按值由大到小排序
    dict_feature_select=sorted(word_tf_idf.items(),key=operator.itemgetter(1),reverse=True)
    return dict_feature_select
 
if __name__=='__main__':
    filePath = 'E:\\lhy\\3-sophomore First\\Fundamentals of Data Science\\BIGBIGBIG\\关键词'
    file = '\\澎湃新闻第一阶段.xlsx'
    column = '评论'
    
    data_list=loadDataSet(filePath, file, column) 
    features=feature_select(data_list) 
    #print(features)
    
    
    contentDf = pd.DataFrame(features, columns = ['词','TFIDF'])
    #contentDf = contentDf.reset_index().rename(columns = {'index':'词'})
    contentDf.head()

    contentDf = contentDf.sort_values(by = 'TFIDF', axis = 0,ascending = False)
    contentDf.reset_index(drop=True)
    print(contentDf)
    contentDf.to_excel(filePath+'\\澎湃新闻第一阶段评论TFIDF.xlsx')
    