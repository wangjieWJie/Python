from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}
# 发送HTTP请求获取网页内容
response = requests.get(
    "https://www.haitangsoshu.org/book/21800/582866_1.html", headers=headers
)

# 设置文本编码
response.encoding = "UTF-8"
# 将文本加载为文本形式
html_content = response.text
# 使用BeautifulSoup解析网页
web = BeautifulSoup(html_content, "html.parser")

text = []

novel = web.find_all("p", attrs={"style": "text-indent:2em; padding:0px; margin:0px;"})
for pn in novel:
    text.append(pn.text)
print(text)
