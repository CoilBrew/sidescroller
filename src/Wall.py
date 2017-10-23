import pygame
from random import randint
from src.colours import *

class Wall(pygame.sprite.Sprite):
    """This defines the wall"""
    def __init__(self, display, width, height):
        """
        velocity is the rate at which the wall moves to the right, in absolute terms
        """
        self.x = 0
        self.y = height * 0.75 # hard coded for now
        self.velocity = 0.10

        self.display = display
        self.width = width
        self.height = height
        self.bottom_left_location = (0, self.height * 0.75)
        self.colour = WALL_RED
        self.obstacle_height = 0
        self.obstacle_length = 100
        self.line_width = 1

        # A rectangle is a polygon with four vertices
        self.v1 = (self.x, self.y)
        self.v2 = (self.x, self.obstacle_height)
        self.v3 = (self.x + self.obstacle_length, self.obstacle_height)
        self.v4 = (self.x + self.obstacle_length, self.y)

    def draw(self, world_scroll):
        self.updateVertices(self.velocity, world_scroll)
        vertices = [self.v1, self.v2, self.v3, self.v4]
        pygame.draw.polygon(self.display, self.colour, vertices, self.line_width)

    def updateVertices(self, velocity, world_scroll):
        """A rectangle is a polygon with four vertices"""
        self.v1 = (self.v1[0] + velocity - world_scroll/2, self.v1[1]) 
        self.v2 = (self.v2[0] + velocity - world_scroll/2, self.v2[1]) 
        self.v3 = (self.v3[0] + velocity - world_scroll/2, self.v3[1]) 
        self.v4 = (self.v4[0] + velocity - world_scroll/2, self.v4[1]) 

