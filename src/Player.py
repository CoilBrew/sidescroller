import pygame
import time
from datetime import datetime, timedelta
from functools import wraps

class Player(object):
    """This defines the player"""
    def __init__(self, startx, starty, left, right): # Constructor method
        self.x = startx
        self.y = starty
        self.left = left
        self.right = right

        self.image_height = 100
        self.image_length = 100
        self.velocity = 5# This modifies world scroll speed
        self.health = 100
        self.image = pygame.image.load('assets/burrito_man.png')

        """This will determine the position of everything else"""
        self.world_scroll = 0

        self.jumpUp = False
        self.jumpDown = False
        self.jumpedHeight = 0
        self.jumpRateUp = 100
        self.jumpRateDown = 10
        self.jumpedMaxHeight = 1000 # Jumps to maximum of 100 pixels

    def move(self, direction):
        """Takes a character representing the direction of movement"""
        key = pygame.key.get_pressed()
        if direction == self.left:
            self.world_scroll = self.world_scroll - self.velocity
        elif direction == self.right:
            self.world_scroll = self.world_scroll + self.velocity
        elif direction == "jump":
            if self.jumpDown == False:
                self.jumpUp = True

    def jump_animation(self):
        """Manages jump animation"""
        if self.jumpUp == True:
            if self.jumpedHeight <= self.jumpedMaxHeight:
                self.y = self.y - self.jumpRateUp
                self.jumpedHeight = self.jumpedHeight + self.jumpRateUp
            else:
                self.jumpUp = False
                self.jumpDown = True
        elif self.jumpDown == True:
            if self.jumpedHeight > 0:
                self.y = self.y + self.jumpRateUp
                self.jumpedHeight = self.jumpedHeight - self.jumpRateDown
            else:
                self.jumpDown = False

    def updateVertices(self):
        """A rectangle is a polygon with four vertices"""
        self.v1 = (self.x, self.y)
        self.v2 = (self.x, self.y - self.image_height)
        self.v3 = (self.x + self.image_length, self.y - self.image_height)
        self.v4 = (self.x + self.image_length, self.y)
