"""
弄个随机数看看明天吃啥
一是炒菜，零是烤肉
"""

import random

print("我们明天要干的事情是。。。。。。。。")

food=random.randint(0,1)

if food==0:
    print("吃烤肉！")
if food==1:
    print("吃炒菜！")
    