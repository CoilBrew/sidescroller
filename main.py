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
from src.Level import *
from src.Settings import *
from src.Floor import *
from src.Player import *
from src.Obstacle import *
from src.Timer import *

def debug_statements(*dictionary):
    for d in dictionary:
        print(d["msg"] + ": " + str(d["args"]))

def main():
    # CONSTANTS
    IMAGE_SIZE = 100
    settings = Settings() # Initialise settings object
    SCREEN_WIDTH, SCREEN_HEIGHT = settings.width, settings.height
    FLOOR_HEIGHT = SCREEN_HEIGHT * settings.floor_height_percentage
    PLAYER_START_X = 0.25 * SCREEN_WIDTH
    PLAYER_START_Y = FLOOR_HEIGHT

    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Burrito Man')

    event = Event() # Initialise the event handler
#    wall = Wall(display, SCREEN_WIDTH, SCREEN_HEIGHT) # Initialise the wall
    player = Player(
            PLAYER_START_X,
            PLAYER_START_Y,
            FLOOR_HEIGHT
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
    
    timer = Timer(display, GREEN, BLACK)

    # Generate obstacles with function in Level class
    obstacle_list = level.generateObstacles(obstacle_num=2)

    # Work out where the finish line should be (300px after last obstacle)
    end_coord = level.createEnd(obstacle_list)

    # Game loop
    while True:
        display.fill(BLACK)
        event.update(pygame.event.get(), player, obstacle_list)

        display.blit(player.image, player.rect) # draw player
        floor.draw()
    
        timer.render(100, 100)

        # draw all Obstacles in obstacle_list
        for obst in obstacle_list:
            # Draw the finish line as a vertical white line
            level.drawFinish(end_coord, player.world_scroll)
            obst.update(player.world_scroll)
            obst.draw()

        player.jump_animation()

        pygame.display.update()
        clock.tick(60) # opt arg: limit framerate; otherwise, unlimited

        print("\n###Debugging###")
        debug_statements(
            {"msg": "FPS", "args": round(clock.get_fps())},
            {"msg": "World scroll", "args": player.world_scroll},
            {"msg": "Distance to finish", "args": round(end_coord[0] - player.world_scroll - 250, 2)},
        )

if __name__ == "__main__":
    main()
