# 用来出创建游戏的函数
import pygame

# 设置的类
from setting import Settings

# 僵尸和植物的属性的类
from PZ import Zombie, Guard

# 各种游戏功能的实现
from realize import check_event, update_screen

# 用于创建各种编组
from pygame.sprite import Group


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
    # 创建一个用于储存子弹的编组
    bullets = Group()
    # 我们将在alien_invasion.py中创建一个编组（group），用于存储所有有效的子弹，以便能够管理发射出去的所有子弹。
    # 这个编组将是pygame.sprite.Group类的一个实例；pygame.sprite.Group类 类似于列表，但提供了有助于开发游戏的额外功能。
    # 创建一个用于储存僵尸的编组
    zombies = Group()
    #

    #
    # 开始循环
    while True:
        # 捕获鼠标或者按键操作
        check_event(fox, bullets, zombies, fight_screen)
        # 更新屏幕
        update_screen(fight_screen, now_setting, zombies, fox, bullets)
        # 检查更新子弹
        update_bullet(bullets, zombies, now_setting)


# 删除看不见了的子弹
def bullet_delete(bullets, now_setting):
    for bullet in bullets.copy():  # 书上使用的是 in bullets.copy() 我没有使用但是好像也可以正常删除没有问题
        if bullet.rect.x > now_setting.fight_screen_width:
            bullets.remove(bullet)


def update_bullet(bullets, zombies, now_setting):
    # 删除已经消失了的子弹
    bullet_delete(bullets, now_setting)
    # 检测子弹和僵尸的碰撞，并删除子弹或者僵尸
    hit = pygame.sprite.groupcollide(bullets, zombies, True, True)
    # sprite提供的groupcollide函数能够检测两个编组中的每个surface是否碰撞，并且返回一个以子弹为键、以僵尸为值的字典
    # 在这个字典中，每个值都是被子弹击中的僵尸
    # 函数最后俩个参数分别代表是否将击中僵尸的bullet和被子弹击中的zombie在他们所在的编组中删除


# 游戏主体
game()
