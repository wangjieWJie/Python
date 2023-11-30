import requests
from bs4 import BeautifulSoup


def load_news(st):
    for one_link in st.news_link:
        if one_link[0] == "/":
            one_link = st.url_start + one_link
            # 发送HTTP请求获取网页内容
            news_response = requests.get(one_link)
            # 设置文本编码
            news_response.encoding = "UTF-8"
            # 将网页加载为文本形式
            html_content = news_response.text
            # 使用BeautifulSoup解析网页
            news_web = BeautifulSoup(html_content, "html.parser")
            # 执行成功
            print("that is OK")

            # 获取相应文本内容
            get_content(news_web, st)
        else:
            print("Error")
    st.news_link = []


def get_content(news_web, st):
    # 找到所有的标题
    all_titles = news_web.find_all(attrs={"class": "arti_title"})
    # 找到所有的正文文本
    all_text = news_web.find_all(attrs={"class": "p_text_indent_2"})

    # 将文章储存为txt文件
    save_txt(all_titles, all_text, st)


def save_txt(title, texts, st):
    # 计数：
    print(str(st.downloaded) + "/" + str(st.news_total))
    st.downloaded = st.downloaded + 1
    filename = ""
    # 设置文件名及文件储存位置
    for one_titles in title:
        filename = st.file_address + one_titles.text.replace("\n", "") + ".txt"
        # 将爬取的文本写入文件中
        # 标题：
        # print(filename)
        with open(filename, "w", encoding="utf-8") as file_write:
            for one_titles in title:
                file_write.write(one_titles.text)
        # 正文：
        with open(filename, "a", encoding="utf-8") as file_add:
            file_add.write("\n\n")
            for one_p in texts:
                file_add.write(one_p.text + "\n")


class Setting:
    def __init__(self) -> None:
        # 爬取文件储存位置
        self.file_address = "file/QGD_ZHXW/"
        # 网站地址 : https://news.qlu.edu.cn/年份/月日/序号/page.htm
        self.url_start = "https://news.qlu.edu.cn/"
        self.url_end = "/page.htm"
        # 年份/
        self.url_year = "2023/"
        # 月日
        self.url_MD = "11/29"

        # 媒体工大新闻目录：
        self.url_list = ""
        # 媒体工大新闻目录开头：
        self.url_list_start = "https://news.qlu.edu.cn/zhxw/list"
        # 媒体工大新闻目录后缀
        self.url_list_end = "" + ".psp"
        # 目录页码数
        self.url_list_num = 0
        # 最大爬取页码数：
        self.get_list = 10

        # 存储每个新闻链接地址的列表
        self.news_link = []

        # 计数器
        # 总文章数：
        self.news_total = self.get_list * 14
        # 当前下载数：
        self.downloaded = 1


# 设置设置
st = Setting()
# 开始爬取新闻目录中的网址：
#   编写网页地址
while st.url_list_num < st.get_list:
    if st.url_list_num == 0:
        url_list = st.url_list_start + st.url_list_end
    elif st.url_list_num > 0:
        url_list = st.url_list_start + str(st.url_list_num) + st.url_list_end
    st.url_list_num = 1 + st.url_list_num
    print(url_list)

    # 发送HTTP请求获取网页内容
    response = requests.get(url_list)
    # 设置文本编码
    response.encoding = "UTF-8"
    # 将网页加载为文本形式
    html_content = response.text
    # 使用BeautifulSoup解析网页
    list_web = BeautifulSoup(html_content, "html.parser")

    # 爬取新闻列链接
    news_all = list_web.find_all("span", attrs={"class": "news_title"})
    for one_news in news_all:
        tag_a = one_news.find_all("a")
        for a_link in tag_a:
            st.news_link.append(a_link.get("href"))

    # 加载新闻链接
    load_news(st)


print(" OVER !")
