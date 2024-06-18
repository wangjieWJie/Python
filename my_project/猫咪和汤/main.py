import pyautogui

#判断现在的鼠标位置
p = pyautogui.position()
#获取屏幕分辨率
size = pyautogui.size()

#在每次 PyAutoGUI 调用后设置 2.5 秒的暂停：
pyautogui.PAUSE = 1.5

print("分辨率："+ size + "当前鼠标位置" + p)