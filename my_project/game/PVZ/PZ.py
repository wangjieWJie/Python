# 存储rect类的变量他就只能叫rect，不然groupgroupcollide（）函数他就不能用
import pygame
from setting import Settings
from pygame.sprite import Sprite
import random


# 这个模板里面放着的是关于 僵尸和植物的属性的 类
class Zombie(Sprite):
    def __init__(self, screen):
        # 调用super()来继承Sprite
        super(Zombie, self).__init__()

        # 初始化僵尸，并且设置其初始位置
        self.screen = screen  # 指定僵尸应该绘制到的地方

        # 基准移速
        self.zmb_speed_basic = 0.005  # 0.005 的速度还是可以的
        # 僵尸的移速
        self.zmb_speed = 0.005
        # 基准血量
        self.zmb_blood_basic = 100
        # 僵尸血量
        self.zmb_blood = 100
        # 死亡证明
        self.killed_judge = False

        # 加载僵尸图像并获取其外接矩形
        setting_adr = Settings()
        self.img_head = pygame.image.load(
            setting_adr.file_adr + "file/simple_zmb/head.PNG"
        )
        # image.load() 函数返回一个表示飞船的surface
        self.rect = self.img_head.get_rect()  # 获取僵尸的位置    ，get_rect() 是 pygame 中的一个类
        self.screen_rect = screen.get_rect()  # 获取屏幕的位置
        # 加载图像后，我们使用get_rect()获取相应surface的属性rect。
        # Pygame的效率之所以如此高，一个原因是它让你能够像处理矩形（rect对象）一样处理游戏元素，即便它们的形状并非矩形。
        # 像处理矩形一样处理游戏元素之所以高效，是因为矩形是简单的几何形状。
        # 这种做法的效果通常很好，游戏玩家几乎注意不到我们处理的不是游戏元素的实际形状。
        # 处理rect对象时，可使用矩形四角和中心的x和y坐标。可通过设置这些值来指定矩形的位置。
        # 要将游戏元素居中，可设置相应rect对象的属性center、centerx或centery。
        # 要让游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right；
        # 要调整游戏元素的水平或垂直位置，可使用属性x和y，它们分别是相应矩形左上角的x和y坐标。

        # 生成僵尸的随机数
        rand_adr = random.randint(
            -(setting_adr.fight_screen_height - 100) / 2,
            (setting_adr.fight_screen_height - 100) / 2,
        )

        # 将僵尸随机放置到最右边的一个位置，以中心线为基准，上下随机，但是排除最上面和最下面
        self.rect.centery = self.screen_rect.centery + rand_adr
        # 表示僵尸图像的纵向的中心点的y坐标 等于 屏幕的纵向的中心点的y坐标
        self.rect.right = self.screen_rect.right  # + 50  # 使其出生在屏幕之外
        # 表示 僵尸右边缘的x坐标 等于 屏幕的最右边缘的x坐标

        # 设置储存位置的float类型变量
        self.zmb_x = float(self.rect.right)

    # 在指定位置绘制僵尸，同时移动
    def put_zmb(self):
        self.zmb_moving()
        self.screen.blit(self.img_head, self.rect)
        # 根据 rect 指定的位置放置图片

    # 僵尸的移动
    def zmb_moving(self):
        self.zmb_x -= self.zmb_speed
        self.rect.right = self.zmb_x


class Guard:
    def __init__(self, screen):
        self.screen = screen  # 指定守卫应该绘制到的地方

        # 多余路径
        setting_adr = Settings()
        self.img_guard = pygame.image.load(
            setting_adr.file_adr + "file/guard/fox/fox.png"
        )

        # 获取守卫和屏幕的位置表示,返回一个类
        # 只能获取或储存整数，所以要把它转换为float类型(新建一个变量 guard_center、guard_left)
        self.rect = self.img_guard.get_rect()
        self.screen_rect = screen.get_rect()

        # 定位起始位置
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + 50

        # 使其能添加小数,桥梁
        self.guard_centery = float(self.rect.centery)
        self.guard_left = float(self.rect.left)

        # 守卫是否应该移动的标志 sign
        # 之前我只设置了一个字符串变量作为标志，但是一次只能响应一个按键，所以没法急停和斜着走
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        #  守卫的移动速度
        self.guard_speed = 10
        # 守卫血量
        self.guard_blood = 100

    # 在指定位置绘制守卫
    def put_guard(self):
        self.screen.blit(self.img_guard, self.rect)
        # 根据 rect 指定的位置放置图片

    # 守卫的移动
    def moving(self):
        # 向右移动                         # 全都使用 if 而是不 elif。防止同时按下两个按键时只能响应一个按键
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.guard_left += self.guard_speed
        # 向左移动
        if self.moving_left and self.guard_left >= self.screen_rect.left:  # 或者写大于零
            self.guard_left -= self.guard_speed
        # 向上移动
        if self.moving_up and self.rect.top >= self.screen_rect.top:  # 或者写大于0
            self.guard_centery -= self.guard_speed
        # 向下移动
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.guard_centery += self.guard_speed

        # 更新gurad_rect以改变图片位置
        self.rect.centery = self.guard_centery
        self.rect.left = self.guard_left
