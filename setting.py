class Settings():
    # 存储游戏所有的设置的类
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 5  


        self.bullet_speed_factor=1
        self.bullet_color=(60,60,60)
        self.bullet_width=3
        self.bullet_height=15
        self.bullets_allowed=5
