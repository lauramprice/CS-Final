
import random
import pygame
pygame.init()
pygame.font.init() 

window_size=[1000,900]
window=pygame.display.set_mode(window_size)

class Hole(object):

    def __init__(self, pos, size, color, width):
        """Stores all of the above information about the groundhog hole"""
        self.pos = list(pos)
        self.size = list(size)
        self.color = list(color)
        self.width = width
        
    def __repr__(self):
        """ Displays groundhog data in an organized format"""
        need = str(self.pos)
        return need

    def draw_hole(self):
        """ Draws the groundhog holes"""
        pygame.draw.ellipse(window, self.color, self.pos + self.size, self.width)

class Groundhog(object):

    def __init__(self, Hole, gh_color, gh_width):
        self.gh_pos = [Hole.pos[0] + (Hole.size[0] / 7), Hole.pos[1] - (Hole.size[1] * .15)]
        self.gh_size = [Hole.size[0] * 0.70 , Hole.size[1] * 0.90]
        self.gh_color = gh_color
        self.gh_width = gh_width

    def draw_gh(self):
        """ Draws the groundhog box"""
        pygame.draw.rect(window, self.gh_color, self.gh_pos + self.gh_size, self.gh_width)

def game_design():

    """ Game Window Additions and Background """
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

    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    textsurface = myfont.render('X', False, (0, 0, 0))
    window.blit(textsurface,(963, 19))


    """ Creation of the Game Board"""
    """ Guide board for the 3D perspective of the holes:
    board_color = pygame.Color(85, 107, 47)
    board_vertices = [(250, 560), (770, 560), (950, 840), (75, 840)]
    board_width = 0

    def draw_board(surface, board_color, board_vertices, board_width):
        pygame.draw.polygon(surface, board_color, board_vertices, board_width)

    draw_board(window, board_color, board_vertices, board_width)
    """

    # First row of holes
    def draw_hole_r1(n):
        holes_row1 = []
        color = pygame.Color(82, 54, 27)
        size = (60, 50)
        width = 0
        x_hole_pos = 235
        y_hole_pos = 535

        for x in range(n):
            draw_h = Hole([x_hole_pos] + [y_hole_pos], size, color, width)
            draw_h.draw_hole()
            holes_row1 += [draw_h]
            x_hole_pos += 115

        return holes_row1
        
    draw_hole_r1(5)

    # Second row of holes
    def draw_hole_r2(n):
        holes_row2 = []
        color = pygame.Color(82, 54, 27)
        size = (80, 70)
        width = 0
        x_hole_pos = 195
        y_hole_pos = 620

        for x in range(n):
            draw_h = Hole([x_hole_pos] + [y_hole_pos], size, color, width)
            draw_h.draw_hole()
            holes_row2 += [draw_h]
            x_hole_pos += 130

        return holes_row2

    draw_hole_r2(5)

    # Third row of holes
    def draw_hole_r3(n):
        holes_row3 = []
        color = pygame.Color(82, 54, 27)
        size = (100, 90)
        width = 0
        x_hole_pos = 125
        y_hole_pos = 730

        for x in range(n):
            draw_h = Hole([x_hole_pos] + [y_hole_pos], size, color, width)
            draw_h.draw_hole()
            holes_row3 += [draw_h]
            x_hole_pos += 160

        return holes_row3

    draw_hole_r3(5)

    holes_list = draw_hole_r1(5) + draw_hole_r2(5) + draw_hole_r3(5)
    print(holes_list)

    """ Adding in the ground hogs"""

    def get_groundhog(n):
    
        gh_color = pygame.Color(0, 0, 0)
        gh_width = 0

        for x in range(n):
            gh_location = random.choice(holes_list)
            individual_gh = Groundhog(gh_location, gh_color, gh_width)
            individual_gh.draw_gh()



    """
        x = pygame.image.load('/home/laprice/cscamp/CS-Final/gh.png').convert()
        x = pygame.transform.scale(x ,(100,100))
        window.blit(x, (gh_location[0], gh_location[1])
        
        #print(gh_location)
        """
    get_groundhog(5)
    

game_design()


pygame.display.flip()