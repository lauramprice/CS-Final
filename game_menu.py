import pygame
import pygame.freetype
import random
import math
import game_play


rect_Rect= [418,380, 85,33]
rect_color=pygame.Color(244,141,141)

rect_Rect2= [380,428, 158,33]
rect_color2=pygame.Color(244,141,141)

rect_Rect3=[245,245,510,310] 
rect_color3=pygame.Color(0,0,0)

rect_Rect4= [250,250, 500,300]
rect_color4=pygame.Color(255,255,255)


instrcirc_pos= (732,270)
instrcirc_color= pygame.Color(0,0,0)
instrcirc_radius= 15

instrcirc_pos2= (732,270)
instrcirc_color2 = pygame.Color(163,19,19)
instrcirc_radius2 = 13

instrcirc_pos3= (963,19)
instrcirc_color3= pygame.Color(0,0,0)
instrcirc_radius3= 15

instrcirc_pos4= (963,19)
instrcirc_color4 = pygame.Color(163,19,19)
instrcirc_radius4 = 13


#Clickable areas that draws another screenn/surface
""" Rectangles that hold the buttons"""
def Rect2 (surface,rect_color1,rect_Rect1,rect_width2=0):
    pygame.draw.rect(surface,rect_color2,rect_Rect2,rect_width2)

def Rect1 (surface,rect_color,rect_Rect,rect_width=0):
    pygame.draw.rect(surface,rect_color,rect_Rect,rect_width)

pygame.init()
window_size=[1000,900]
window=pygame.display.set_mode(window_size)
"""Library Image with Wompwomps"""
x=pygame.image.load('/home/ooloyede/cs-camp/CS-Final/library1.xcf').convert()
x=pygame.transform.scale(x,(1000,900))

pygame.font.init() 

"""Main page buttons"""
gtitle0= pygame.font.SysFont('liberationsansnarrow', 45)
textsurface0 = gtitle0.render('Whack A Womp womp!', False, (163,19,19))

gtitle1 = pygame.font.SysFont('liberationsansnarrow', 45)
textsurface1 = gtitle1.render('Whack A Womp womp!', False, (0, 0, 0))

gplaybtn= pygame.font.SysFont('liberationsansnarrow', 25)
textsurface2 = gplaybtn.render('PLAY', False, (0, 0, 0))

ginstrbtn = pygame.font.SysFont('liberationsansnarrow', 23)
textsurface3 = ginstrbtn.render('INSTRUCTIONS', False, (0, 0, 0))

ginstrfont= pygame.font.SysFont('lato', 18)
textsurface4 =ginstrfont.render('Use the MOUSE to click on the groundhogs as they appear. ', False, (242,79,79))

ginstrfont1= pygame.font.SysFont('lato', 23)
textsurface5 =ginstrfont1.render('Click as many as you can in 30 secs!!', False, (242,79,79))

instr_exit = pygame.font.SysFont('Comic Sans MS', 30) 
textsurface6= instr_exit.render('X', False, (0, 0, 0))

instr_exit1 = pygame.font.SysFont('Comic Sans MS', 30) 
textsurface7= instr_exit1.render('X', False, (0, 0, 0))

showinstr = False
playgame =False

def menu():
    showinstr = False
    playgame =False
    while True:
        while True:
            for y in pygame.event.get():
                if y.type ==pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(rect_Rect2).collidepoint(y.pos):
                        showinstr = True
                    elif math.sqrt((y.pos[0]- instrcirc_pos2[0])**2+(y.pos[1]- instrcirc_pos2[1])**2)< instrcirc_radius2:
                        showinstr = False
                    elif math.sqrt(( y.pos[0]- instrcirc_pos4[0])**2+(y.pos[1]- instrcirc_pos4[1])**2)< instrcirc_radius4:
                        pygame.quit()
                        break
                    elif pygame.Rect(rect_Rect).collidepoint(y.pos):
                        playgame =True
                        
            "Window for Main Menu"
            window.fill((0,0,0))
            window.blit(x,(0,0))
            window.blit(textsurface0,(273,270))
            window.blit(textsurface1,(270,270))
            Rect1(window,rect_color, rect_Rect)
            window.blit(textsurface2,(435,383))
            Rect2(window,rect_color2, rect_Rect2)
            window.blit(textsurface3,(385,430))
            pygame.draw.circle(window,instrcirc_color3,instrcirc_pos3, instrcirc_radius3,0) 
            pygame.draw.circle(window,instrcirc_color4,instrcirc_pos4 , instrcirc_radius4,0) 
            window.blit(textsurface7,(956,11))
            """Window for Instructions"""
            if showinstr == True:
                pygame.draw.rect(window,rect_color3,rect_Rect3,0)
                pygame.draw.rect(window,rect_color4,rect_Rect4,0)
                window.blit(textsurface4,(275,340))
                window.blit(textsurface5,(310,420))   
                pygame.draw.circle(window,instrcirc_color,instrcirc_pos, instrcirc_radius,0) 
                pygame.draw.circle(window,instrcirc_color2,instrcirc_pos2 , instrcirc_radius2,0)  
                window.blit(textsurface6,(725,261))
                
            """Window to commence game"""
            if playgame == True:
                break   
                    

            pygame.display.flip()
        playgame=game_play.play(window)
menu()  
