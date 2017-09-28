#!/usr/bin/env python3
import pygame, sys, json
from pygame.locals import *
# Misc
from random import randint
from colours import *
# Classes
from src.Event import *
from src.Wall import *
from src.Universe import *
#from src.Floor import *
from src.Player import *

def main():
    pygame.init()
    INFO = pygame.display.Info()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Burrito Man')

    # Settings
    settings = json.load(open("./settings.json"))
    FPS = settings["FPS"]

    # Set the resolution settings
    if settings["resolution"]["dynamic"] == True:
        WIDTH = INFO.current_w # Width is the width of the screen
        HEIGHT = int((INFO.current_h / 2)) # Height is the screen height divided by 2
    else:
        WIDTH = settings["resolution"]["width"] # Width is the width of the screen
        HEIGHT = settings["resolution"]["height"] # Height is the screen height divided by 2

    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

    STARTX = 0.5*WIDTH #Starting location is in the middle (x axis)
    STARTY = 0.75*HEIGHT #Starting location is 25% up from bottom
    burritoMan = pygame.image.load('assets/burrito.bmp') #Assign the character image to burritoMan
    DISPLAY.blit(burritoMan, (STARTX, STARTY)) #Display burritoman at the starting co-ordinates

    event = Event() # Initialise the event handler
    wall = Wall(DISPLAY) # Initialise the wall
    player = Player(STARTX) # Initialise the player

    # Below can be moved/deleted if neccessary; just wanted something to appear on screen
    # This is the floor going the full width of the screen 20% of the way up the screen, (100,244,66) is RGB colour
    pygame.draw.rect(DISPLAY, (100, 244, 66), (0, 0.8*HEIGHT, WIDTH, 5))

    # This is the list of objects that will be updated on frame redraw, initalise it here
    seqUpdate = pygame.sprite.RenderUpdates()

    DISPLAY.fill(BLACK)

    # Create groups
    #a = pygame.Sprite.Group()
    # Assign to groups
    #Player.containers = a

    # Game loop
    while True:
        # For everything in the RenderUpdates group (seqUpdate):
        #   1. Erase all sprites with cover
        #   2. Redraw them
        cover = (0, 0, 0)
        seqUpdate.clear(DISPLAY, cover)
        seqUpdate.draw(DISPLAY)

        event.update(pygame.event.get())

        #This bit below is really bad, need to get rid of the old image rather than just loading it again
        DISPLAY.blit(burritoMan, (STARTX, STARTY))  #After moving, reload the image at new position

        rect_list = seqUpdate.draw(DISPLAY) # This returns a rect_list to be passed into update()
        # Update the screen
        # This one won't work until our classes are subclasses of Sprite classes
        #pygame.display.update(rect_list) # We will want to pass only those things that change into this method
        # For now use:
        pygame.display.update()
        # Each frame call tick()
        clock.tick() # You can pass a framerate to tick(), limiting the game to that framework
        # If you want unlimited frames, then pass nothing in

        wall.move()
        player.move()
        # Debugging
        print("\n###Debugging###")
        print("Wall position: " + str(wall.abs_pos))
        print("FPS: ", round(clock.get_fps(), 2))
        print("Player position: " + str(player.position))

if __name__ == "__main__":
    main()
