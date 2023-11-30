import requests
from bs4 import BeautifulSoup

# 发送HTTP请求获取网页内容
url = "https://news.qlu.edu.cn/2023/1121/c811a229627/page.htm"
response = requests.get(url)
# 设置文本编码
response.encoding = "UTF-8"
# 将文本加载为文本形式
html_content = response.text

# 使用BeautifulSoup解析网页
the_web = BeautifulSoup(html_content, "html.parser")

# 找到所有的标题
all_titles = the_web.find_all(attrs={"class": "arti_title"})
# 找到所有的正文文本
all_text = the_web.find_all(attrs={"class": "p_text_indent_2"})

# 将爬取的文本写入文件中
# 标题：
filename = "file/qigongda_news.txt"
with open(filename, "w") as file_write:
    for one_titles in all_titles:
        file_write.write(one_titles.text)
# 正文：
with open(filename, "a") as file_add:
    file_add.write("\n\n")
    for one_p in all_text:
        file_add.write(one_p.text + "\n")


# 获取新闻标题,选择标签
# news_titles = the_web.select(".arti_title")
# for title in news_titles:
#     # print(title.text)
#     pass

# # 爬取新闻界面的正文内容
# news_article = the_web.select(".p_text_indent_2")
# for article in news_article:
#     # print(article.text)
#     pass
# # 写入文本
# filename = "file/qigongda_news.txt"
# with open(filename, "w") as file_write:
#     for article in news_article:
#         # print(article.text)
#         if article.text == " ":
#             file_write.write("\n")
