import pygame
import pygame.freetype
import random

rect_Rect= [418,380, 85,33]
rect_color=pygame.Color(244,141,141)

rect_Rect2= [380,428, 158,33]
rect_color2=pygame.Color(244,141,141)

rect_Rect3= [250,250, 500,300]
rect_color3=pygame.Color(255,255,255)

instrcirc_pos= (740,260)
instrcirc_color= pygame.Color(0,0,0)
instrcirc_radius= 13

instrcirc_pos2= (740,260)
instrcirc_color2 = pygame.Color(163,19,19)
instrcirc_radius2 = 11


#Clickable areas that draws another screenn/surface

def Rect2 (surface,rect_color1,rect_Rect1,rect_width2=0):
    pygame.draw.rect(surface,rect_color2,rect_Rect2,rect_width2)

def Rect1 (surface,rect_color,rect_Rect,rect_width=0):
    pygame.draw.rect(surface,rect_color,rect_Rect,rect_width)

pygame.init()
window_size=[1000,900]
window=pygame.display.set_mode(window_size)

x=pygame.image.load('/home/ooloyede/cs-camp/CS-Final/library1.xcf').convert()
x=pygame.transform.scale(x,(1000,900))

pygame.font.init() 

#Game Title
gtitle = pygame.font.SysFont('liberationsansnarrow', 45)
textsurface1 = gtitle.render('Wack A Wompwomp!', False, (0, 0, 0))

gplaybtn= pygame.font.SysFont('liberationsansnarrow', 25)
textsurface2 = gplaybtn.render('PLAY', False, (0, 0, 0))

ginstrbtn = pygame.font.SysFont('liberationsansnarrow', 23)
textsurface3 = ginstrbtn.render('INSTRUCTIONS', False, (0, 0, 0))

ginstrfont= pygame.font.SysFont('lato', 18)
textsurface4 =ginstrfont.render('Use the MOUSE to click on the groundhogs as they appear. ', False, (242,79,79))

ginstrfont1= pygame.font.SysFont('lato', 23)
textsurface5 =ginstrfont1.render('Click as many as you can in 30 secs!!', False, (242,79,79))

instr_exit = pygame.font.SysFont('Comic Sans MS', 35) 
textsurface6= instr_exit.render('X', False, (0, 0, 0))

showinstr = False

while True:
    for y in pygame.event.get():
        if y.type ==pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(rect_Rect2).collidepoint(y.pos):
                showinstr = True
            if pygame.Rect(rect_Rect).collidepoint(y.pos):
                #break #game_design()
                pass

    window.fill((0,0,0))
    window.blit(x,(0,0))
    window.blit(textsurface1,(270,280))
    Rect1(window,rect_color, rect_Rect)
    window.blit(textsurface2,(435,383))
    Rect2(window,rect_color2, rect_Rect2)
    window.blit(textsurface3,(385,430))

    if showinstr == True:
        pygame.draw.rect(window,rect_color3,rect_Rect3,0)
        window.blit(textsurface4,(275,340))
        window.blit(textsurface5,(310,420))   
        pygame.draw.circle(window,instrcirc_color,instrcirc_pos, instrcirc_radius,0) 
        pygame.draw.circle(window,instrcirc_color2,instrcirc_pos2 , instrcirc_radius2,0)  
        window.blit(textsurface6,(743,250))

    pygame.display.flip()
#function to call Laura's loop
input()
