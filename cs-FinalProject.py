import pygame
import random


pygame.init()
window_size=[900,780]
window=pygame.display.set_mode(window_size)

rect_pos=(100,100)
rect_Rect= [134,134, 600,500]
rect_color=pygame.Color(18,52,17)

rect_pos2=(100,100)
rect_Rect2= [200,200, 465,370]
rect_color2=pygame.Color(205,234,144)

x=pygame.image.load('/home/ooloyede/cs-camp/wompwomp.xcf').convert()


def Rect1 (surface,rect_color,rect_Rect,rect_width=0):
    pygame.draw.rect(surface,rect_color,rect_Rect,rect_width)

window.fill(pygame.Color(255,255,255))

Rect1(window,rect_color, rect_Rect)

def Rect2(surface,rect_color2,rect_Rect2,rect_width2=0):
    pygame.draw.rect(surface,rect_color2,rect_Rect2,rect_width2)

Rect2(window,rect_color2, rect_Rect2)

x=pygame.transform.scale(x,(300,300))

window.blit(x, (282,200))

pygame.font.init() 

myfont = pygame.font.SysFont('Comic Sans MS', 80)
textsurface = myfont.render('Wack a wompwomp!', False, (204,170,187))
window.blit(textsurface,(190,170))



circ_pos=(430,600)
circ_radius=70
circ_color=pygame.Color(204,170,187)

circ_pos2=(435,600)
circ_radius2=50
circ_color2=pygame.Color(255,211,255)



def circle1(surface,circ_color,circ_pos, circ_radius):
    pygame.draw.circle(surface, circ_color,circ_pos,circ_radius)

def circle2(surface,circ_color2,circ_pos2,circ_radius2):
    pygame.draw.circle(surface, circ_color2,circ_pos2,circ_radius2)

circle1(window, circ_color,circ_pos,circ_radius)
circle2(window, circ_color2,circ_pos2,circ_radius2)

myfont = pygame.font.SysFont('Comic Sans MS', 50)
textsurface = myfont.render('Play', False, (0, 0, 0))
window.blit(textsurface,(400,580))

pygame.display.flip()

input()


