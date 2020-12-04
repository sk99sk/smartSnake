import parameters
import pygame
class board:
    def __init__(self,width=parameters.board_width,height=parameters.board_height,color=parameters.board_color,block_size=parameters.snake_width,wall_color=parameters.wall_color):
        self.width = width
        self.height = height
        self.color = color
        self.block_size = block_size
        self.wall_color = wall_color
    def board_draw(self,screen):
        screen.fill(self.color)
        #building horizontal walls
        for x in range(0, self.width, self.block_size):
            y = 0
            pygame.draw.rect(screen, self.wall_color, (x, y, self.block_size, self.block_size), 1)
            pygame.draw.rect(screen, self.wall_color, (x+3, y+3, self.block_size-6, self.block_size-6))
            y = self.height - self.block_size
            pygame.draw.rect(screen, self.wall_color, (x, y, self.block_size, self.block_size), 1)
            pygame.draw.rect(screen, self.wall_color, (x+3, y+3, self.block_size-6, self.block_size-6))
        # building the vertical walls
        for y in range(self.block_size, self.height-self.block_size, self.block_size):
            x = 0
            pygame.draw.rect(screen, self.wall_color, (x, y, self.block_size, self.block_size), 1)
            pygame.draw.rect(screen, self.wall_color, (x+3, y+3, self.block_size-6, self.block_size-6))
            x = self.width - self.block_size
            pygame.draw.rect(screen, self.wall_color, (x, y, self.block_size, self.block_size), 1)
            pygame.draw.rect(screen, self.wall_color, (x+3, y+3, self.block_size-6, self.block_size-6))
        return screen
    
