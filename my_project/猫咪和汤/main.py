from click import click_food,Setting,grade_up

while True:
    # 创建setting类
    St = Setting()

    while True:
        #刷新窗口位置
        St.update_win()

        # 点击做完的饭菜
        click_food(St)

        #升级
        grade_up(St)



        

    break
