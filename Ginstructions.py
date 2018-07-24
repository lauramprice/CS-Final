import pygame
import random


pygame.init()
window_size=[1000,900]
window=pygame.display.set_mode(window_size)

rect_Rect3= [418,380, 85,30]
rect_color3=pygame.Color(204,170,187)


def Rect3 (surface,rect_color3,rect_Rect3,rect_width3=0):
    pygame.draw.rect(surface,rect_color3,rect_Rect3,rect_width3)


Rect3(window,rect_color3, rect_Rect3)
