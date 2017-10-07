from random import randint
from src.colours import *
import pygame

class Obstacle(object):
    def __init__(self, display, width, height):
        self.display = display
        self.width = width
        self.height = height
        self.colour = FLOOR_GREEN
        self.obstacle_height = randint(50, 250)
        self.obstacle_length = randint(50, 250)
        self.bottom_left_location = (self.width * 0.75, self.height * 0.75) # It starts here
        self.line_width = 1

    def draw(self):
        # Hard-coded percent for now
        vertices = [
                self.bottom_left_location, 
                (self.width * 0.75, self.height * 0.75 - self.obstacle_height),
                (self.width * 0.75 - self.obstacle_length, self.height * 0.75 - self.obstacle_height),
                (self.width * 0.75 - self.obstacle_length, self.height * 0.75)
        ]
        pygame.draw.polygon(self.display, self.colour, vertices, self.line_width)
