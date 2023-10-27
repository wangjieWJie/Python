# 用来出创建游戏的函数
import pygame

# 设置的类
from setting import Settings, Button, Achievement, See_Achievement

# 僵尸和植物的属性的类
from PZ import Zombie, Guard

# 各种游戏功能的实现
from realize import (
    check_event,
    update_screen,
    add_zombie,
    wait_play,
    bullet_delete,
    hit_zombies,
    update_guard_blood,
    kill_you,
    harder,
)

# 用于创建各种编组
from pygame.sprite import Group

# 时间函数
import time


def game():
    # 创建记分器
    achievement = Achievement()
    while True:
        # 加载、倒入设置,创建类Settings类型的变量
        now_setting = Settings()

        pygame.init()  # 初始化一个图形窗口
        # 我定义了一个surface，叫做fight_screen，使用display来定义他，后面的 （720，480） 是一个元组，制定了游戏窗口的尺寸
        fight_screen = pygame.display.set_mode(
            (now_setting.fight_screen_width, now_setting.fight_screen_height)
        )
        # 对象fight_screen是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个surface。
        # display.set_mode()返回的surface表示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface。

        # 重置计分
        achievement.reset_score()
        # 创建计分展示
        see_achievement = See_Achievement(fight_screen, now_setting, achievement)

        # 创建play按钮：
        play_button = Button(now_setting, fight_screen, "Play")
        #
        # 创建一个守卫类型的狐狸
        fox = Guard(fight_screen)
        # 创建一个用于储存子弹的编组
        bullets = Group()
        # 我们将在alien_invasion.py中创建一个编组（group），用于存储所有有效的子弹，以便能够管理发射出去的所有子弹。
        # 这个编组将是pygame.sprite.Group类的一个实例；pygame.sprite.Group类 类似于列表，但提供了有助于开发游戏的额外功能。
        # 创建一个用于储存僵尸的编组
        zombies = Group()
        while True:
            # 开始游戏
            if now_setting.if_game:
                start_game(
                    fight_screen,
                    now_setting,
                    zombies,
                    fox,
                    bullets,
                    achievement,
                    see_achievement,
                )
                break
            # 等待游戏开始
            if now_setting.if_game == False:
                wait_play(now_setting, fight_screen, play_button)


# 开始游戏
def start_game(
    fight_screen,
    now_setting,
    zombies,
    fox,
    bullets,
    achievement,
    see_achievement,
):
    while True:
        # 如果游戏开始
        # 捕获鼠标或者按键操作
        check_event(fox, bullets, zombies, fight_screen)
        # 生成僵尸
        add_zombie(zombies, fight_screen, now_setting, achievement)
        # 检查更新子弹
        update_bullet(
            fight_screen, bullets, zombies, now_setting, achievement, see_achievement
        )
        # 结束游戏
        over_game(now_setting, zombies, fox, bullets)
        # 更新屏幕
        update_screen(
            fight_screen,
            now_setting,
            zombies,
            fox,
            bullets,
            achievement,
            see_achievement,
        )
        # 如果游戏未开始或者结束
        if now_setting.if_game == False:
            break


def update_bullet(screen, bullets, zombies, now_setting, achievement, see_achievement):
    # 删除已经消失了的子弹
    bullet_delete(bullets, now_setting)
    # 扣除僵尸血量并杀死他们
    hit_zombies(screen, bullets, zombies, now_setting, achievement, see_achievement)


# 结束游戏
def over_game(now_setting, zombies, fox, bullets):
    # 更新守卫血量
    update_guard_blood(now_setting, zombies, fox)
    # 检测僵尸是否入侵
    kill_you(now_setting, zombies)


# 游戏主体
game()
