import requests
from bs4 import BeautifulSoup


def load_news(news_link):
    url_all_url = []
    for one_link in news_link:
        if one_link[0] == "/":
            one_link = url_start + one_link
            # 发送HTTP请求获取网页内容
            news_response = requests.get(one_link)
            # 设置文本编码
            news_response.encoding = "UTF-8"
            # 将网页加载为文本形式
            html_content = news_response.text
            # 使用BeautifulSoup解析网页
            news_web = BeautifulSoup(html_content, "html.parser")
            print("that is OK")

            # 获取相应文本内容
            get_content(news_web)
        else:
            # 发送HTTP请求获取网页内容
            news_response = requests.get(one_link)
            # 设置文本编码
            news_response.encoding = "UTF-8"
            # 将网页加载为文本形式
            html_content = news_response.text
            # 使用BeautifulSoup解析网页
            news_web = BeautifulSoup(html_content, "html.parser")
            print("that also is OK")


def get_content(news_web):
    # 找到所有的标题
    all_titles = news_web.find_all(attrs={"class": "arti_title"})
    # 找到所有的正文文本
    all_text = news_web.find_all(attrs={"class": "p_text_indent_2"})


# 爬取文件储存位置
file_address = "file/QGDnews"
# 网站地址 : https://news.qlu.edu.cn/年份/月日/序号/page.htm
url_start = "https://news.qlu.edu.cn/"
url_end = "/page.htm"
# 年份/
url_year = "2023/"
# 月日
url_MD = "11/29"

# 媒体工大新闻目录：
url_list = ""
# 媒体工大新闻目录开头：
url_list_start = "https://news.qlu.edu.cn/826/list"
# 媒体工大新闻目录后缀
url_list_end = "" + ".psp"
# 目录页码数
url_list_num = 0
# 最大爬取页码数：
get_list = 1

# 存储每个新闻链接地址的列表
news_link = []


# 开始爬取新闻目录中的网址：
#   编写网页地址
while url_list_num < get_list:
    if url_list_num == 0:
        url_list = url_list_start + url_list_end
    elif url_list_num > 0:
        url_list = url_list_start + str(url_list_num) + url_list_end
    url_list_num = 1 + url_list_num
    print(url_list)

    # 发送HTTP请求获取网页内容
    response = requests.get(url_list)
    # 设置文本编码
    response.encoding = "UTF-8"
    # 将网页加载为文本形式
    html_content = response.text
    # 使用BeautifulSoup解析网页
    list_web = BeautifulSoup(html_content, "html.parser")

    # 爬取新闻列表
    news_all = list_web.find_all("span", attrs={"class": "news_title"})
    for one_news in news_all:
        tag_a = one_news.find_all("a")
        for a_link in tag_a:
            news_link.append(a_link.get("href"))

    # 加载新闻链接
    load_news(news_link)

print(news_link)
