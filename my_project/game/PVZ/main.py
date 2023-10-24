# 用来出创建游戏的函数
import pygame

# 设置的类
from setting import Settings

# 僵尸和植物的属性的类
from PZ import Zombie, Guard

# 各种游戏功能的实现
from realize import check_event, update_screen


def game():
    # 加载、倒入设置,创建类Settings类型的变量
    now_setting = Settings()

    pygame.init()  # 初始化一个图形窗口
    # 我定义了一个surface，叫做fight_screen，使用display来定义他，后面的 （720，480） 是一个元组，制定了游戏窗口的尺寸
    fight_screen = pygame.display.set_mode(
        (now_setting.fight_screen_width, now_setting.fight_screen_height)
    )
    # 对象fight_screen是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个surface。
    # display.set_mode()返回的surface表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface。

    #
    # 创建一个僵尸类型的普通僵尸
    s_zombie = Zombie(fight_screen)
    # 创建一个守卫类型的狐狸
    fox = Guard(fight_screen)
    #

    #
    # 开始循环
    while True:
        # 捕获鼠标或者按键操作
        check_event(fox)
        # 更新屏幕
        update_screen(fight_screen, now_setting, s_zombie, fox)


game()
