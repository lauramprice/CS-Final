import pygame
import random


pygame.init()
window_size=[900,700]
window=pygame.display.set_mode(window_size)

rect_pos=(400,600)
rect_Rect= [395,564, 85,60]
rect_color=pygame.Color(204,170,187)

rect_pos2=(400,600)
rect_Rect2= [383,557, 110,80]
rect_color2=pygame.Color(204,140,167)

x=pygame.image.load('/home/ooloyede/cs-camp/CS-Final/vassarlib.xcf').convert()

x=pygame.transform.scale(x,(900,700))


window.blit(x,(0,0))

pygame.font.init() 

myfont = pygame.font.SysFont('Comic Sans MS', 60)
textsurface = myfont.render('Wack ', False, (204,140,167))
textsurface=pygame.transform.rotate(textsurface,349)
window.blit(textsurface,(670,80))

myfont = pygame.font.SysFont('Comic Sans MS', 60)
textsurface = myfont.render(' A ', False, (204,140,167))
textsurface=pygame.transform.rotate(textsurface,349)
window.blit(textsurface,(700,130))

myfont = pygame.font.SysFont('Comic Sans MS', 53)
textsurface = myfont.render(' Wompwomp!', False, (204,140,167))
textsurface=pygame.transform.rotate(textsurface,349)
window.blit(textsurface,(600,170))

def Rect2 (surface,rect_color1,rect_Rect1,rect_width2=0):
    pygame.draw.rect(surface,rect_color2,rect_Rect2,rect_width2)


Rect2(window,rect_color2, rect_Rect2)

def Rect1 (surface,rect_color,rect_Rect,rect_width=0):
    pygame.draw.rect(surface,rect_color,rect_Rect,rect_width)


Rect1(window,rect_color, rect_Rect)




myfont = pygame.font.SysFont('Comic Sans MS', 50)
textsurface = myfont.render('Play', False, (0, 0, 0))
window.blit(textsurface,(400,580))

pygame.display.flip()

input()


while False: 
    for x in pygame.event.get():
        if x.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(rect_Rect).collidepoint(x.pos):
                pass
