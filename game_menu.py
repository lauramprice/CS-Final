import pygame
import random


pygame.init()
window_size=[900,700]
window=pygame.display.set_mode(window_size)

rect_pos=(400,600)
rect_Rect= [383,570, 100,60]
rect_color=pygame.Color(204,170,187)


x=pygame.image.load('/home/ooloyede/cs-camp/CS-Final/vassarlib.xcf').convert()

x=pygame.transform.scale(x,(900,700))


window.blit(x,(0,0))

pygame.font.init() 

myfont = pygame.font.SysFont('Comic Sans MS', 63)
textsurface = myfont.render('Wack ', False, (204,170,187))
window.blit(textsurface,(670,100))

myfont = pygame.font.SysFont('Comic Sans MS', 63)
textsurface = myfont.render(' A ', False, (204,170,187))
window.blit(textsurface,(700,140))

myfont = pygame.font.SysFont('Comic Sans MS', 60)
textsurface = myfont.render(' Wompwomp!', False, (204,170,187))
window.blit(textsurface,(600,180))


def Rect1 (surface,rect_color,rect_Rect,rect_width=0):
    pygame.draw.rect(surface,rect_color,rect_Rect,rect_width)


Rect1(window,rect_color, rect_Rect)


myfont = pygame.font.SysFont('Comic Sans MS', 50)
textsurface = myfont.render('Play', False, (0, 0, 0))
window.blit(textsurface,(400,580))

pygame.display.flip()

input()


