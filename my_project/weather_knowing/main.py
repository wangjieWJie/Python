# 一个HTML文件中应该只有一个”当前天气“
# 今日天气后面第一个数字就是当前时间
# 所有的有用信息全都在两个尖括号中间  >17<
# 看到了不同的天气  后面的第一个°C 之前的数字是体感温度，后面第二个°C之前的数字是体感温度
# 体感温度后面是个表格（table），<table>之后的<div>中的文本就是对今天 天气最高温的描述：  ”今天大部分地区天气晴朗。 最高气温24°。“

# <div class="temp-DS-EntryPoint1-1 tempSelected-DS-EntryPoint1-1">16°</div>
# 上边是今日最低气温的标签，理论上这些 选择器（CSS style）应该不会随便修改，所以直接索检标签可能对于大部分的信息很有效果
# temp-DS-EntryPoint1-1 tempSelected-DS-EntryPoint1-1
# 这两个选择器 只有最高温和最低温 使用，比较一下大小就能确定一天的气温 ，棒

# topTemp-DS-EntryPoint1-1 temp-DS-EntryPoint1-1
# 这是未来十天的天气预测的气温的最高温的标签选择器

import re
import time

mark_time = '"labelUpdatetime-DS-EntryPoint1-1"'
that_time = ""


html = "山东省, 济南市, 槐荫区 天气预报 _ Microsoft 天气.html"
may_addrass = re.split("[, \.]+", html)
# 地址信息储存
addrass = []
print(may_addrass)

# 记录当前时间
now_time = time.localtime()
print(now_time)

# 创建一个字典用于储存地址、日期和天气信息
the_weather = {}

# 写入地址信息
for tmp_adr in may_addrass:
    if "省" in tmp_adr:
        addrass.append(tmp_adr)
    elif "市" in tmp_adr:
        addrass.append(tmp_adr)
    elif ("区" or "县") in tmp_adr:
        addrass.append(tmp_adr)
print(addrass)

# 文件储存位置
file = "my_project/weather_knowing/file/" + html
# 打开并读取文件
with open(file, "r") as html_file:
    html_constents = html_file.read()
    # 逐行读取
    for tmp_consts in html_constents:
        # 如果有关于当前时间的选择器则用正则表达式（所有数字或者是冒号，匹配一个以上）将时间匹配出来
        if mark_time in tmp_consts:
            that_time = re.match("[0-9|:]+", tmp_consts)
            print(that_time)


# 好像是因为文件字数太长了，read 不下来，应该分节输入
