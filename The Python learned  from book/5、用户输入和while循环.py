# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
in_num = input("随便输入一个数字")
in_name = input("请输入你的名字")
print(in_name + "今天的幸运数字是" + in_num)
# 在上面的程序中，即便没加 str() 也能正常输出，这是因为 input 输入进来的一切都是字符串类型

# 为此可以使用类型转换（我认为他是类型转换，但是说上说这个函数能将字符串转换为数值） int()
in_num = int(in_num)
print(6 * in_num)


# while 循环：   包含 break、continue的使用
active = 1
while in_num > 0:
    in_num -= 1
    active = active + 1
    if active >= 24:
        break
    if (
        (in_num % 4) == 0
        or ((in_num / 10 <= 1) and in_num / 10 % 4 <= 1)
        or in_num == 11
    ):
        continue
    print("数一数：" + str(in_num))
