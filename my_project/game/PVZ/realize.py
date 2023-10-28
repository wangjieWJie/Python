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

# 文本转推片
import pygame.font


# 等待游戏开始
def wait_play(now_setting, fight_screen, play_button, achievement):
    # 检查鼠标活动
    check_point(now_setting, play_button, achievement)

    # 更新等待界面
    update_wait(now_setting, fight_screen, play_button, achievement)


# 更新等待界面
def update_wait(now_setting, fight_screen, play_button, achievement):
    # 填充等待界面背景颜色
    fight_screen.fill(now_setting.bg_color)
    # 显示光标
    pygame.mouse.set_visible(True)
    # 绘制成绩单
    see_score_waitting(fight_screen, achievement)
    # 绘制play按钮
    play_button.draw_button()
    # 更新屏幕，让最近绘制的屏幕可见
    pygame.display.flip()


# 检查鼠标活动
def check_point(now_setting, play_button, achievement):
    # 检查退出游戏
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_quit(achievement)
        # 检查点击按钮
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 获取鼠标 x, y 坐标，pygame.mouse. get_pos() 返回一个元组，其中包含玩家单击时鼠标的x和y坐标
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # collidepoint()检查鼠标单击位置是否在Play按钮的rect内
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                now_setting.if_game = True


# 更新屏幕
def update_screen(
    fight_screen, now_setting, zombies, fox, bullets, achievement, see_achievement
):
    # 设置fight_screen的背景颜色，fill方法一次只能调用一个参数，一种颜色，表示将这个颜色填满屏幕
    fight_screen.fill(now_setting.bg_color)

    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 绘制守卫
    fox.put_guard()

    # 绘制子弹
    for bullet in bullets.sprites():  # 遍历编组中所有的子弹
        bullet.bullet_draw()  # 绘制每个子弹

    # 绘制僵尸
    zombie_coming(zombies)

    # 显示计分
    see_achievement.show_score()

    # 更新屏幕，让最近绘制的屏幕可见
    pygame.display.flip()


# 增大游戏难度
def harder(achievement, zombies):
    for one_zombies in zombies:
        # 僵尸移速增加
        one_zombies.zmb_speed = (
            achievement.killed_zombies / 100 + one_zombies.zmb_speed_basic
        )
        # 增加僵尸血量
        one_zombies.zmb_blood = (
            achievement.killed_zombies * 10 + one_zombies.zmb_blood_basic
        )


# 接收鼠标和键盘的各种操作的函数
def check_event(guard, bullets, zombies, screen, setting, achievement):
    # 相应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_quit(achievement)

        # 移动守卫的条件
        guard_moving(event, guard)
        # 按键抬起时停止移动的条件
        guard_stop(event, guard)

        # 守卫移动
        guard.moving()

        # 创建子弹
        test_bullet = Bullet(screen, guard)  # 创建一个子弹类的子弹，以便于使用子弹类中各种参数
        bullet_shoot(event, guard, setting, bullets, screen)


# 移动守卫的条件
def guard_moving(event, guard):
    if event.type == pygame.KEYDOWN:
        # 向右移动
        if event.key == pygame.K_d:
            guard.moving_right = True
        # 向左移动
        if event.key == pygame.K_a:
            guard.moving_left = True  #  全都使用 if 而是不 elif。防止同时按下两个按键时只能响应一个按键
        # 向上移动
        if event.key == pygame.K_w:
            guard.moving_up = True

        # 向下移动
        if event.key == pygame.K_s:
            guard.moving_down = True


# 按键抬起时停止移动的条件
def guard_stop(event, guard):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            guard.moving_right = False
        elif event.key == pygame.K_a:
            guard.moving_left = False  # 不需要全部使用if，因为两个按键不可能同时松开，即同时处于松开的状态
        elif event.key == pygame.K_w:  # 因为他们是两个不同的事件
            guard.moving_up = False
        elif event.key == pygame.K_s:
            guard.moving_down = False


# 创建子弹
def bullet_shoot(event, guard, setting, bullets, screen):
    if event.type == pygame.KEYDOWN:
        if (
            event.key == pygame.K_SPACE
            and len(bullets) <= setting.bullet_num_max  # 限制子弹数量
        ):
            # 创建一个新的 bullet
            bullet_new = Bullet(screen, guard)
            # 将子弹加入到编组bullets中
            bullets.add(bullet_new)


# 绘制僵尸
def zombie_coming(zombies):
    for one_zombie in zombies:
        one_zombie.put_zmb()


