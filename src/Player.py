import pygame
import time
from datetime import datetime, timedelta
from functools import wraps

class Player(object):
    """This defines the player"""
    def __init__(self, startx, starty): # Constructor method
        self.starty = starty
        self.x = startx
        self.y = starty

        self.image_height = 100
        self.image_length = 100
        self.velocity = 5# This modifies world scroll speed
        self.health = 100
        self.image = pygame.image.load('assets/burrito_man.png')

        """This will determine the position of everything else"""
        self.world_scroll = 0
        self.world_tower = 0

        self.jumpUp = False
        self.jumpDown = False
        self.jumpedHeight = 0
        self.jumpRateUp = 25
        self.jumpRateDown = 12
        self.jumpedMaxHeight = 150 # Jumps to maximum of 100 pixels

        self.elevatedPlatform = False

        self.rect = pygame.Rect(self.x, self.y, self.image_length, -self.image_height)

    def jump(self):
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
                self.y = self.y + self.jumpRateDown
                self.jumpedHeight = self.jumpedHeight - self.jumpRateDown
            else:
                self.jumpDown = False

    def updateVertices(self):
        """A rectangle is a polygon with four vertices"""
        v1 = (self.x, self.y)
        v2 = (self.x, self.y - self.image_height)
        v3 = (self.x + self.image_length, self.y - self.image_height)
        v4 = (self.x + self.image_length, self.y)
        self.vertices = {"bottom_left": v1, "top_left": v2, "top_right": v3, "bottom_right": v4}

