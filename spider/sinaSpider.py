from bs4 import BeautifulSoup
import requests
import openpyxl
from datetime import datetime, timedelta
import math


def main():
    # save_path = ".\\sina_roll.xls"
    # get data
    get_data()
    # save data


def get_data():
    global date
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '全阶段2_新浪'
    row = ['日期', '标题', '关键字', '链接', '正文', '评论数']
    sheet.append(row)

    # datalist = []
    start_dt = datetime(2019, 12, 23)
    end_dt = datetime(2020, 6, 15)
    dt = start_dt

    while dt <= end_dt:
        try:
            print(str(dt) + ": ")
            date = str(dt).split(" ")[0]
            etime = int(dt.timestamp())
            stime = etime + 86400
            ctime = stime
            index = 0
            url = "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&etime=" + str(etime) + "&stime=" + str(
                stime) + "&ctime=" + str(ctime) + "&date=" + date + "&k=&num=50&page=1"  # 从第一页的json文件里获取页数
            source = askURL(url)  # json文件
            page_count = math.ceil(source.get('result').get('total') / 50)  # 页数

            for i in range(0, page_count):  # 18次
                datalist = []  # 一页的数据
                try:
                    index += 1
                    url = "https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&etime=" + str(
                        etime) + "&stime=" + \
                          str(stime) + "&ctime=" + str(ctime) + "&date=" + date + "&k=&num=50&page=" + str(index)
                    source = askURL(url)  # json文件
                    for j in range(0, len(source['result']['data'])):  # 每一页的新闻数
                        key = source['result']['data'][j]['keywords']
                        title = source['result']['data'][j]['title']
                        if not str(key).__contains__("疫"):
                            break
                        data = [str(date), title, key]

                        news_url = source['result']['data'][j]['url']  # 链接
                        data.append(news_url)
                        # docid = source.get('result').get('data')[j].get('docid')  # 正文
                        data.append(get_Text(news_url))
                        comment_total = source['result']['data'][j].get('comment_total')

                        if comment_total is None:
                            data.append("--")
                        else:
                            data.append(comment_total)  # 评论量
                            commentid = source.get('result').get('data')[j].get('commentid')  # 评论内容
                            commentList = get_Comment(commentid)  # commentList: several hot comments
                            if commentList is not None:
                                for com in range(0, len(commentList)):
                                    data.append(commentList[com])
                                for ind in range(len(commentList), 5):
                                    data.append(" ")
                            else:
                                for com in range(0, 5):
                                    data.append(" ")
                        # except Exception as in_e:
                        #     print("最里层出错:第{}页第{}条".format(index, j + 1))
                        #     print(in_e.__cause__)
                        # continue
                        # else:
                        datalist.append(data)
                        print("第{}页第{}条".format(index, j + 1) + ": 完成")
                except Exception as mid_e:
                    print("第二层循环出错:第{}页".format(index))
                    print(mid_e.__cause__)
                    continue
                finally:
                    for item in datalist:
                        sheet.append(item)
                        wb.save('全阶段2_新浪.xlsx')

            dt += timedelta(days=1)
        except Exception as e:
            print("最外层循环出错:第{}天".format(str(date)))
            print(e.__cause__)
            dt += timedelta(days=1)
            continue


def get_Text(news_url):
    r = requests.get(news_url)
    r.encoding = r.apparent_encoding
    s = BeautifulSoup(r.text, "lxml").find_all('p')
    paragraphList = [i.text for i in s]
    return "".join(paragraphList)


def askURL(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.json()  # 返回json文件


if __name__ == "__main__":
    main()


# def get_Comment(commentid):
#     hotList = []
#     channel = str(commentid).split(":")[0]
#     itr = str(commentid).split(":")[1]
#     print(channel)
#     print(itr)
#     r = requests.get(
#         "http://comment5.news.sina.com.cn/page/info?format=json&channel=" + channel + "&newsid=" + itr)
#     # http://comment5.news.sina.com.cn/page/info?format=json&channel=cj&newsid=comos-imxxsth1660069
#     r.encoding = r.apparent_encoding
#     s = r.json()
#     commentList = s.get('result').get('hot_list')
#     if commentList is None:
#         return None
#     index = 0
#     while (index < 5) & (index < len(commentList)):
#         hotList.append(commentList[index].get('content'))
#         index += 1
#
#     return hotList
