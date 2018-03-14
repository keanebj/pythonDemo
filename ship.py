import pygame


class Ship():
    def __init__(self, ai_settings,screen):
        #  初始化飞机的的位置
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载图片
        self.image = pygame.image.load("images/plane.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞机放置最底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.left=self.screen_rect.left

        self.moving_right = False
        self.moving_left = False
        self.moving_up=False
        self.moving_down=False

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def update(self):
        # print(self.rect.top,self.rect.bottom,self.screen_rect.top,self.screen_rect.bottom,self.moving_up,self.moving_down,self.bottom)

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            # self.rect.centerx -= 1

        # if self.moving_up and self.rect.top > 0:
        #     self.bottom -= self.ai_settings.ship_speed_factor

        # if self.bottom >self.screen_rect.bottom:
        #     self.moving_down=False


        # if self.rect.top < self.screen_rect.top:
        #     self.moving_up=False

        # if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #     self.bottom += self.ai_settings.ship_speed_factor


        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
        # self.rect.centery = self.center

    def blitme(self):
        # 指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
