from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from Pixiv_set import Pixiv
from get_it import find_more, find_img, return_web

# 创建Pixiv设置类
pix = Pixiv()

# 解析网页
month_web = return_web(pix.url_monthly)

# 加载图片详情页地址
find_more(month_web, pix)

# 加载图片原图地址
find_img(pix)
