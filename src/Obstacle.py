from random import randint, uniform
from src.colours import *
import pygame

class Obstacle(object):
    """ This is a class used to define a obstacle. """

    def __init__(self, display, width, height, floor_height_percentage):
        self.display = display
        # randfloat with uniform dist to give obstacles different x values
        self.x = width * uniform(0.75, 3.0) 
        self.y = height * floor_height_percentage
        self.colour = FLOOR_GREEN
        self.obstacle_height = randint(50, 150)
        self.obstacle_length = randint(50, 250)
        self.line_width = 1

        # use a negative integer here for length and height, in order to project the rects upward
        self.rect = pygame.Rect(self.x, self.y, self.obstacle_length, -self.obstacle_height)

    def draw(self):
        pygame.draw.rect(self.display, self.colour, self.rect, self.line_width)

    def update(self, world_scroll):
        x = self.x - world_scroll
        y = self.y
        self.rect = pygame.Rect(x, y, self.obstacle_length, -self.obstacle_height)

