import pygame
import time
from datetime import datetime, timedelta
from functools import wraps

class Player(object):
    """This defines the player"""
    def __init__(self, startx, starty, floor_height): # Constructor method
        self.starty = starty
        self.image_height = 100
        self.image_length = 100
        self.width = 20
        self.height = 20
        
        self.x = startx
        # We want the top left position to be the floor height
        # plus the height of the player
        self.y = starty - self.height 
        self.floor = floor_height

        self.velocity = 5# This modifies world scroll speed
        self.health = 100 # NOT USED
        self.image = pygame.image.load('assets/burrito_man.png') # NOT USED

        """This will determine the position of everything else"""
        self.world_scroll = 0

        self.jumpUp = False
        self.jumpDown = False
        self.jumpedHeight = 0
        self.jumpRateUp = 25
        self.jumpRateDown = 12
        self.jumpedMaxHeight = 150 # Jumps to maximum of 150 pixels

        self.elevatedPlatform = False
        self.collisionLeft = False
        self.collisionRight = False
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
#        self.rect = pygame.Rect(self.x, self.y, self.image_length, self.image_height)

    def move(self, direction):
        if direction == "left" and not(self.collisionLeft):
            self.world_scroll = self.world_scroll - self.velocity
        elif direction == "right" and not(self.collisionRight):
            self.world_scroll = self.world_scroll + self.velocity

    def jump(self):
        if self.jumpDown is False:
            self.jumpUp = True

    def jump_animation(self):
        """Manages jump animation"""
        if self.rect.bottom >= self.floor:
            # Do not let the player fall through the floor
            self.jumpDown = False

        if self.jumpUp is True:
            if self.jumpedHeight <= self.jumpedMaxHeight:
                self.y = self.y - self.jumpRateUp
                self.jumpedHeight = self.jumpedHeight + self.jumpRateUp
            else:
                self.jumpUp = False
                self.jumpDown = True
        elif self.jumpDown is True:
            if self.jumpedHeight > 0:
                self.y = self.y + self.jumpRateDown
                self.jumpedHeight = self.jumpedHeight - self.jumpRateDown
            else:
                self.jumpDown = False
        self.rect.y = self.y