# 生成僵尸
def add_zombie(
    zombies, screen, time_setting, achievement
):  # 设置模块中包含最大僵尸数、上一个僵尸的创建时间、僵尸生成间隔
    if len(zombies) <= time_setting.zombie_max:
        if len(zombies) < 1:  # 僵尸全部死亡时，立即创建一个僵尸，并且创建游戏开始的第一个僵尸
            new_zombei = Zombie(screen)
            zombies.add(new_zombei)
            harder(achievement, zombies)  # 强化僵尸
            time_setting.last_zmb_brithday = time.time()  # 储存上一个僵尸的生成时间
        elif (
            len(zombies) >= 1  # 达到时间间隔之后生成僵尸
            and (time.time() - time_setting.last_zmb_brithday) > time_setting.add_sleep
        ):
            new_zombei = Zombie(screen)
            zombies.add(new_zombei)
            harder(achievement, zombies)  # 强化僵尸
            time_setting.last_zmb_brithday = time.time()  # 储存僵尸生成的时间


# 删除看不见了的子弹
def bullet_delete(bullets, now_setting):
    for bullet in bullets.copy():  # 书上使用的是 in bullets.copy() 我没有使用但是好像也可以正常删除没有问题
        if bullet.rect.x > now_setting.fight_screen_width:
            bullets.remove(bullet)


# 扣除僵尸血量并杀死他们
def hit_zombies(screen, bullets, zombies, now_setting, achievement, see_achievement):
    # 检测子弹和僵尸的碰撞，并删除子弹或者僵尸
    # pygame.sprite.groupcollide（）–两个精灵组中所有精灵的碰撞检测
    # hit = pygame.sprite.groupcollide(bullets, zombies, True, False)
    # sprite提供的groupcollide函数能够检测两个编组中的每个surface是否碰撞，并且返回一个以子弹为键、以僵尸为值的字典
    # 在这个字典中，每个值都是被子弹击中的僵尸
    # 函数最后俩个参数分别代表是否将击中僵尸的bullet和被子弹击中的zombie在他们所在的编组中删除
    for zombie_sprite in zombies.copy():
        # pygame.sprite.spritecollide() —判断某个精灵和指定精灵组中的精灵的碰撞,Ture表示，如果发生碰撞，则移除指定精灵组中的精灵
        hit = pygame.sprite.spritecollide(zombie_sprite, bullets, True)
        if hit:
            zombie_sprite.zmb_blood -= now_setting.bullet_ATK
            if zombie_sprite.zmb_blood <= 0:
                zombies.remove(zombie_sprite)
                update_achievement(achievement, see_achievement, now_setting)


# 更新成就、计分系统
def update_achievement(achievement, see_achievement, setting):
    # 升级
    achievement.killed_zombies += 1
    achievement.score += setting.zombie_value
    achievement.level = int(achievement.killed_zombies / 5) + 1
    # 守卫升级
    setting.bullet_num_max = achievement.level + 1

    # 更新计分面板
    see_achievement.update_score(
        achievement.score, achievement.killed_zombies, achievement.level
    )


# 更新守卫血量
def update_guard_blood(now_setting, zombies, fox):
    fox_hit = pygame.sprite.spritecollide(fox, zombies, False)
    if (
        fox_hit
        and time.time() - now_setting.guard_injury_time
        > now_setting.injury_immunity  # 设置无敌时间
    ):
        fox.guard_blood -= now_setting.zombie_ATK
        # 记录受伤时间
        now_setting.guard_injury_time = time.time()
        print(fox.guard_blood)
        if fox.guard_blood <= 0:
            now_setting.if_game = False
            print("over")


# 检查僵尸是否入侵
def kill_you(now_setting, zombies):
    for a_zombie in zombies:
        if a_zombie.rect.right < 0:
            now_setting.if_game = False
            print("over")


# 等待进入游戏时的分数显示
def see_score_waitting(screen, achievement):
    score_str = "Top score: " + str(achievement.score_max)
    killed_str = "Total killed: " + str(achievement.all_killed)
    font = pygame.font.SysFont(None, 40)
    # 渲染图象
    score_image = font.render(
        score_str,
        True,
        (50, 145, 113),
        (225, 225, 225),
    )
    killed_image = font.render(
        killed_str,
        True,
        (50, 145, 113),
        (225, 225, 225),
    )

    # 获取屏幕和文本位置
    screen_rect = screen.get_rect()
    score_rect = score_image.get_rect()
    killed_rect = killed_image.get_rect()
    # 摆放文本位置
    score_rect.centerx = screen_rect.centerx
    score_rect.top = screen_rect.top + 20

    killed_rect.centerx = screen_rect.centerx
    killed_rect.top = screen_rect.top + 40 + 20

    # 打印成绩单
    screen.blit(score_image, score_rect)
    screen.blit(killed_image, killed_rect)


# 保存然后退出
def save_quit(achievement):
    # save
    acvmt_str = str(achievement.score_max) + "\n" + str(achievement.all_killed)
    with open("my_project/game/PVZ/file/achievement", "w") as achievement_file:
        achievement_file.write(acvmt_str)
    # quit
    sys.exit()


# 读取存档
def get_score(achievement):
    with open("my_project/game/PVZ/file/achievement", "r") as achievement_file:
        all_score = []
        if achievement_file:
            for every_score in achievement_file:
                all_score.append(int(every_score.rstrip()))
            achievement.score_max = all_score[0]
            achievement.all_killed = all_score[1]
