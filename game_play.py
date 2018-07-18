
import random
import pygame
pygame.init()

""" Game Window and Background """
window_size=[1000,900]
window=pygame.display.set_mode(window_size)

x = pygame.image.load('/home/laprice/cscamp/CS-Final/library.JPG').convert()
x=pygame.transform.scale(x,(1000,900))
window.blit(x, (0, 0))

circle_color = pygame.Color(255, 51, 51)
circle_color2 = pygame.Color(0, 0, 0)
circle_pos = (970, 30)
circle_radius = 15
circle_radius2 = 17
circle_width = 0

pygame.draw.circle(window, circle_color2, circle_pos, circle_radius2, circle_width)
pygame.draw.circle(window, circle_color, circle_pos, circle_radius, circle_width)


""" Creation of the Game Board"""
""" The Green board beneath the holes:
board_color = pygame.Color(85, 107, 47)
board_vertices = [(250, 560), (770, 560), (950, 840), (75, 840)]
board_width = 0

def draw_board(surface, board_color, board_vertices, board_width):
    pygame.draw.polygon(surface, board_color, board_vertices, board_width)

draw_board(window, board_color, board_vertices, board_width)
"""
# First row of holes
def draw_hole_r1(n):
    hole_color = pygame.Color(82, 54, 27)
    hole_pos = (535, 60, 50)
    hole_width = 0
    x_hole_pos = 235

    for x in range(n):
        pygame.draw.ellipse(window, hole_color, [x_hole_pos] + list(hole_pos), hole_width)
        x_hole_pos += 115
        
draw_hole_r1(5)

# Second row of holes
def draw_hole_r2(n):
    hole_color = pygame.Color(82, 54, 27)
    hole_pos = (620, 80, 70)
    hole_width = 0
    x_hole_pos = 195

    for x in range(n):
        pygame.draw.ellipse(window, hole_color, [x_hole_pos] + list(hole_pos), hole_width)
        x_hole_pos += 130
        
draw_hole_r2(5)

# Third row of holes
def draw_hole_r3(n):
    hole_color = pygame.Color(82, 54, 27)
    hole_pos = (730, 100, 90)
    hole_width = 0
    x_hole_pos = 125

    for x in range(n):
        pygame.draw.ellipse(window, hole_color, [x_hole_pos] + list(hole_pos), hole_width)
        x_hole_pos += 160
        

draw_hole_r3(5)

pygame.display.flip()