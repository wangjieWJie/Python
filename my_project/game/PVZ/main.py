# 用来退出游戏的模块
import sys

# 用来出创建游戏的函数
import pygame

# 设置的类
from setting import Settings

# 僵尸和植物的属性的类
from PZ import Zombie


def game():
    # 加载、倒入设置,创建类Settings类型的变量
    now_setting = Settings()
    # 创建一个僵尸类型的僵尸
    s_zombie = Zombie

    pygame.init()  # 初始化一个图形窗口
    # 我定义了一个surface，叫做fight_screen，使用display来定义他，后面的 （720，480） 是一个元组，制定了游戏窗口的尺寸
    fight_screen = pygame.display.set_mode(
        (now_setting.fight_screen_width, now_setting.fight_screen_height)
    )
    # 对象fight_screen是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个surface。
    # display.set_mode()返回的surface表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface。

    # 开始循环
    while True:
        # 捕获鼠标或者按键操作
        for event in pygame.event.get():
            # 游戏退出，当点击窗口的关闭按钮时，就触发 pygame.QUIT
            if event.type == pygame.QUIT:
                sys.exit()

        # 设置fight_screen的背景颜色，fill方法一次只能调用一个参数，一种颜色，表示将这个颜色填满屏幕
        fight_screen.fill(now_setting.bg_color)

        # 更新屏幕，让最近绘制的屏幕可见
        pygame.display.flip()


game()
