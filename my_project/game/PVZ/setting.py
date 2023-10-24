# 创建一个设置类
# 用于整合所有的设置，和设置的参数
class Settings:
    def __init__(self):
        # 全部设置成私有变量，不准修改，也不需要修改。但是设置上self之后外界也能访问，非常nice
        # 把前面咱们设置好的变量全部转移到这里，方便以后修改
        # 战斗界面的宽和高
        self.fight_screen_width = 720
        self.fight_screen_height = 480
        # 背景颜色，创建背景颜色的变量，储存背景的RGB颜色
        self.bg_color = (230, 230, 230)
