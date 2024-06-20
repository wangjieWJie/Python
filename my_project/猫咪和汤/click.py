import pyautogui
import cv2
import time

# #判断现在的鼠标位置
# p = pyautogui.position()
# #获取屏幕分辨率
# size = pyautogui.size()

# #在每次 PyAutoGUI 调用后设置 0.3 秒的暂停：
# pyautogui.PAUSE = 0.3


# print(type(size))
# print("分辨率：" )
# print( size )
# print(  "当前鼠标位置" )
# print( p )

        #截取屏幕
        # screen = pyautogui.screenshot()
        # screen.save("file/cat&soup/screen.png")
        #pyautogui.screenshot("file/cat&soup/screen.png")

class Setting:
    def __init__(self) -> None:
        #设置窗口位置
        head = cv2.imread("file/cat&soup/head.png")
        locat_head = pyautogui.locateOnScreen(head, confidence=0.43)
        self.loca_head = locat_head

        #宽长比
        self.rate = 0.5374
        #窗口四坐标,left, top, right, bottom, width, height
        self.loca_win = {"left" : self.loca_head.left, 
                         "top"  : self.loca_head.top, 
                         "right" : self.loca_head.left + self.loca_head.width, 
                         "bottom" : self.loca_head.top + int(self.loca_head.width / self.rate),
                         "width" : self.loca_head.width,
                         "height" : int(self.loca_head.width / self.rate) }
        #升级按钮  X坐标位于窗口坐标1/10处，Y坐标位于窗口0.8333处
        self.grade_up = {"x" : int(self.loca_win["left"] + 0.1*self.loca_win["width"]),
                          "y" : int(self.loca_win["top"] + 0.833*self.loca_win["height"]) }
        #食物盘子  x坐标位于x轴的0.0795处
        self.food = {"x" : int(self.loca_win["left"] + 0.0795*self.loca_win["width"]),
                     "y" : self.loca_win["top"] + self.loca_win["height"] - 25 } 
        #升级时间戳
        self.time_grade = 0 



    #更新窗口位置
    def update_win(self):
        #更新标题头位置
        head = cv2.imread("file/cat&soup/head.png")
        self.loca_head = pyautogui.locateOnScreen(head, confidence=0.43)

        #更新窗口四坐标
        self.loca_win = {"left" : self.loca_head.left, 
                         "top"  : self.loca_head.top, 
                         "right" : self.loca_head.left + self.loca_head.width, 
                         "bottom" : self.loca_head.top + int(self.loca_head.width / self.rate),
                         "width" : self.loca_head.width,
                         "height" : int(self.loca_head.width / self.rate)}
        #更新升级按钮
        self.grade_up = {"x" : int(self.loca_win["left"] + 0.1*self.loca_win["width"]),
                          "y" : int(self.loca_win["top"] + 0.86*self.loca_win["height"]) } 
        #更新食物盘子
        self.food = {"x" : int(self.loca_win["left"] + 0.0795*self.loca_win["width"]),
                     "y" : self.loca_win["top"] + self.loca_win["height"] -25 } 


        print(self.loca_head)
         
             












#点击食物
def click_food(St):
    
    #移动并点击food
    pyautogui.moveTo(St.food["x"], St.food["y"])
    pyautogui.click(clicks=1,button= "left",duration=0)

    pyautogui.PAUSE = 1.5
    print("卖菜中")



#升级食物
def grade_up(St):
    if time.time()-St.time_grade > 12:
        #隔段时间就升级
        pyautogui.moveTo(St.grade_up["x"], St.grade_up["y"])
        pyautogui.click(clicks=1,button= "left",duration=0)
        #更新时间戳
        St.time_grade = time.time()
        print("升级中...\n")
   





