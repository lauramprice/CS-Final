
import random
import pygame
pygame.init()
pygame.font.init() 

window_size = [1000,900]
window = pygame.display.set_mode(window_size)

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

    def __init__(self, hole, bday, gh_color, gh_width):
        self.gh_pos = [int(hole.pos[0] + (hole.size[0] / 7)), int(hole.pos[1] - (hole.size[1] * .15))]
        self.gh_size = [int(hole.size[0] * 0.70), int(hole.size[1] * 0.90)]
        self.gh_color = gh_color
        self.gh_width = gh_width
        self.birthday = bday

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
        
        """ Score """
        self.score = 0

        """Window Buttons"""
        self.exit_color = pygame.Color(255, 51, 51)
        self.exit_color2 = pygame.Color(0, 0, 0)
        self.exit_pos = (970, 30)
        self.exit_radius = 15
        self.exit_radius2 = 17
        self.exit_width = 0
        self.myfont = pygame.font.SysFont('Comic Sans MS', 35)
        self.exit_button = self.myfont.render('X', False, (0, 0, 0))

        self.gc_color = pygame.Color(255, 255, 255)
        self.gc_color2 = pygame.Color(0, 0, 0)
        self.gc_pos = (75, 165)
        self.gc_pos2 = (70, 160)
        self.gc_size = (125, 80)
        self.gc_size2 = (135, 90)
        self.gc_width = 0
        self.screenfont = pygame.font.SysFont('Comic Sans MS', 45)
        self.gc_text = self.myfont.render('Timer:', False, (0, 0, 0))

        self.st_color = pygame.Color(255, 255, 255)
        self.st_color2 = pygame.Color(0, 0, 0)
        self.st_pos = (695, 165)
        self.st_pos2 = (690, 160)
        self.st_size = (125, 80)
        self.st_size2 = (135, 90)
        self.st_width = 0
        self.st_text = self.myfont.render('Score:', False, (0, 0, 0))
        self.st_score = self.screenfont.render(str(self.score), False, (0, 0, 0))

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
        self.gh_num = random.randint(4, 5)

        """ Timing """
        self.game_clock = pygame.time.Clock()
        self.elapsed_time = 0
        self.gh_onscreen = random.randint(1500, 2500)
        self.game_runtime = 30000
        self.gh_countdown = random.randint(1000, 3000)
        self.time_left = 30000

        """ End Screen"""
        self.end_color = pygame.Color(200, 200, 200)
        self.end_color2 = pygame.Color(0, 0, 0)
        self.end_pos = (270, 300)
        self.end_pos2 = (260, 290)
        self.end_size = (450, 300)
        self.end_size2 = (470, 320)
        self.end_width = 0
        self.score_font = pygame.font.SysFont('Comic Sans MS', 70)
        self.end_text = self.myfont.render('Congratulations! Your score is:', False, (0, 0, 0))
        self.end_text2 = self.myfont.render('Thanks for playing!', False, (0, 0, 0))

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

    def generate_groundhog(self, gh_num):
        
        for _ in range(gh_num):
            if 0 not in self.gh_list:
                return 

            while True:
                hole_choice = random.randint(0, len(self.hole_list) - 1)
            
                if self.gh_list[hole_choice] == 0:
                    break
        
            individual_gh = Groundhog(self.hole_list[hole_choice], self.elapsed_time, self.gh_color, self.gh_width)
            self.gh_list[hole_choice] = individual_gh

    def remove_groundhog(self, gh):
        self.gh_list[gh] = 0

    # called once per frame
    def timing(self, fps):
        self.game_clock.tick(fps)
        self.elapsed_time += self.game_clock.get_time()
        self.gh_countdown -= self.game_clock.get_time()
        self.time_left -= self.game_clock.get_time()

        for x in range(len(self.gh_list)):
            if isinstance(self.gh_list[x], Groundhog):
                if self.elapsed_time - self.gh_list[x].birthday > self.gh_onscreen:
                    
                    self.remove_groundhog(x)

        if self.gh_countdown <= 0:
            
            self.generate_groundhog(self.gh_num)
            self.gh_countdown = random.randint(1000, 2000)

        #print(self.elapsed_time)


        if self.elapsed_time >= self.game_runtime:
            for x in range(len(self.gh_list)):
                if isinstance(self.gh_list[x], Groundhog):
                    self.remove_groundhog(x)

            self.generate_endscreen()
    
    def generate_endscreen(self):
        window.blit(wam.background, (0, 0))

        pygame.draw.circle(window, wam.exit_color2, wam.exit_pos, wam.exit_radius2, wam.exit_width)
        pygame.draw.circle(window, wam.exit_color, wam.exit_pos, wam.exit_radius, wam.exit_width)
        window.blit(wam.exit_button,(963, 19))

        pygame.draw.rect(window, self.end_color2, (self.end_pos2, self.end_size2), self.end_width)
        pygame.draw.rect(window, self.end_color, (self.end_pos, self.end_size), self.end_width)
        end_score = self.score_font.render(str(self.score), False, (0, 0, 0))

        window.blit(self.end_text, (300, 350))
        window.blit(end_score, (455, 425))
        window.blit(self.end_text2, (380, 520))
        

wam = WAM()
wam.generate_groundhog(wam.gh_num)

def game_design(wam):
    """ Runs the essential game features necessary every time"""

    window.blit(wam.background, (0, 0))

    pygame.draw.rect(window, wam.gc_color2, (wam.gc_pos2, wam.gc_size2), wam.gc_width)
    pygame.draw.rect(window, wam.gc_color, (wam.gc_pos, wam.gc_size), wam.gc_width)
    window.blit(wam.gc_text,(85, 170))
    window.blit(wam.screenfont.render(str(wam.time_left // 1000), False, (0, 0, 0)),  (120, 205))

    pygame.draw.rect(window, wam.st_color2, (wam.st_pos2, wam.st_size2), wam.st_width)
    pygame.draw.rect(window, wam.st_color, (wam.st_pos, wam.st_size), wam.st_width)
    window.blit(wam.st_text,(705, 170))
    window.blit(wam.st_score, (735, 205))

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
    
    wam.timing(30)
    
    """event loop"""
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for x in range(len(wam.gh_list)):
                if isinstance(wam.gh_list[x], Groundhog):
                    rectangle = pygame.Rect(wam.gh_list[x].gh_pos, wam.gh_list[x].gh_size)
                    if rectangle.collidepoint(event.pos):
                        wam.score += 10
                        wam.st_score = wam.screenfont.render(str(wam.score), False, (0, 0, 0))
                        wam.remove_groundhog(x)
                        break

            circle = pygame.draw.circle(window, wam.exit_color2, wam.exit_pos, wam.exit_radius2, wam.exit_width)
            if event.pos in circle:
                pygame.quit()
                break


    pygame.display.flip()


