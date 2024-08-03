import numpy   # 引入numpy库，目的是将读取的数据转换为列表
import pandas  # 引入pandas库，用来读取csv数据
from uiautomation import WindowControl  # 引入uiautomation库中的WindowControl类，用来进行图像识别和模拟操作

# 文件目录
path = "my_project/"

# 定义微信窗口控件
wx = WindowControl(Name = "微信")  # ,searchDepth = 1)
#print("微信已绑定： " + str(wx))

# 切换窗口到微信——显示微信窗口
wx.SwitchToThisWindow()

# 寻找会话控件并绑定——微信的会话控件就是左边的会话列表那一个区域
session_list = wx.ListControl(Name = "会话")

# 通过 pandas 读取 scv 文件中的自动回复语句
words = pandas.read_csv(path + '微信自动回复/AutoWords.csv', encoding='GBK')
print(words)

while True:
    # 分离出消息列表中的前四深度，用于在里面查找未读信息
    red_point = session_list.TextControl(searchDepth = 4)  # searchDepth 搜索深度，表示最深会搜索到哪里，例如： 会话/好友名称/窗格/1 文本

    # 死循环维持，没有超时报错
    while not red_point.Exists():
        pass


    # 如果红点存在
    if red_point.Name:
        # 点击进入会话
        red_point.Click(simulateMove = False)   # simulateMove: 模拟移动，模拟鼠标移动过去的轨迹
        #读取最后两条消息
        last_msg = wx.ListControl(Name = '消息').GetChildren()[-1].Name
        print(last_msg)

        # 根据关键词判断需要返回的信息
        msg = words.apply(lambda x: x['回复内容'] if x['关键词'] in last_msg else None, axis=1)
        # apply方法将后面的运算遍历地运算到列表中，其中axis若为1，则表示处理每一行，若为0则表示处理每一列，运算完成后返回结果到等号前的变量中
        # lambda（匿名函数）表达式：有一个参数x进入函数，这个x就是前面的words，x['回复内容']表示返回回复内容这一列，但只有 “关键词” 这一列中有人家发的消息时才执行， 否则返回 None
        # 上面就是匿名函数中 使用if语句的方法，请牢记，就是把if后面的执行内容提前了而已，执行语句前置
        # 那么上式总起来就表示，遍历每一行的关键词，如果相符合就返回回复内容，否则返回None，最终返回到msg中的是一个DataFrame（数组）

        #删除消息中的空值    dropna 能够找到DataFrame类型数据的空值（缺失值），将空值所在的行/列删除后，将新的DataFrame作为返回值返回
        msg.dropna(axis=0, how='any', inplace=True)
        # axis为0表示按行删除， any 表示只要一行有一个空值就删除这一行，  inplace表示是否原地替换，如果为True，则在原DataFrame上进行操作，返回值为None。

        # 将DataFrame类型转换为数组类型
        send = numpy.array(msg).tolist()
        # array将 msg 转换为 NumPy数组，tolist将 NumPy数组 转化为列表\

        # 如果成功匹配到了话术
        if send:
            print(send)
            # 输入内容到聊天框
            # 替换换行符号，防止在输入完成后立即发送，{Shift}{Enter}可以在不发送的情况下回车
            wx.SendKeys(send[0].replace('{br}', '{Shift}{Enter}'), waitTime=1)
            # 发送消息 回车键
            wx.SendKeys('{Enter}', waitTime=1)

            # 通过消息匹配检索会话栏的联系人并右键点击他，以便于他发送的下一条消息可以被识别
            wx.TextControl(SubName=send[0][:5]).RightClick()

        # 如果没能匹配到话术
        else:
            wx.SendKeys('没带手机，一会回你', waitTime=1)
            wx.SendKeys('{Enter}', waitTime=1)

            # 通过消息匹配检索会话栏的联系人并右键点击他，以便于他发送的下一条消息可以被识别
            wx.TextControl(SubName=last_msg[:5]).RightClick()
