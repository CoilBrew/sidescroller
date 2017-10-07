import pygame
from src.colours import *
from src.Universe import * 

class Floor(Universe):
    """This class defines the floor"""
    def __init__(self, display, level, width, floor_height):
        Universe.__init__(self, level)
        self.display = display # Takes a display argument and stores it internally
        self.colour = FLOOR_GREEN
        self.startpoint = 0
        #self.endpoint = self.levellength #inheritesd from the Universe class?    # The endpoint of the floor, where the level ends :: (Int, Int)
        self.begin = (0, floor_height)
        self.end = (width, floor_height)

    def draw(self):
        pygame.draw.line(self.display, self.colour, (self.begin), (self.end), 1) # start, end, width

    def segments(self):
        """Segments is a list of segments"""
        pass # TODO
