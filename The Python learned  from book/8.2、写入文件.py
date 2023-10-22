# 调用 open 时我们可以给他多个参数
# open(filename,'r')   其中的
# W :写入模式 （会覆写已经存在的文件）
# r : 只读
# a : 附加模式
# r+ : 读写模式
# 当你省略实参的时候，默认为只读模式
# 注意： 当你使用 open 而找不到指定文件的时候，open会自动帮您创建一个新的文件
# 但是但是，和C一样，当你使用了实参 w 之后，他会覆写你指定的文件（如果存在）

# python 只能写入字符串，如果有其他数字，则应使用 str 进行转化

filename = "file/i will write in.txt"
with open(filename, "w") as file_write:
    file_write.write(
        "这就是我想要写入的东西\n而且我不知道写点什么\n就像我满心欢喜面对无言的你\n是的，你可以认为这是一首诗\n一首不顾格调的诗\n"
    )
    file_write.write(
        "This is what i want to write in\nAnd i don't know what to write\n"
        + "Just like me full of joy face you with silence\n"
        + "You may think this is  a poem\nA poem that have no rhyme\n"
    )


# 附加模式：
# 当你要给文件添加内容而不是覆写他的时候，可以使用附加模式，但是当原文件不存在时，可以为你创建一个新文件


# 下面是一个附加操作，但是我设计的让他每次附加的时候都会标记一个递增的数字

count = 0  # 计数器，储存这次应该写入的次数编码
FM_r_a = "file/a、add.txt"  # 这次操作的文件名
with open(FM_r_a, "a") as none:  # 随便打开一下，主要是为了创建我想要的文件，创建完他就一点作用都没有了
    1 + 1

with open(FM_r_a, "r") as FM_r:  # 用只读的模式打开这个文件，因为我不知道附加模式能不能读取
    for line_r in FM_r:  # 一行行的读取文件，看看里面有没有单行的数字
        #  Python的  isdigit() 方法检测字符串是否只由数字组成。返回True or False
        if (
            line_r.rstrip().isdigit()
        ):  # 检测是不是单行的数字，这里 .rstrip() 的作用是剥除行末的换行符，因为只要有换行符存在，他就检测不出单行的数字来
            # 好神奇，原来 if 后面可以跟括号和回车
            print(line_r)  # 不放心，把编号打印出来看看
            count = int(line_r) + 1  # 在上一次的基础上加一

with open(FM_r_a, "a") as FM_a:  # 开始附加写入
    FM_a.write(
        str(count) + "\n你每次运行一次这个代码，他都会将这行数字输入一遍" + "\n但是区别是我上面会有一个计数，你每次运行他都会增长，厉不厉害\n"
    )  # 先写编号，回车之后在写文本，写完文本记得回车，否则下次的编号就会写在这次文本的最后一行的末尾，妨碍检测

    # 丑中不足：
    # 只能显示运行了多少次这个代码，但如果我想自己手动写点东西他就不知道
    # 编码不是 UTF-8 显示的全是乱码
    # 只能检测单行的数字，行内的数字可以这么检测：
    # 使用 for 循环一个字一个字的检测，当发现一个数字后，检查下一个字符是不是数字或者是不是“ 、 ”（我自己想的特殊标志）
    # 如果是数字，那么继续检测，如果是顿号，那么表示这是我设置的一个编号，应该记住他，如果后面不是数字也不是顿号，那就别管他
