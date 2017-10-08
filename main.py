#!/usr/bin/env python3
import pygame, sys, json
from pygame.locals import *
# Misc
from random import randint
from src.colours import *
# Classes
from src.Event import *
from src.Wall import *
from src.Universe import *
from src.Settings import *
from src.Floor import *
from src.Player import *
from src.Obstacle import *

def debug_statement(msg, args):
    print(msg + ": " + str(args))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Burrito Man')

    # Settings
    settings = Settings()
    width, height = settings.width, settings.height
    floor_height = height * settings.floor_height_percentage

    display = pygame.display.set_mode((width, height))

    STARTX = 0.5 * width #Starting location is in the middle (x axis)
    STARTY = 0.75 * height #Starting location is 25% up from bottom
    burritoMan = pygame.image.load('assets/burrito.bmp') #Assign the character image to burritoMan

    event = Event() # Initialise the event handler
    wall = Wall(display) # Initialise the wall
    player = Player(STARTX) # Initialise the player
    level = 100
    floor = Floor(display, level, width, height, floor_height) 

    # This is the list of objects that will be updated on frame redraw, initalise it here
    seqUpdate = pygame.sprite.RenderUpdates()

    display.fill(BLACK)

    # Create groups: a = pygame.Sprite.Group()
    # Assign to groups: Player.containers = a
    obstacle = Obstacle(display, width, height)
    # Game loop
    while True:
        # For everything in the RenderUpdates group (seqUpdate):
        #   1. Erase all sprites with color; 2. Redraw them
        seqUpdate.clear(display, BLACK)
        rect_list = seqUpdate.draw(display) # This returns a rect_list to be passed into update()

        event.update(pygame.event.get())

        #This bit below is really bad, need to get rid of the old image rather than just loading it again
        display.blit(burritoMan, (STARTX, STARTY))  #After moving, reload the image at new position

        wall.move()
        player.move()
        floor.draw()
        obstacle.draw()

        # This one won't work until our classes are subclasses of Sprite classes
        #pygame.display.update(rect_list) # We will want to pass only those things that change into this method
        # For now use:
        pygame.display.update()
        # Each frame call tick()
        clock.tick() # opt arg: limit framerate; otherwise, unlimited
        
        # Debugging
        print("\n###Debugging###")
        debug_statement("FPS", round(clock.get_fps()))
        debug_statement("Wall position", wall.abs_pos)
        debug_statement("Player position", player.position)

if __name__ == "__main__":
    main()
