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
from src.Level import *
from src.Settings import *
from src.Floor import *
from src.Player import *
from src.Obstacle import *

def debug_statements(*dictionary):
    for d in dictionary:
        print(d["msg"] + ": " + str(d["args"]))

def main():
    # CONSTANTS
    LEFT = "left"
    RIGHT = "right"
    IMAGE_SIZE = 100
    settings = Settings() # Initialise settings object
    SCREEN_WIDTH, SCREEN_HEIGHT = settings.width, settings.height
    FLOOR_HEIGHT = SCREEN_HEIGHT * settings.floor_height_percentage
    PLAYER_START_X = 0.25 * SCREEN_WIDTH
    PLAYER_START_Y = settings.floor_height_percentage * SCREEN_HEIGHT - 3

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Burrito Man')

    event = Event(LEFT, RIGHT) # Initialise the event handler
#    wall = Wall(display, SCREEN_WIDTH, SCREEN_HEIGHT) # Initialise the wall
    player = Player(
            PLAYER_START_X,
            PLAYER_START_Y - IMAGE_SIZE, # This is to move the image above the floor
            LEFT,
            RIGHT
    ) # Initialise the player
    floor = Floor(
            display,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            FLOOR_HEIGHT
    )

    display.fill(BLACK)

    level = Level(
            display,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            settings.floor_height_percentage
    )

    # Generate obstacles with function in Level class
    obstacle_list = level.generateObstacles(obstacle_num=10)

    # Game loop
    while True:
        display.fill(BLACK)
        player.updateVertices()
        event.update(pygame.event.get(), player, obstacle_list)
        world_scroll = player.world_scroll

        display.blit(player.image, (player.x, player.y))  #After moving, reload the image at new position

        floor.draw()
        
        # draw all Obstacles in obstacle_list
        for obst in obstacle_list:
            obst.draw(world_scroll)

        player.putOnObstacleFloor(obstacle_list)
        player.raiseToFloor()

        #wall.draw(world_scroll)
        player.jump_animation()

        pygame.display.update()
        clock.tick(60) # opt arg: limit framerate; otherwise, unlimited

        print("\n###Debugging###")
        debug_statements(
            {"msg": "FPS", "args": round(clock.get_fps())},
            {"msg": "World scroll", "args": world_scroll},
        )

if __name__ == "__main__":
    main()
