#!/usr/bin/env python3
import pygame, sys, json
from pygame.locals import *
from src.Event import *

def main():
    pygame.init()
    INFO = pygame.display.Info()

    # Settings
    settings = json.load(open("./settings.json"))
    FPS = settings["FPS"]

    # Set the resolution settings
    if settings["resolution"] == "dynamic":
        WIDTH = INFO.current_w # Width is the width of the screen
        HEIGHT = int((INFO.current_h / 2)) # Height is the screen height divided by 2
    else:
        WIDTH = settings["resolution"]["width"] # Width is the width of the screen
        HEIGHT = settings["resolution"]["height"] # Height is the screen height divided by 2

    display = pygame.display.set_mode((WIDTH, HEIGHT))

    event = Event() # Initialise the event handler

    # Game loop
    while True:
        event.update(pygame.event.get())
        
        # Update the screen
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
