#!/usr/bin/env python3
import pygame, sys, json
from pygame.locals import *
from src.Event import *
from random import randint

class BurritoMan(pygame.sprite.Sprite):
    def __init__(self): #Constructor
        self.image = pygame.image.load('assets/burrito.bmp')
        self.x = startx
        self.y = starty

    def handle_keys(self): #Method to handle key presses
        key = pygame.key.get_pressed()
        dist = 10
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist

    def draw(self, surface):
        # blit on the display
        surface.blit(self.image, (self.x, self.y))

pygame.init()

info = pygame.display.Info()
clock = pygame.time.Clock()

# Settings
settings = json.load(open("./settings.json"))
FPS = settings["FPS"]

# Set the resolution settings
if settings["resolution"]["dynamic"] == True:
    width = info.current_w # Width is the width of the screen
    height = int((info.current_h / 2)) # Height is the screen height divided by 2
else:
    width = settings["resolution"]["width"] # Width is the width of the screen
    height = settings["resolution"]["height"] # Height is the screen height divided by 2

display = pygame.display.set_mode((width, height))

# Below can be moved/deleted if neccessary; just wanted something to appear on screen
# This is the floor going the full width of the screen 20% of the way up the screen, (100,244,66) is RGB colour
pygame.draw.rect(display, (100, 244, 66), (0, 0.8*height, width, 5))

#Starting dimension
startx = 0.5*width #Starting location is in the middle (x axis)
starty = 0.75*height #Starting location is 25% up from bottom

burritoman = BurritoMan() #New instance of burittoMan()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    burritoman.handle_keys()
    burritoman.draw(display)
    pygame.display.flip()
    clock.tick(FPS)
