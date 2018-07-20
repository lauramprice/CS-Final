
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

    def __init__(self, hole, gh_color, gh_width):
        self.gh_pos = [int(hole.pos[0] + (hole.size[0] / 7)), int(hole.pos[1] - (hole.size[1] * .15))]
        self.gh_size = [int(hole.size[0] * 0.70), int(hole.size[1] * 0.90)]
        self.gh_color = gh_color
        self.gh_width = gh_width

    def draw_gh(self):
        """ manifests a box """
        position = pygame.Rect(self.gh_pos, self.gh_size)
        gh_image = pygame.image.load('/home/laprice/cscamp/CS-Final/gh.png').convert_alpha()
        scaled_image = pygame.transform.scale(gh_image, self.gh_size)
        return scaled_image, position

class WAM(object):

    def __init__(self):
        """Window Background"""
        self.background = pygame.image.load('/home/laprice/cscamp/CS-Final/library.JPG').convert()
        self.background = pygame.transform.scale(self.background,(1000,900))

        """Window Buttons"""
        self.exit_color = pygame.Color(255, 51, 51)
        self.exit_color2 = pygame.Color(0, 0, 0)
        self.exit_pos = (970, 30)
        self.exit_radius = 15
        self.exit_radius2 = 17
        self.exit_width = 0
        self.myfont = pygame.font.SysFont('Comic Sans MS', 35)
        self.exit_button = self.myfont.render('X', False, (0, 0, 0))

        """Information about individual holes"""
        self.hole_color = pygame.Color(82, 54, 27)
        self.hole_width = 0

        self.row1_size = (60, 50)
        self.row1_x_hole_pos = 235
        self.row1_y_hole_pos = 535
                
        self.row2_size = (80, 70)
        self.row2_x_hole_pos = 195
        self.row2_y_hole_pos = 620

        self.row3_size = (100, 90)
        self.row3_x_hole_pos = 125
        self.row3_y_hole_pos = 730
        
        self.hole_list = self.generate_holes(5)

        """Information about individual groundhogs"""
        self.gh_color = pygame.Color(0, 0, 0)
        self.gh_width = 0
        self.gh_list = [0] * 15

    def generate_holes(self, n):
        holes_list = []

        for x in range(n):
            draw_h = Hole([self.row1_x_hole_pos] + [self.row1_y_hole_pos], self.row1_size, self.hole_color, self.hole_width)
            holes_list += [draw_h]
            self.row1_x_hole_pos += 115

        for x in range(n):
            draw_h2 = Hole([self.row2_x_hole_pos] + [self.row2_y_hole_pos], self.row2_size, self.hole_color, self.hole_width)
            holes_list += [draw_h2]
            self.row2_x_hole_pos += 130

        for x in range(n):
            draw_h3 = Hole([self.row3_x_hole_pos] + [self.row3_y_hole_pos], self.row3_size, self.hole_color, self.hole_width)
            holes_list += [draw_h3]
            self.row3_x_hole_pos += 160
    
        return holes_list

    def generate_groundhog(self):
        if 0 not in self.gh_list:
            return 

        while True:
            hole_choice = random.randint(0, len(self.hole_list) - 1)
            
            if self.gh_list[hole_choice] == 0:
                break
        
        individual_gh = Groundhog(self.hole_list[hole_choice], self.gh_color, self.gh_width)
        self.gh_list[hole_choice] = individual_gh

    def remove_groundhog(self, gh):
        self.gh_list[gh] = 0

wam = WAM()
wam.generate_groundhog()

def game_design(wam):
    """ Runs the essential game features necessary every time"""

    window.blit(wam.background, (0, 0))

    pygame.draw.circle(window, wam.exit_color2, wam.exit_pos, wam.exit_radius2, wam.exit_width)
    pygame.draw.circle(window, wam.exit_color, wam.exit_pos, wam.exit_radius, wam.exit_width)

    window.blit(wam.exit_button,(963, 19))

    for x in wam.hole_list:
        x.draw_hole()

    for x in wam.gh_list:
        if x != 0:
            img, pos = x.draw_gh()
            window.blit(img, pos)
            

while True:
    game_design(wam)




    pygame.display.flip()


