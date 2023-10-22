# 一个HTML文件中应该只有一个”今日天气“
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
