# 引入selenium库中的 webdriver 模块
from selenium import webdriver

# 引入time库
import time

# 打开谷歌浏览器
driver = webdriver.Chrome()
# 打开智慧树学习平台
driver.get("https://www.zhihuishu.com/")
"""
考虑到网页打开的速度取决于每个人的电脑和网速，
使用time库sleep()方法，让程序睡眠5秒
"""
time.sleep(5)
# 在主页面点击登录按钮，进入登录页面
driver.find_element_by_xpath('//*[@id="notLogin"]/span/a[1]').click()
# 输入账号和密码
driver.find_element_by_xpath('//*[@id="lUsername"]').send_keys("账号")
driver.find_element_by_xpath('//*[@id="lPassword"]').send_keys("密码")
# 点击登录按钮
driver.find_element_by_xpath('//*[@id="f_sign_up"]/div[1]/span').click()

#

#
# ————————————————
# 版权声明：本文为CSDN博主「shiaohan」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/shiaohan/article/details/108834770
