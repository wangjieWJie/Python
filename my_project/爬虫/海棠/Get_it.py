from bs4 import BeautifulSoup
import requests


# 解析网页
def return_web(ht, url):
    # 设置params参数
    # 设置headers参数
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }
    # 发送HTTP请求获取网页内容
    response = requests.get(url, headers=headers)

    # 判断链接是否有效
    if response.status_code != 200:
        ht.url_ok = False
        print(url + "有大问题，打不开呀！")

    # 设置文本编码
    response.encoding = "UTF-8"
    # 将文本加载为文本形式
    html_content = response.text
    # 使用BeautifulSoup解析网页
    return BeautifulSoup(html_content, "html.parser")


# 寻找所有的小说详情页链接
def find_more(rank_web, ht):
    # 寻找所有的<a>标签
    tag_a = rank_web.find_all(attrs={"class": "r"})
    for one_a in tag_a:
        ht.more_link.append(one_a.get("href"))
        print("加载网址中……")


# 解析所有详情页链接并储存小说第一章链接
def find_novel(ht):
    for noe_more in ht.more_link:
        # 解析每个详情页：
        more_web = return_web(ht, noe_more)
        # 寻找小说
        tag_li = more_web.find_all(attrs={"class": "CGsectionOne-active"})
        for li in tag_li:
            # ht.novel_frist.append(li.find_all("a").get("href"))
            for a in li.find_all("a"):
                # 储存每个小说的第一章链接
                ht.novel_frist.append(a.get("href"))
        # 设置最大保存小说数
        ht.now_save += 1
        if ht.now_save > ht.max_save:
            ht.now_save = 1
            break


# 解析小说页面并返回所有自然段的标签
def get_novel(ht, N_url):
    novel_web = return_web(ht, N_url)
    # 查找标题
    chapterTitle = novel_web.find_all("h1", attrs={"id": "chapterTitle"})
    # 记录这一章小说有多少页，并且现在爬到了多少页
    for title in chapterTitle:
        # 这里偷懒了，赌一把，赌他没有超过十页的小说
        ht.total_page = int(title.text[-2])
        ht.now_page = int(title.text[-4])
        print("总共" + str(title.text[-2]) + "章，当前为第" + str(title.text[-4]) + "章")

    #  返回自然段标签
    return novel_web.find_all(
        "p",
        attrs={
            "style": "text-indent: 2em; padding: 0px; margin: 0px; font-size: 14px;"
        },
    )


# 将所有标签中的内容存储到列表中
def tmp_save(tag_p):
    # 临时储存文本的列表
    text_tmp = []
    for p in tag_p:
        # 保存一个自然段
        text_tmp.append(p.text + "\n")
    return text_tmp


# 将文本保存到txt文件
def save_txt(filename, save_path, text_list):
    pass


# 开始下载小说
def download(ht):
    # 保存所有小说
    for one_novel in ht.novel_frist:
        print("正在保存第" + str(ht.now_save) + "篇小说")
        # 保存所有章节
        while True:
            print("保存第" + str(ht.chapter) + "章")
            # 保存第一页到列表中 ：
            print("第1页/总共" + str(ht.total_page) + "章")
            text_tmp = tmp_save(get_novel(ht, one_novel))
            # 保存后面的页
            while True:
                print("第" + str(ht.now_page) + "页")
                page_url = (
                    ht.novel_frist[ht.now_save][:-6]
                    + "_"
                    + str(ht.now_page)
                    + ht.novel_frist[ht.now_save][-5:]
                )

                print(page_url)
                #  存储并储存一整章节
                ht.all_novel.append(text_tmp.append(tmp_save(get_novel(ht, page_url))))
                # 结束一章的爬取，准备下一章
                if ht.now_page == ht.total_page:
                    ht.now_page = 0
                    ht.total_page = 0
                    print(ht.all_novel)
                    break
            # 下一章
            ht.chapter += 1
        # 下一篇小说
        ht.now_save += 1
    # 恢复默认设置
    ht.chapter = 1
    ht.now_page = 1
    ht.now_save = 1
