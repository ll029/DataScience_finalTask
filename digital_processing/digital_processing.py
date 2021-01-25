import glob

if __name__ == "__main__":
    # 对爬取得到的数据格式进行处理
    xmls = glob.glob('.\\data')
    for one_xml in xmls:
        print(one_xml)
        f = open(one_xml, 'r+', encoding='utf-8')
        all_the_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_the_lines:
            line = line.replace('', '')
            # line = line.replace('评论', '')
            f.write(line)
        f.close()
