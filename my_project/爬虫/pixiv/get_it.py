from bs4 import BeautifulSoup
import requests


# 加载图片详情页地址
def find_more(month_web, pix):
    div_more = month_web.find_all(attrs={"class": "ranking-image-item"})
    for tag_a in div_more:
        for a in tag_a.find_all("a"):
            pix.img_more.append(a.get("href"))


# 加载图片原图地址
def find_img(pix):
    for more in pix.img_more:
        # 计数
        pix.fact_img -= 1
        # 判断终止
        if pix.fact_img < 0:
            break
        # 补充网址
        url = pix.url_pixiv + more
        print(url)
        # 解析网页
        more_web = return_web(url)

        #
        #
        #
        #
        with open("filenametxt.html", "w", encoding="utf-8") as file_write:
            for one in more_web:
                file_write.write(str(one))

        #
        #
        #
        # 寻找图片标题
        img_title = more_web.find_all(attrs={"class": "sc-1u8nu73-3 huVRfc"})
        print(img_title)
        # 寻找图片原图
        img_original_a = more_web.find_all(
            attrs={"class": "sc-1qpw8k9-3 ilIMcK gtm-expand-full-size-illust"}
        )
        for href in img_original_a:
            img_original = href.get("href")
            print(img_original)
            print("66")


# 解析网页
def return_web(url):
    # 设置headers参数
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    }
    # 发送HTTP请求获取网页内容
    response = requests.get(url, headers=headers)
    # 设置文本编码
    response.encoding = "UTF-8"
    # 将文本加载为文本形式
    html_content = response.text
    # 使用BeautifulSoup解析网页
    return BeautifulSoup(html_content, "html.parser")
