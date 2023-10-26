# 这是个用来储存实现游戏各种功能的模块
import pygame

# 用来退出游戏的模块
import sys

# 子弹的类, 以及设置
from setting import Bullet

# 僵尸的类
from PZ import Zombie

# 时间模板
import time


# 更新屏幕
def update_screen(fight_screen, now_setting, zombies, fox, bullets):
    # 设置fight_screen的背景颜色，fill方法一次只能调用一个参数，一种颜色，表示将这个颜色填满屏幕
    fight_screen.fill(now_setting.bg_color)

    # 绘制守卫
    fox.put_guard()
    # 绘制子弹
    for bullet in bullets.sprites():  # 遍历编组中所有的子弹
        bullet.bullet_draw()  # 绘制每个子弹

    # 创建僵尸
    add_zombie(zombies, fight_screen, now_setting)
    # 绘制僵尸
    zombie_coming(zombies)

    # 更新屏幕，让最近绘制的屏幕可见
    pygame.display.flip()


# 接收鼠标和键盘的各种操作的函数
def check_event(guard, bullets, zombies, screen):
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
        test_bullet = Bullet(screen, guard)  # 创建一个子弹类的子弹，以便于使用子弹类中各种参数
        bullet_shoot(event, guard, test_bullet, bullets, screen)


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
def bullet_shoot(event, guard, bullet_text, bullets, screen):
    if event.type == pygame.KEYDOWN:
        if (
            event.key == pygame.K_SPACE
            and len(bullets) <= bullet_text.bullet_num_max  # 限制子弹数量
        ):
            # 创建一个新的 bullet
            bullet_new = Bullet(screen, guard)
            # 将子弹加入到编组bullets中
            bullets.add(bullet_new)
            print("当前子弹数量: " + str(len(bullets)))
            print("当前时间: " + str(time.time()))


# 绘制僵尸
def zombie_coming(zombies):
    for one_zombie in zombies:
        one_zombie.put_zmb()


# 生成僵尸
def add_zombie(zombies, screen, time_setting):  # 设置模块中包含最大僵尸数、上一个僵尸的创建时间、僵尸生成间隔
    if len(zombies) <= time_setting.zombie_max:
        if len(zombies) < 1:  # 僵尸全部死亡时，立即创建一个僵尸，并且创建游戏开始的第一个僵尸
            new_zombei = Zombie(screen)
            zombies.add(new_zombei)
            time_setting.last_zmb_brithday = time.time()  # 储存上一个僵尸的生成时间
        elif (
            len(zombies) >= 1  # 达到时间间隔之后生成僵尸
            and (time.time() - time_setting.last_zmb_brithday) > time_setting.add_sleep
        ):
            new_zombei = Zombie(screen)
            zombies.add(new_zombei)
            time_setting.last_zmb_brithday = time.time()  # 储存僵尸生成的时间
