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
                guard.moving_right = True
            # 向左移动
            if pressed_keys[pygame.K_a]:
                guard.moving_left = True
            # 向上移动
            if pressed_keys[pygame.K_w]:
                guard.moving_up = True
            # 向下移动
            if pressed_keys[pygame.K_s]:
                guard.moving_down = True

        if event.type == pygame.KEYUP:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_d] == None:
                guard.moving_right = False
            elif pressed_keys[pygame.K_a] == None:
                guard.moving_left = False
            elif pressed_keys[pygame.K_w] == None:
                guard.moving_up = False
            elif pressed_keys[pygame.K_s] == None:
                guard.moving_down = False

        # 守卫移动
        guard.moving()
