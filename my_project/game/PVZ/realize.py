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
        elif event.type == pygame.KEYDOWN:
            # pygame.key.get_pressed()来获得所有按下的键值，它会返回一个元组。这个元组的索引就是键值，对应的就是是否按下
            pressed_keys = pygame.key.get_pressed()
            # 向右移动
            if pressed_keys[pygame.K_d]:  # 检测元组的这个索引中是否有值（是否为空）
                guard.moving_sign = "right"
            # 向左移动
            if pressed_keys[pygame.K_a]:
                guard.moving_sign = "left"
            # 向上移动
            if pressed_keys[pygame.K_w]:
                guard.moving_sign = "up"
            # 向下移动
            if pressed_keys[pygame.K_s]:
                guard.moving_sign = "down"
            print(guard.moving_sign)
        # 守卫移动
        guard.moving()
        if event.type == pygame.KEYUP:
            guard.moving_sign = "stop"
