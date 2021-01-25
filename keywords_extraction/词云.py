# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:40:22 2021

@author: DELL
"""

import pandas as pd
import jieba
import matplotlib.pyplot as plt
from os import path
from imageio import imread
from wordcloud import WordCloud

def loadDataSet(filePath, file, column):

    data=pd.read_excel(filePath+file)
    dataDf=pd.DataFrame(data)
    subjects=[str(a) for a in dataDf[column].tolist()]

    words=set(line.strip() for line in open(filePath+'\\情感词.txt', encoding='utf-8'))

    alist = [] 

    for subject in subjects:
        blist=jieba.cut(subject)     
        for item in blist:
            if item in words:
                alist.append(item)
    
    return alist
 

 
if __name__=='__main__':
    filePath = 'E:\\lhy\\3-sophomore First\\Fundamentals of Data Science\\BIGBIGBIG\\词云'
    file = '\\人民央视澎湃_加权重点评论.xlsx'
    column = '评论'
  
    dataset = loadDataSet(filePath, file, column)
    
    content={}
    for item in dataset:
        content[item]=content.get(item,0)+1


    d=path.dirname(__file__)
    mask=imread(path.join(d, filePath+'\\抗疫-3.png'))
    wc=WordCloud(font_path='simhei.ttf',background_color='white',mask=mask).generate_from_frequencies(content)
    plt.imshow(wc)
    plt.axis("off")
    wc.to_file(filePath+'\\人民央视澎湃_加权重点评论_抗疫-3.png')
    plt.show()

