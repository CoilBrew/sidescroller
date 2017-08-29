#!/usr/bin/env python3
import pygame, sys
import src.Floor
from pygame.locals import *

pygame.init()
info = pygame.display.Info()
width = info.current_w # Width is the width of the screen
height = int((info.current_h / 2)) # Height is the screen height divided byß 2

display = pygame.display.set_mode((width, height))

FPS = 60

# Game loop
while True:
    # Event loop
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
