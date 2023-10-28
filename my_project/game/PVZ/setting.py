# 创建一个设置类
# 用于整合所有的设置，和设置的参数

from pygame.sprite import Sprite
import pygame
import pygame.font


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
        # 最大僵尸数
        self.zombie_max = 5
        # 僵尸的价值（分数）
        self.zombie_value = 50
        # 僵尸的生成间隔(单位:秒)
        self.add_sleep = 8
        # 第一只僵尸的出生日期
        self.last_zmb_brithday = 0
        # 子弹伤害
        self.bullet_ATK = 34
        # 最多子弹数量
        self.bullet_num_max = 1
        # 僵尸伤害
        self.zombie_ATK = 50
        # 守卫无敌时间,伤害免疫
        self.injury_immunity = 2
        # 守卫上次受伤时间
        self.guard_injury_time = 0
        # 游戏结束的标志
        self.if_game = False

    # 记录上一只僵尸的出生日期
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
        # # 限制子弹数量
        # self.bullet_num_max = 1  # 最大子弹数量为此值加一

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


# 设置按钮类
class Button:
    def __init__(self, setting, screen, msg):
        self.setting = setting
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮宽度和高度
        self.width, self.height = 200, 50
        # 设置按钮颜色
        self.button_color = (214, 195, 192)
        # 设置文本颜色
        self.text_color = (255, 255, 255)
        # 设置文本字体和字号，None则默认字体
        self.font = pygame.font.SysFont(None, 48)

        # 设置按钮位置
        self.rect = pygame.Rect(  # 我也不知道为什么除以二，但是他确实居中了，我是个天才
            self.screen_rect.centerx - self.width / 2,
            self.screen_rect.centery - self.height / 2,
            self.width,
            self.height,
        )  # 一般位置都是后调的，直接使用center即可

        # 将 msg 渲染成图片,True 表示开启标签反锯齿功能，如果没有指定背景色(按钮颜色)，Pygame将以透明背景的方式渲染文本）
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        # 设置文本的位置
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

        # 绘制按钮

    def draw_button(self):
        if self.setting.if_game == False:
            # 在屏幕上绘制按钮：    按钮颜色       按钮位置
            self.screen.fill(self.button_color, self.rect)  # 用颜色填充区域
            # 在按钮上绘制文字
            self.screen.blit(self.msg_img, self.msg_img_rect)  # 用图形填充区域


# 成就系统
class Achievement:
    def __init__(self) -> None:
        # 得分
        self.score = 0
        # 最高分
        self.score_max = 0
        # 杀敌数
        self.killed_zombies = 0
        # 总杀敌数
        self.all_killed = 0
        # 等级
        self.level = 1

    # 重置分数、杀敌数和等级,记录最高分、总杀敌数
    def reset_score(self):
        # 更新
        self.all_killed += self.killed_zombies
        if self.score > self.score_max:
            self.score_max = self.score
        # 归零
        self.score = 0
        self.killed_zombies = 0
        self.level = 1


# 分数显示
# 借助类能够长久保存数据的特性，极大的提高了程序的运行效率，重复执行的只有一个show_score
class See_Achievement:
    def __init__(self, screen, setting, achievement) -> None:
        self.screen = screen
        self.setting = setting
        self.achievement = achievement

        # 分数导入
        self.score = self.achievement.score
        self.killed_zombies = self.achievement.killed_zombies
        self.level = self.achievement.level
        # 文本设置
        self.text_color = (30, 30, 30)
        self.font_size = 30
        self.font = pygame.font.SysFont(None, self.font_size)

        # 渲染图像
        self.score_img = self.font.render(
            "score:" + str(self.score), True, self.text_color, self.setting.bg_color
        )
        self.killed_zombies_img = self.font.render(
            "kill:" + str(self.killed_zombies),
            True,
            self.text_color,
            (self.setting.bg_color),
        )
        self.level_img = self.font.render(
            "level:" + str(self.level), True, self.text_color, self.setting.bg_color
        )
        # 获取屏幕和文本位置
        self.screen_rect = self.screen.get_rect()
        self.score_img_rect = self.score_img.get_rect()
        self.killed_zombies_img_rect = self.killed_zombies_img.get_rect()
        self.level_img_rect = self.level_img.get_rect()
        # 摆放文本
        self.score_img_rect.top = self.screen_rect.top
        self.score_img_rect.centerx = self.screen_rect.centerx

        self.killed_zombies_img_rect.top = self.screen_rect.top + self.font_size
        self.killed_zombies_img_rect.centerx = self.screen_rect.centerx

        self.level_img_rect.top = self.screen_rect.top + (self.font_size * 2)
        self.level_img_rect.centerx = self.screen_rect.centerx

    # 展示得分
    def show_score(self):
        self.screen.blit(self.score_img, self.score_img_rect)
        self.screen.blit(self.killed_zombies_img, self.killed_zombies_img_rect)
        self.screen.blit(self.level_img, self.level_img_rect)

    # 重新渲染图像
    def make_img(self):
        # 渲染图像
        self.score_img = self.font.render(
            "score:" + str(self.score), True, self.text_color, self.setting.bg_color
        )
        self.killed_zombies_img = self.font.render(
            "kill:" + str(self.killed_zombies),
            True,
            self.text_color,
            (self.setting.bg_color),
        )
        self.level_img = self.font.render(
            "level:" + str(self.level), True, self.text_color, self.setting.bg_color
        )

    # 更新得分数据
    def update_score(self, score, killed_zombies, level):
        self.score = score
        self.killed_zombies = killed_zombies
        self.level = level
        self.make_img()
