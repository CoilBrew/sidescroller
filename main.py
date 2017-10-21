#!/usr/bin/env python3
# Burrito Man
# By CoilBrew

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

def debug_statements(*dictionary):
    for d in dictionary:
        print(d["msg"] + ": " + str(d["args"]))

def main():
    # CONSTANTS
    level = 100
    LEFT = "left"
    RIGHT = "right"
    IMAGE_SIZE = 100

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

    event = Event(LEFT, RIGHT) # Initialise the event handler
#    wall = Wall(display, width, height) # Initialise the wall
    player = Player(
            STARTX,
            STARTY - IMAGE_SIZE, # This is to move the image above the floor
            LEFT,
            RIGHT
    ) # Initialise the player
    floor = Floor(
            display,
            level,
            width,
            height,
            floor_height
    )

    display.fill(BLACK)

    obstacle = Obstacle(
            display,
            width,
            height
    )

    # Game loop
    while True:
        display.fill(BLACK)
        event.update(
            pygame.event.get(),
            player
        )
        world_scroll = player.world_scroll

        display.blit(player.image, (player.x, player.y))  #After moving, reload the image at new position

        floor.draw()
        obstacle.draw(world_scroll)
        #wall.draw(world_scroll)
        player.jump_animation()

        # For now use:
        pygame.display.update()
        # Each frame call tick()
        clock.tick(60) # opt arg: limit framerate; otherwise, unlimited

        # Debugging
        print("\n###Debugging###")
        debug_statements(
            {"msg": "FPS", "args": round(clock.get_fps())},
            {"msg": "World scroll", "args": world_scroll},
        )

if __name__ == "__main__":
    main()
