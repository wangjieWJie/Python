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
    # 设置params参数
    params = {"mode": "monthly"}
    # 设置headers参数
    headers = {
        "login_id": "wangjie18706647540@gmail.com",
        "password": "123.q123.q",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "cookie": "p_ab_id=9; p_ab_id_2=6; p_ab_d_id=2070108976; _fbp=fb.1.1695277536096.2024884913; privacy_policy_notification=0; a_type=0; _gid=GA1.2.14578990.1701401996; device_token=084cde81a02fcab5e2b7d7549c01efcd; c_type=20; b_type=1; privacy_policy_agreement=0; __cf_bm=O0HyenGRIwYZUHI6Qw3Ojr_1wPL9lGO.hrEXzTOlOhk-1701404016-0-Aeli8Ct4hMtN8Inel4jUa4CGmIerMNRdcYkLidWpVoN5tyGy8L9Bm7XFNre3V2cZnb+rVKm0dfT9ls4RyuHtLfaztWCE/wSDqaY9ldJ9kS/q; PHPSESSID=u29g7thshqjmuniqrvgppolsk3lcq7vu; cc1=2023-12-01%2013%3A20%3A07; _ga_75BBYNYN9J=GS1.1.1701401992.4.1.1701404421.0.0.0; _gat_UA-1830249-3=1; _ga_MZ1NL4PHH0=GS1.1.1701401997.4.1.1701404423.0.0.0; _ga=GA1.1.816218656.1678588557; cf_clearance=A7fhLNkEXZICJkmF1H1J8N5sfQm_qvmruYjlnsP_3aA-1701404421-0-1-4d688f68.55cfc673.1a69d088-0.2.1701404421",
    }
    # 发送HTTP请求获取网页内容
    response = requests.get(url, headers=headers)
    # 设置文本编码
    response.encoding = "UTF-8"
    # 将文本加载为文本形式
    html_content = response.text
    # 使用BeautifulSoup解析网页
    return BeautifulSoup(html_content, "html.parser")
