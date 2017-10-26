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
        self.obstacle_height = randint(50, 250)
        self.obstacle_length = randint(50, 250)
        self.line_width = 1

    def draw(self, world_scroll=0):
        self.updateVertices(world_scroll)
        vertices = [self.v1, self.v2, self.v3, self.v4]
        pygame.draw.polygon(self.display, self.colour, vertices, self.line_width)

    def updateVertices(self, world_scroll):
        """A rectangle is a polygon with four vertices"""
        self.v1 = (self.x - world_scroll, self.y)
        self.v2 = (self.x - world_scroll, self.y - self.obstacle_height)
        self.v3 = (self.x + self.obstacle_length - world_scroll, self.y - self.obstacle_height)
        self.v4 = (self.x + self.obstacle_length - world_scroll, self.y)
