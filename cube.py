import parameters
import pygame
class cube(object):
    def __init__(self,pos,color,dir_x=1,dir_y=0,eyes=False):
        self.pos = pos
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.color = color
        self.eyes = eyes
    def draw(self,win):
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(win,self.color,(i*parameters.snake_width,j*parameters.snake_width,parameters.snake_width , parameters.snake_width),border_radius=parameters.snake_width//3)
        if self.eyes:
            centre = parameters.snake_width//2
            radius = 3
            circleMiddle = (i*parameters.snake_width+centre-radius,j*parameters.snake_width+8)
            circleMiddle2 = (i*parameters.snake_width + parameters.snake_width -radius*2, j*parameters.snake_width+8)
            pygame.draw.circle(win, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(win, (0,0,0), circleMiddle2, radius)
        return win
		
    def move(self,dir_x,dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0]+self.dir_x,self.pos[1]+self.dir_y)