import pygame
from random import randint
from src.colours import *
from src.Level import *

class Floor(Level):
    """This class defines the floor"""

    def __init__(self, display, width, height, floor_height):
        self.display = display # Takes a display argument and stores it internally
        self.colour = FLOOR_GREEN
        self.startpoint = 0
        self.floor_height = floor_height
        self.width = width
        self.height = height
        #self.endpoint = self.levellength #inheritesd from the Level class?    # The endpoint of the floor, where the level ends :: (Int, Int)
        self.begin = (0, floor_height)
        self.end = (width, floor_height)

    def draw(self):
        line_width = 1 # Pixel
        pygame.draw.line(self.display, self.colour, (self.begin), (self.end), line_width) # start, end, width

    def segments(self):
        """Segments is a list of segments"""
        pass # TODO
