#!/usr/bin/env python3
import pygame, sys, json
#import src.Floor
from pygame.locals import *

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

    # Game loop
    while True:
        # Event loop
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
