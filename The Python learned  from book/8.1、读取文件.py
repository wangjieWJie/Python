little_pi = open("file/pi(6838).txt")
# open("文件") 函数用于接受一个文件并且将这个文件返回为一个对象储存在前面的变量中（并且还会把这个文件缓存起来）
# 方法 close() 可以用于关闭文件
little_pi.close()
# 但是使用open、close 会因为 bug 导致close未运行或者close运行太早导致文件早已关闭而产生问题
# 所以我们一般使用以下方法打开文件

with open("file/pi(68).txt") as little_pi:
    pi_contents = little_pi.read()
    print("将读取的文件中的内容全部打印出来：\n" + pi_contents)

    # with ··· as ··· 表示将文件返回的对象储存在后面的变量中
    # 关键字 with 在不再需要访问文件后将其关闭。
    # 方法 read 读取这个文件的全部内容，并将其作为一个长长的字符串存储在变量 contents 中。
    # 这样，通过打印contents的值，就可将这个文本文件的全部内容显示出来
    # 书上说 read 读取到文件末尾时会返回一个空字符串，这个空字符串打印出来就是一个空行
    # 为解决这个问题，我们将会使用之前学过的方法： .rstrip()
    #  print(pi_contents.rstrip())          # 打印出来太长了，况其我这也没有空白行，就不打印了
    # 他可以删除（剥除）字符串末尾的空白

    # 逐行读取
    # 使用for循环读取时，自动按照 行 为单位进行读取
print("使用 for 循环按行打印:")
with open("file/pi(68).txt") as little_pi:
    for pi_line in little_pi:
        print(pi_line)
        # 像这样，将 文本一行一行写入 pi_line，然后在使用 print 打印出来
        # 这里就出现了之前以为他会出的情况：文本最后出现了空字符串，然后就导致他每行直接有个空行

        # 使用预备好的解决方案：
    print("删除空行之后的pi_line:")
with open("file/pi(68).txt") as little_pi:
    for pi_line in little_pi:
        print(pi_line.rstrip())


# 使用文件
# 一般我们都是把文件中的内容存储到一个列表中以方便读取，而且即便文件关闭我们任然能够读取文件
# 我们可以使用循环将文件分行储存为列表的一个个元素
# 记得储存的时候要使用 .rstrip() 删除字符串末尾的换行符
pi_list = []
with open("file/pi(68).txt") as little_pi:
    for pi_line in little_pi:
        pi_list.append(pi_line.rstrip())
    print("列表的最后一个元素是:" + pi_list[-1])


# 但是书上给的例子是把文字储存在一个字符串中
# 书上说字符串可以储存几百万个文字
# 那我们就根据书上的例子把pi的前68位小数存进一个字符串中并且计算这串数字中的字符个数
pi_string = ""
with open("file/pi(68).txt") as little_pi:
    for pi_line in little_pi:
        pi_string += pi_line.rstrip()
    print("这个pi中一共有 " + str(len(pi_string)) + "个数字!")
    # 当然,我这个文件有点傻逼,从第二行开始我给每行开头加了两个空格(为了好看,但是不实用)
