# 这是个用来储存实现游戏各种功能的模块
import pygame

# 用来退出游戏的模块
import sys

# 子弹的类
from setting import Bullet


# 更新屏幕
def update_screen(fight_screen, now_setting, s_zombie, fox, bullets):
    # 设置fight_screen的背景颜色，fill方法一次只能调用一个参数，一种颜色，表示将这个颜色填满屏幕
    fight_screen.fill(now_setting.bg_color)

    # 使用我们定义的函数绘制僵尸
    s_zombie.put_zmb()
    # 绘制守卫
    fox.put_guard()
    # 绘制子弹
    for bullet in bullets.sprites():  # 遍历编组中所有的子弹
        bullet.bullet_draw()  # 绘制每个子弹

    # 更新屏幕，让最近绘制的屏幕可见
    pygame.display.flip()


# 接收鼠标和键盘的各种操作的函数
def check_event(guard, bullets, screen):
    # 相应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # 移动守卫的条件
        guard_moving(event, guard)
        # 按键抬起时停止移动的条件
        guard_stop(event, guard)

        # 守卫移动
        guard.moving()

        # 创建子弹
        bullet_shoot(event, guard, bullets, screen)


# 移动守卫的条件
def guard_moving(event, guard):
    if event.type == pygame.KEYDOWN:
        # 向右移动
        if event.key == pygame.K_d:
            guard.moving_right = True
            print("右kick")
        # 向左移动
        if event.key == pygame.K_a:
            guard.moving_left = True  #  全都使用 if 而是不 elif。防止同时按下两个按键时只能响应一个按键
            print("左kick")
        # 向上移动
        if event.key == pygame.K_w:
            guard.moving_up = True
            print("上kick")

        # 向下移动
        if event.key == pygame.K_s:
            guard.moving_down = True
            print("下kick")


# 按键抬起时停止移动的条件
def guard_stop(event, guard):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            guard.moving_right = False
            print("右up")
        elif event.key == pygame.K_a:
            guard.moving_left = False  # 不需要全部使用if，因为两个按键不可能同时松开，即同时处于松开的状态
            print("左up")
        elif event.key == pygame.K_w:  # 因为他们是两个不同的事件
            guard.moving_up = False
            print("上up")
        elif event.key == pygame.K_s:
            guard.moving_down = False
            print("下up")


# 创建子弹
def bullet_shoot(event, guard, bullets, screen):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # 创建一个新的 bullet
            bullet_new = Bullet(screen, guard)
            # 将子弹加入到编组bullets中
            bullets.add(bullet_new)
