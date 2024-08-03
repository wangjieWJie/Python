import numpy   # 引入numpy库，目的是将读取的数据转换为列表
import pandas  # 引入pandas库，用来读取csv数据
from uiautomation import WindowControl  # 引入uiautomation库中的WindowControl类，用来进行图像识别和模拟操作
#我的函数文件AiFunction
import AiFunction

# 文件目录
path = "my_project/"
# 用于AI问答的类
qw_tb = AiFunction.ChatGpt()

# 定义微信窗口控件
wx = WindowControl(Name = "微信")  # ,searchDepth = 1)

# 切换窗口到微信——显示微信窗口
wx.SwitchToThisWindow()

# 寻找会话控件并绑定——微信的会话控件就是左边的会话列表那一个区域
session_list = wx.ListControl(Name = "会话")

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
        #读取最后一条消息
        last_msg = wx.ListControl(Name = '消息').GetChildren()[-1].Name
        print(last_msg)

        # 由Ai生成回复
        send = qw_tb.chat_qwen_turbo(last_msg)

        if send:
            print(send)
            # 输入内容到聊天框
            # 替换换行符号，防止在输入完成后立即发送，{Shift}{Enter}可以在不发送的情况下回车
            wx.SendKeys(send[0:-1].replace('{br}', '{Shift}{Enter}'), waitTime=1)
            # 发送消息 回车键
            wx.SendKeys('{Enter}', waitTime=1)

            # 通过消息匹配检索会话栏的联系人并右键点击他，以便于他发送的下一条消息可以被识别
            wx.TextControl(SubName=send[0][:5]).RightClick()

        # 如果没能匹配到话术
        else:
            wx.SendKeys('这边出了点问题，回不了消息了', waitTime=1)
            wx.SendKeys('{Enter}', waitTime=1)

            # 通过消息匹配检索会话栏的联系人并右键点击他，以便于他发送的下一条消息可以被识别
            wx.TextControl(SubName=last_msg[:5]).RightClick()
