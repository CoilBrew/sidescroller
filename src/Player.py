import pygame
import time
from datetime import datetime, timedelta
from functools import wraps

class Player(object):
    """This defines the player"""
    def __init__(self, startx, starty, left, right): # Constructor method
        self.starty = starty
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
        self.jumpRateUp = 25
        self.jumpRateDown = 12
        self.jumpedMaxHeight = 150 # Jumps to maximum of 100 pixels

        self.elevatedPlatform = False

    def move(self, direction, obstacles):
        """Takes a character representing the direction of movement"""
        key = pygame.key.get_pressed()
        if direction == self.left and not(self.collideObstacleLeft(obstacles)):
            self.world_scroll = self.world_scroll - self.velocity
        elif direction == self.right and not(self.collideObstacleRight(obstacles)):
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

    def putOnObstacleFloor(self, obstacles):
        yes = False
        for obst in obstacles:
            if self.vertices["bottom_right"][0] - 50 > obst.vertices["bottom_left"][0] and self.vertices["bottom_right"][0] < obst.vertices["bottom_right"][0] and self.vertices["bottom_left"][1] <= obst.vertices["bottom_left"][1]:
                self.elevatedPlatform = obst
                yes = True
            elif self.vertices["bottom_left"][0] + 50 > obst.vertices["bottom_left"][0] and self.vertices["bottom_left"][0] < obst.vertices["bottom_right"][0] and self.vertices["bottom_left"][1] <= obst.vertices["bottom_left"][1]:
                self.elevatedPlatform = obst
                yes = True
        if not(yes):
            self.elevatedPlatform = False

    def raiseToFloor(self):
        if self.jumpUp or self.jumpDown:
            return False
        elif self.elevatedPlatform:
            self.y = self.elevatedPlatform.vertices["top_left"][1] - self.image_height
            return True
        else: 
            self.y = self.starty
            return False

    def collideObstacleRight(self, obstacles):
        for obst in obstacles:
            if self.vertices["bottom_right"][0] >= obst.vertices["bottom_left"][0] and self.vertices["bottom_left"][0] < obst.vertices["bottom_left"][0] and self.vertices["bottom_right"][1] > obst.vertices["top_right"][1]:
                return True
        return False

    def collideObstacleLeft(self, obstacles):
        for obst in obstacles:
            if self.vertices["bottom_left"][0] <= obst.vertices["bottom_right"][0] and self.vertices["bottom_right"][0] > obst.vertices["bottom_right"][0] and self.vertices["bottom_left"][1] > obst.vertices["top_left"][1]:
                return True
        return False
