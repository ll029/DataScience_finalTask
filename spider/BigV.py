from selenium import webdriver
import re
import time
from datetime import datetime,timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scroll():
    try:
        for i in range(3):
            driver.execute_script('window.scrollTo(1000,document.body.scrollHeight);')
            time.sleep(5)
    except Exception :
        print(Exception)
        data.to_excel('澎湃新闻2.xlsx')
        print('滑条出错')

def clickPinlun():
    scroll()
    source = driver.page_source
    bs = BeautifulSoup(source, 'lxml')
    action = bs.find_all('div', {'action-data':'cur_visible=0'})
    n = len(action)
    for i in range(4, n + 3):
        p_button = '//*[@id="Pl_Official_MyProfileFeed__26"]/div/div[' + str(i) + ']/div[2]/div/ul/li[3]/a'
        element1 = driver.find_element_by_xpath(p_button)
        driver.execute_script("arguments[0].click();", element1)

def get_page_num(u):
    driver.get(u)
    scroll()
    driver.implicitly_wait(5)
    source = driver.page_source
    bs = BeautifulSoup(source, 'lxml')
    p = len(bs.find('span', class_="list").find_all('li'))
    return p


def process(bs):

    info = pd.DataFrame(columns=['时间','内容','转发','评论','点赞'])
    items = bs.find_all("div", {'action-data': 'cur_visible=0'})
    li1 = [t.find('div', class_="WB_from S_txt2").a.text for t in items]
    # li2 = [t.find('div', class_='WB_text W_f14').text.split()[0] for t in items]
    li3 = []
    li4 = []
    li5 = []
    li6 = []
    li2 = []

    co = bs.find_all('ul', class_="WB_row_line WB_row_r4 clearfix S_line2")
        # 收藏，评论，转发，点赞
    for t in co:

        comment = t.text.split()
        li3.append(comment[1])
        li4.append(comment[2])
        li5.append(comment[3])

    for i in items:
        tem2 = i.find_all('div', class_='WB_text')
        li2.append(tem2[0].text.split()[0])
        if len(tem2) >= 20:
            tem2 = tem2[:20]
        c = len(tem2)
        res = ''
        for j in range(1, c, 2):
            res += " " + tem2[j].text.split()[0]
        li6.append(res)

    info['时间'] = li1
    info['内容'] = li2
    info['评论数'] = li3
    info['转发'] = li4
    info['点赞'] = li5
    info['评论'] = li6
    return info


driver = webdriver.Chrome()
url = 'https://s.weibo.com'
driver.get(url)
time.sleep(30)
data = pd.DataFrame(columns=['时间','内容','评论数','转发','点赞','评论'])


base_url = 'https://weibo.com/thepapernewsapp?profile_ftype=1&is_all=1#_0'
# weibo.com/p/1002062803301701/home?profile_ftype=1&is_search=1&key_word=%E7%96%AB&is_ori=1#_0
pages = get_page_num(base_url)

for i in range(1,pages+1):
    cur_url = 'https://weibo.com/thepapernewsapp?is_search=1&visible=0&is_ori=1&is_pic=1&is_video=1&is_music=1&' \
              'is_article=1&is_forward=1&is_text=1&key_word=%E7%96%AB&start_time=2019-12-08&end_time=2020-02-09&' \
              'is_tag=0&profile_ftype=1&page='+str(i)+'#feedtop'
    # https://weibo.com/p/1002062803301701/home?is_search=1&visible=0&is_ori=1&is_pic=1&is_video=1&is_music=1&is_article=1&is_forward=1&is_text=1&key_word=%E7%96%AB&start_time=2019-12-08&end_time=2020-06-30&is_tag=0&profile_ftype=1&page='+str(i)+'#feedtop
    # https://weibo.com/rmrb?is_search=1&visible=0&is_ori=1&is_pic=1&is_video=1&is_music=1&is_article=1&is_forward=1&is_text=1&key_word=%E7%96%AB&start_time=2019-12-08&end_time=2020-06-30&is_tag=0&profile_ftype=1&page=2#feedtop
    # https://weibo.com/rmrb?is_all=1&stat_date=202001&page=27#feedtop
    try:
        driver.get(cur_url)
        clickPinlun()
        source = driver.page_source
        bs = BeautifulSoup(source, 'lxml')
        data = data.append(process(bs))
    except Exception:
        data.to_excel('澎湃新闻2.xlsx')

    time.sleep(0.5)
data.to_excel('澎湃新闻2.xlsx')