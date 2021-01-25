# DataScience_finalTask

> 计算社会学：疫情背景下深描中国大众的网络社会心态

小组成员：胡越，李洪妍，刘璐

### 文件结构：

```python
│  README.md
├─digital_processing  # 数据处理相关代码所在文件
   ├─data.txt  # convert.py和fit_Gaussian.py所使用的数据存放的文件(每次手动粘入需要被处理的数据)
   ├─convert.py  # 对爬取下来的数据进行简单的格式处理
   ├─fit_Gaussian.py  # 绘制直方图和高斯拟合曲线
   ├─Iplot.py  # 绘制雷达图
   ├─line_graph.py  # 绘制折线图/直方图
   ├─mapping.py  # 心态词典映射所使用的代码
   ├─minddict.txt  # 心态词典(每一行对应一种心态,从上到下为焦虑、悲伤、愤怒、喜悦、感激、信任)
   ├─mood.xlsx  # line_graph.py绘图时使用的数据
   ├─stopWords  # 停用词表
   ├─心态分析.html  # Iplot.py生成的动态雷达图
   ├─心态变化折线图.html  # line_graph.py生产的动态折线图
   ├─映射_一阶段_官方媒体.xlsx		# 以下表格为心态映射得到的得分结果，表内最后一行为均值
   ├─映射_一阶段_民间媒体.xlsx
   ├─映射_一阶段_评论.xlsx
   ├─映射_三阶段_官方媒体.xlsx
   ├─映射_三阶段_民间媒体.xlsx
   ├─映射_三阶段_评论.xlsx
   ├─映射_二阶段_官方媒体.xlsx
   ├─映射_二阶段_民间媒体.xlsx
   ├─映射_二阶段_评论.xlsx
   ├─映射_四阶段_官方媒体.xlsx
   ├─映射_四阶段_民间媒体.xlsx
   ├─映射_四阶段_评论.xlsx
   └─雷达图数据.xlsx  # Iplot.py绘图使用的数据
├─spider  # 爬虫代码及所得数据
  ├─BigV.py  # 微博爬虫的代码
  ├─sinaSpider.py  # 新浪滚动新闻中心的爬虫代码
  └─爬下来的许多数据表格……
├─Data  # 原始数据以及处理中的所有数据
├─ccfx.m  # 层次分析法所使用的matlab代码
├─keywords_extraction.py
  ├─情感词.txt  # 知网情感词典：用以提取新闻文本及评论中的心态词
  ├─stopWords.txt  # 百度停用词表：用以新闻文本及评论分词得到关键词(手动添加一些干扰数据，如明星姓名等)
  ├─KeyWord.py  # 提取重点新闻中的关键词，并进行词频统计
  ├─TFIDF.py  # 提取重点新闻中的心态词，并计算TF-IDF
  ├─xinhua.py  # 爬取新华网网站中新闻正文
  └─词云.py  # 对文本进行分词词频统计后，制作词云图
└─Report  # 报告相关源文件以及最终报告的成品
```