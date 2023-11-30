# 一半总厚度：3.60cm
# 一半：32圈
# 厚度:3.6 / 32 = 0.1125cm
# 直径：8.7cm
# 半径：4.35cm

w = 3.6
rad = 32
per_w = 3.6 / 32
d = 8.7
r = 8.7 / 2
pi = 3.1415926535

total_l = 0

for n in range(1, 33):  # 总共三十二圈，循环三十二次
    # 一圈长度
    l = 2 * pi * r
    total_l += l
    # 半径减小
    r -= per_w

print("一卷长度约为：" + str(total_l) + "厘米")
print("换算为厘米为：" + str(total_l / 100) + "米")
