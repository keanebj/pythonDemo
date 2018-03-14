import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings,screen,ship,bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up= True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True   
    elif event.key==pygame.K_SPACE:
        # 创建一个子弹，并将其加入编组bullets中
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
        # new_bullet=Bullet(ai_settings,screen,ship)
        # bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False    

def check_events(ai_settings,screen,ship,bullets):

    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
            # if event.key==pygame.K_RIGHT:
            #      ship.moing_right=True
            # elif event.key==pygame.K_LEFT:
            #      ship.moving_left=True

            # ship.rect.centerx+=1
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

            # if event.key==pygame.K_RIGHT:
            #     ship.moving_right=False
            # elif event.key==pygame.K_LEFT:
            #      ship.moving_left=False


def update_screen(ai_settings, screen, ship ,bullets):
    
    # 在飞船和外星人后面重汇所有子弹

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    screen.fill(ai_settings.bg_color)
    

    # 让最近一次页面显示
    pygame.display.flip()


def update_bullets(bullets):
    # 更新已删除子弹  更新子弹的位置
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)