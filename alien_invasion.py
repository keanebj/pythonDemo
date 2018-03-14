import sys

import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group



def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((
        ai_settings.screen_width,
        ai_settings.screen_height
    ))

    # screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    # bg_color=(230,250,200)
    
    ship = Ship(ai_settings,screen)
    

    # 子弹组
    bullets=Group()
    
    
    # 主循环
    while True:
        # for event in pygame.event.get():
        #       if event.type==pygame.QUIT:
        #           sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # bullets.draw_bullet()
        gf.update_bullets(bullets)
       
        # 删除已消失的子弹

        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)
        # print(len(bullets))   
        print(bullets) 

        gf.update_screen(ai_settings, screen, ship, bullets)
        # screen.fill(bg_color)  
        screen.fill(ai_settings.bg_color)
        ship.blitme()
       
        pygame.display.flip()


run_game()
