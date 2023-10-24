# 这是个用来储存实现游戏各种功能的模块

import pygame

# 用来退出游戏的模块
import sys


# 更新屏幕
def update_screen(fight_screen, now_setting, s_zombie, fox):
    # 设置fight_screen的背景颜色，fill方法一次只能调用一个参数，一种颜色，表示将这个颜色填满屏幕
    fight_screen.fill(now_setting.bg_color)

    # 使用我们定义的函数绘制僵尸
    s_zombie.put_zmb()
    # 绘制守卫
    fox.put_guard()

    # 更新屏幕，让最近绘制的屏幕可见
    pygame.display.flip()


# 接收鼠标和键盘的各种操作的函数
def check_event(guard):
    # 相应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 移动守卫
        guard.moving(event)
