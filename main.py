#!/usr/bin/env python3

import pygame
import src.Floor

pygame.init()

info = pygame.display.Info()

width = info.current_w
height = int((info.current_h / 2))

print(int(6.7/2))

print ((width,height))
print (width,height)

display = pygame.display.set_mode((width, height))

while True:
    pygame.display.update()
