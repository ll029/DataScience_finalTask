import jieba
import pandas as pd


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


data = pd.read_excel('C:\\Users\\86173\\OneDrive - smail.nju.edu.cn\\桌面\\学习\\数据科学基础\\大作业\\时间序列(map).xlsx')
dataDf = pd.DataFrame(data)
subjects = [str(a) for a in dataDf['内容'].tolist()]

# subjects=dataDf['评论'].tolist()

words = set(line.strip() for line in open('stopWords', encoding='utf-8'))
f = open('.\\minddict', 'r+', encoding='utf-8')
mind_list = f.readlines()

anxiety = mind_list[0].split(",")
sad = mind_list[1].split(",")
anger = mind_list[2].split(",")
joyful = mind_list[3].split(",")
appreciate = mind_list[4].split(",")
trust = mind_list[5].split(",")

mindset = {'焦虑': anxiety, '悲伤': sad, '愤怒': anger, '喜悦': joyful, '感激': appreciate, '信任': trust}
total_count = {'焦虑': [], '悲伤': [], '愤怒': [], '喜悦': [], '感激': [], '信任': []}

for subject in subjects:  # 每一项
    mindsetCount = {'焦虑': 0, '悲伤': 0, '愤怒': 0, '喜悦': 0, '感激': 0, '信任': 0}  # 每一项的多维心态值
    blist = jieba.cut(subject)  # 分词
    for item in blist:  # 该项中的每一个词
        if (item not in words) and (is_Chinese(item)):  # 不在停用词中且是汉字
            for i in mindset:  # 遍历六个心态
                if item in mindset.get(i):
                    mindsetCount[i] += 1
    # 除以量纲
    count = mindsetCount['焦虑'] + mindsetCount['悲伤'] + mindsetCount['愤怒'] + mindsetCount['喜悦']+ mindsetCount['感激'] + mindsetCount['信任']
    for i in mindsetCount:
        if count != 0:
            mindsetCount[i] = mindsetCount[i] / (count + 0.0)
        total_count[i].append(mindsetCount[i])

# content = {}
# for item in alist:
#     content[item] = content.get(item, 0) + 1
# # print(content)

contentDf = pd.DataFrame(columns=['项目', '焦虑', '悲伤', '愤怒', '喜悦', '感激', '信任'])
contentDf['项目'] = subjects
contentDf['焦虑'] = total_count['焦虑']
contentDf['悲伤'] = total_count['悲伤']
contentDf['愤怒'] = total_count['愤怒']
contentDf['喜悦'] = total_count['喜悦']
contentDf['感激'] = total_count['感激']
contentDf['信任'] = total_count['信任']
# contentDf = contentDf.reset_index().rename(columns={'index': '内容'})
# contentDf.head()

# contentDf = contentDf.sort_values(by='次数', axis=0, ascending=False)
# contentDf.reset_index(drop=True)
print(contentDf)
contentDf.to_excel('.\\映射_时间序列_评论.xlsx')