from random import randint
from src.colours import *
import pygame

class Obstacle(object):
    def __init__(self, display, width, height):
        self.display = display
        self.x = width
        self.y = height
        self.colour = FLOOR_GREEN
        self.obstacle_height = randint(50, 250)
        self.obstacle_length = randint(50, 250)
        self.bottom_left_location = (self.x * 0.75, self.y * 0.75) # It starts here
        self.line_width = 1

    def draw(self, world_scroll=0):
        # Hard-coded percent for now
        self.updateVertices(world_scroll)
        vertices = [self.v1, self.v2, self.v3, self.v4]
        pygame.draw.polygon(self.display, self.colour, vertices, self.line_width)
    
    def updateVertices(self, world_scroll):
        """A rectangle is a polygon with four vertices"""
        self.v1 = (self.x - world_scroll, self.y)
        self.v2 = (self.x - world_scroll, self.y - self.obstacle_height)
        self.v3 = (self.x + self.obstacle_length - world_scroll, self.y - self.obstacle_height)
        self.v4 = (self.x + self.obstacle_length - world_scroll, self.y)
