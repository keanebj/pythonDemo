import sys
import pygame
from pygame import locals
import time
import decide

#自己写的一个模块，如果要使用必须将本模块和这个模块放在同一个文件夹里
def run_game():
    pygame.init()#初始化
    scr=pygame.display.set_mode((1366,768),locals.FULLSCREEN)#第一个参数是分辨率，第二个是设置成全屏模式，
    pygame.display.set_caption('飞船大战外星人')#标题
    
    craft_image=pygame.image.load('images/plane.png')#飞船图片，记得是bmp后缀
    craft_rect=craft_image.get_rect()#得到相应的方框，便于处理，这是pygame很便捷的一个方面
    scr_rect=scr.get_rect()
    craft_rect.centerx=scr_rect.centerx#设置在界面中央
    craft_rect.bottom=scr_rect.bottom#设置在界面底部
    scr.blit(craft_image,craft_rect)#在界面上画出飞船
    
    moving_right=False#以下均为标志
    moving_left=False
    moving_down=False
    moving_up=False
    flag1=False
    flag2=False
    flag3=False
    flag3=False
    flag4=False
    flag5=False
    flag6=False
    flag7=False
    flag8=False
    flag9=False
    flag10=False
    flaga=True
    flagr=True
    flagl=False
    a=1
    
    alien_image=pygame.image.load('images/plane.png')#外星人图片
    alien_rect=alien_image.get_rect()
    alien_rect.centerx=scr_rect.centerx
    alien_rect.top=scr_rect.top
    myfont=pygame.font.SysFont('simkai.ttf',40)#设置最后的输出字体
    text_surface1=myfont.render('You are successful!',True,(255,0,0),(255,255,255))
    text_surface2=myfont.render('Sorry,but you fail!',True,(255,0,0),(255,255,255))
    
    while True:
        scr.fill((230,230,230))#屏幕背景调成灰色，rgb都不懂的，要百度了
        scr.blit(alien_image,alien_rect)#在界面上画出外星人
        if flaga==True:
            if a%5==0:#设置外星人每五次之后就下降一个像素
               alien_rect.bottom +=1
            a +=1
            
            if flagr==True:#这一段代码让外星人先右下再碰壁反弹，再左下再碰壁再回来
                if alien_rect.right<scr_rect.right:
                    alien_rect.centerx +=2
                elif alien_rect.right==scr_rect.right:
                    flagl=True
                    flagr=False
            elif flagl==True:
                if alien_rect.left>scr_rect.left:
                    alien_rect.centerx -=2
                elif alien_rect.left==scr_rect.left:
                    flagl=False
                    flagr=True

        for event in pygame.event.get():#接受玩家对于游戏的命令
            if event.type==pygame.MOUSEBUTTONDOWN:#最终是点击屏幕就可以退出游戏
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                   moving_right=True
                if event.key==pygame.K_LEFT:
                    moving_left=True
                if event.key==pygame.K_DOWN:
                    moving_down=True
                if event.key==pygame.K_UP:
                    moving_up=True
                if event.key==32:#点击空格键。这一段代码虽然看起来啰啰嗦嗦，但是都是一样的
                    if flag1==False:
                        bullet_rect1=pygame.Rect(0,0,5,10)
                        bullet_rect1.centerx=craft_rect.centerx
                        bullet_rect1.top=craft_rect.top
                        bullet_color1=(220,20,60)
                        pygame.draw.rect(scr,bullet_color1,bullet_rect1)
                        flag1=True
                    elif flag2==False:
                        bullet_rect2=pygame.Rect(0,0,5,10)
                        bullet_rect2.centerx=craft_rect.centerx
                        bullet_rect2.top=craft_rect.top
                        bullet_color2=(220,20,60)
                        pygame.draw.rect(scr,bullet_color2,bullet_rect2)
                        flag2=True
                    elif flag3==False:
                        bullet_rect3=pygame.Rect(0,0,5,10)
                        bullet_rect3.centerx=craft_rect.centerx
                        bullet_rect3.top=craft_rect.top
                        bullet_color3=(220,20,60)
                        pygame.draw.rect(scr,bullet_color3,bullet_rect3)
                        flag3=True
                    elif flag4==False:
                        bullet_rect4=pygame.Rect(0,0,5,10)
                        bullet_rect4.centerx=craft_rect.centerx
                        bullet_rect4.top=craft_rect.top
                        bullet_color4=(220,20,60)
                        pygame.draw.rect(scr,bullet_color4,bullet_rect4)
                        flag4=True
                    elif flag5==False:
                        bullet_rect5=pygame.Rect(0,0,5,10)
                        bullet_rect5.centerx=craft_rect.centerx
                        bullet_rect5.top=craft_rect.top
                        bullet_color5=(220,20,60)
                        pygame.draw.rect(scr,bullet_color5,bullet_rect5)
                        flag5=True
                    elif flag6==False:
                        bullet_rect6=pygame.Rect(0,0,5,10)
                        bullet_rect6.centerx=craft_rect.centerx
                        bullet_rect6.top=craft_rect.top
                        bullet_color6=(220,20,60)
                        pygame.draw.rect(scr,bullet_color6,bullet_rect6)
                        flag6=True
                    elif flag7==False:
                        bullet_rect7=pygame.Rect(0,0,5,10)
                        bullet_rect7.centerx=craft_rect.centerx
                        bullet_rect7.top=craft_rect.top
                        bullet_color7=(220,20,60)
                        pygame.draw.rect(scr,bullet_color7,bullet_rect7)
                        flag7=True
                    elif flag8==False:
                        bullet_rect8=pygame.Rect(0,0,5,10)
                        bullet_rect8.centerx=craft_rect.centerx
                        bullet_rect8.top=craft_rect.top
                        bullet_color8=(220,20,60)
                        pygame.draw.rect(scr,bullet_color8,bullet_rect8)
                        flag8=True
                    elif flag9==False:
                        bullet_rect9=pygame.Rect(0,0,5,10)
                        bullet_rect9.centerx=craft_rect.centerx
                        bullet_rect9.top=craft_rect.top
                        bullet_color9=(220,20,60)
                        pygame.draw.rect(scr,bullet_color9,bullet_rect9)
                        flag9=True
                    elif flag10==False:
                        bullet_rect10=pygame.Rect(0,0,5,10)
                        bullet_rect10.centerx=craft_rect.centerx
                        bullet_rect10.top=craft_rect.top
                        bullet_color10=(220,20,60)
                        pygame.draw.rect(scr,bullet_color10,bullet_rect10)
                        flag10=True
                    
            elif event.type==pygame.KEYUP:
                
                if event.key==pygame.K_RIGHT:
                    moving_right=False
                if event.key==pygame.K_LEFT:
                    moving_left=False
                if event.key==pygame.K_DOWN:
                    moving_down=False
                if event.key==pygame.K_UP:
                    moving_up=False
                
        if moving_right==True:
            if craft_rect.right>scr_rect.right:
                pass
            else:
                craft_rect.centerx +=5#在这里可以更改飞船的移动速度
        if moving_left==True:
            if craft_rect.left<scr_rect.left:
                pass
            else:
                craft_rect.centerx -=5
        if moving_down==True:
            if craft_rect.bottom>scr_rect.bottom:
                pass
            else:
                craft_rect.bottom +=5
        if moving_up==True:
            if craft_rect.top<scr_rect.top:
                pass
            else:
                craft_rect.bottom -=5
        scr.blit(craft_image,craft_rect)#画出飞船
        if flag1==True:
            if decide.d1(bullet_rect1,alien_rect):#如果子弹触碰到外星人
                flag1=False
                flaga=False
                print('1st')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()#刷新屏幕显示文字
                time.sleep(3)#控制暂停3秒，然后游戏结束
                pygame.quit()
                sys.exit()
            if bullet_rect1.top>scr_rect.top :#子弹到达界面外部，就消失了，此时就可以发射第11颗子弹了
                bullet_rect1.bottom -=1
                pygame.draw.rect(scr,bullet_color1,bullet_rect1)
            else:
                flag1=False
        if flag2==True:
            if decide.d1(bullet_rect2,alien_rect):
                flag2=False
                flaga=False
                print('2nd')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect2.top>scr_rect.top:
                bullet_rect2.bottom -=1
                pygame.draw.rect(scr,bullet_color2,bullet_rect2)
            else:
                flag2=False
        if flag3==True:
            if decide.d1(bullet_rect3,alien_rect):
                flaga=False
                scr.blit(text_surface1,(600,350))
                print('3rd')
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect3.top>scr_rect.top:
                bullet_rect3.bottom -=1
                pygame.draw.rect(scr,bullet_color3,bullet_rect3)
            else:
                flag3=False
        if flag4==True:
            if decide.d1(bullet_rect4,alien_rect):
                flag4=False
                flaga=False
                print('4th')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect4.top>scr_rect.top:
                bullet_rect4.bottom -=1
                pygame.draw.rect(scr,bullet_color4,bullet_rect4)
            else:
                flag4=False
        if flag5==True:
            if decide.d1(bullet_rect5,alien_rect):
                flag5=False
                flaga=False
                print('5th')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect5.top>scr_rect.top:
                bullet_rect5.bottom -=1
                pygame.draw.rect(scr,bullet_color5,bullet_rect5)
            else:
                flag5=False
        if flag6==True:
            if decide.d1(bullet_rect6,alien_rect):
                flag6=False
                flaga=False
                print('6th')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect6.top>scr_rect.top:
                bullet_rect6.bottom -=1
                pygame.draw.rect(scr,bullet_color6,bullet_rect6)
            else:
                flag6=False
        if flag7==True:
            if decide.d1(bullet_rect7,alien_rect):
                flag7=False
                flaga=False
                print('7th')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect7.top>scr_rect.top:
                bullet_rect7.bottom -=1
                pygame.draw.rect(scr,bullet_color7,bullet_rect7)
            else:
                flag7=False
        if flag8==True:
            if decide.d1(bullet_rect8,alien_rect):
                flag8=False
                flaga=False
                print('8th')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect8.top>scr_rect.top:
                bullet_rect8.bottom -=1
                pygame.draw.rect(scr,bullet_color8,bullet_rect8)
            else:
                flag8=False
        if flag9==True:
            if decide.d1(bullet_rect9,alien_rect):
                flag9=False
                flaga=False
                print('9th')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect9.top>scr_rect.top:
                bullet_rect9.bottom -=1
                pygame.draw.rect(scr,bullet_color9,bullet_rect9)
            else:
                flag9=False
        if flag10==True:
            if decide.d1(bullet_rect10,alien_rect):
                flag10=False
                flaga=False
                print('10th')
                scr.blit(text_surface1,(600,350))
                pygame.display.flip()
                time.sleep(3)
                pygame.quit()
                sys.exit()
            if bullet_rect10.top>scr_rect.top:
                bullet_rect10.bottom -=1
                pygame.draw.rect(scr,bullet_color10,bullet_rect10)
            else:
                flag10=False
        if alien_rect.bottom==scr_rect.bottom or decide.d2(alien_rect,craft_rect):#判断失败的两个条件
            scr.blit(text_surface2,(600,350))
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
            sys.exit()
        scr.blit(alien_image,alien_rect)
        pygame.display.flip()
        
run_game()
