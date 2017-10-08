import pygame
from random import randint
from src.colours import *

class Wall(pygame.sprite.Sprite):
    """This defines the wall"""
    def __init__(self, display, width, height):
        """
        abs_pos is position not relative to camera, but entire universe
        velocity is the rate at which the wall moves to the right, in absolute terms
        """
        self.abs_pos = 0
        self.velocity = 0.10
        self.display = display
        self.width = width
        self.height = height
        self.bottom_left_location = (0, self.height * 0.75)
        self.colour = WALL_RED
        self.obstacle_height = 0
        self.obstacle_length = 100
        self.line_width = 1

        # A rectangle is a polygon with four sides and four vertices
        self.v1 = (0, self.height * 0.75)
        self.v2 = (0, self.obstacle_height)
        self.v3 = (0 + self.obstacle_length, self.obstacle_height)
        self.v4 = (0 + self.obstacle_length, self.height * 0.75)

    def move(self):
        """Update the wall's absolute position"""
        self.abs_pos += self.velocity
    
    def draw(self):
        vertices = [self.v1, self.v2, self.v3, self.v4]
        pygame.draw.polygon(self.display, self.colour, vertices, self.line_width)
        self.moveVerticesRight()

    def moveVerticesRight(self):
        """We are only going to move the wall to the right (along the x-axis, so the y-values will stay the same)
        We then construct a new tuple based on the old with the modified x-axis value
        """
        self.v1 = (self.v1[0] + self.velocity, self.v1[1]) 
        self.v2 = (self.v2[0] + self.velocity, self.v2[1]) 
        self.v3 = (self.v3[0] + self.velocity, self.v3[1]) 
        self.v4 = (self.v4[0] + self.velocity, self.v4[1]) 

