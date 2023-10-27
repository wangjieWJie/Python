# 创建一个设置类
# 用于整合所有的设置，和设置的参数

from pygame.sprite import Sprite
import pygame


class Settings:
    def __init__(self):
        # 全部设置成私有变量，不准修改，也不需要修改。但是设置上self之后外界也能访问，非常nice
        # 把前面咱们设置好的变量全部转移到这里，方便以后修改
        # 战斗界面的宽和高
        self.fight_screen_width = 720
        self.fight_screen_height = 480
        # 背景颜色，创建背景颜色的变量，储存背景的RGB颜色
        self.bg_color = (230, 230, 230)
        # 因为我这个文件大环境是Python这个文件夹，所以python和PVZ之间的文件路径都要加上
        self.file_adr = "my_project/game/PVZ/"
        # 最大将僵尸数
        self.zombie_max = 10
        # 僵尸的生成间隔(单位:秒)
        self.add_sleep = 8
        # 第一只僵尸的出生日期
        self.last_zmb_brithday = 0
        # 子弹伤害
        self.bullet_ATK = 20
        # 僵尸伤害
        self.zombie_ATK = 50
        # 守卫无敌时间,伤害免疫
        self.injury_immunity = 3

        # 记录第一只僵尸的出生日期

    def set_zmb_brithday(self, time):
        self.last_zmb_time = time


# 设置子弹
class Bullet(Sprite):
    def __init__(self, screen, guard):
        # 通过使用sprite，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
        # 为创建子弹实例，需要向__init__()传递screen和guard实例，还调用了super()来继承Sprite。
        super(Bullet, self).__init__()  # 可简写：把super后面括号里的参数删除
        self.screen = screen

        # 设置子弹的宽和高
        self.bullet_width = 15
        self.bullet_height = 5
        # 设置子弹的速度
        self.bullet_speed = 0.25
        # 设置子弹颜色
        self.bullet_color = 60, 60, 60
        # 限制子弹数量
        self.bullet_num_max = 1  # 最大子弹数量为此值加一
        # 子弹伤害
        self.buttet_ATK = 50

        # 在(0,0)处创建一个表示子弹的矩形，Rect 函数表示子弹的属性,(0,0)是子弹左上角的坐标
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        # 设置发射位置
        self.rect.centery = guard.rect.centery
        self.rect.right = guard.rect.right

        # 因为子弹应该是向右直线发射的，所以只需要改变子弹的 x 坐标即可
        # 储存用小数表示的子弹位置：
        self.bullet_x = float(self.rect.x)

    # 让子弹自己移动
    def bullet_moving(self):
        # 改变x坐标
        self.bullet_x += self.bullet_speed
        # 更新子弹的x坐标
        self.rect.x = self.bullet_x

    # 在屏幕上绘制子弹：
    def bullet_draw(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
        #                  surface         颜色                  位置
        # 函数draw.rect()使用存储在self.color中的颜色填充表示子弹的rect占据的屏幕部分
        # 顺便让他动起来吧
        self.bullet_moving()
