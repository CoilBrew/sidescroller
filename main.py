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
from src.Physics import *

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
    player = Player(PLAYER_START_X, PLAYER_START_Y, FLOOR_HEIGHT) # Initialise the player
    floor = Floor(
            display,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            FLOOR_HEIGHT
    )
    physics = Physics()
    level = Level(
            display,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            settings.floor_height_percentage
    )
    
    timer = Timer(display, GREEN, BLACK)
    
    display.fill(BLACK)

    # Generate obstacles 
    obstacle_list = level.generateObstacles(obstacle_num=4)
    # Work out where the finish line should be (300px after last obstacle)
    end_coord = level.createEnd(obstacle_list)

    # Game loop
    while True:
        display.fill(BLACK)
        event.update(pygame.event.get(), player, obstacle_list)

        pygame.draw.rect(display, RED, player.rect)
#        display.blit(player.image, player.rect) # draw player
        floor.draw()
    
        timer.render(100, 100)

        # draw all Obstacles in obstacle_list
        for obst in obstacle_list:
            # Draw the finish line as a vertical white line
            level.drawFinish(end_coord, player.world_scroll)
            obst.update(player.world_scroll)
            obst.draw()

        player.vertical_a = physics.calculate_vertical_acceleration(player, floor)
        player.vertical_velocity = physics.calculate_vertical_velocity(player, floor)

        # Update player y position
        player.rect.y = player.y + player.vertical_velocity
        if player.jumpAttempt is True:
            player.jump()

#        player.jump_animation()

        pygame.display.update()
        clock.tick(60) # opt arg: limit framerate; otherwise, unlimited

        print("\n###Debugging###")
        debug_statements(
            {"msg": "FPS", "args": round(clock.get_fps())},
            {"msg": "World scroll", "args": player.world_scroll},
            {"msg": "Distance to finish", "args": round(end_coord[0] - player.world_scroll - 250, 2)},
            {"msg": "Player touching floor", "args": physics.on_obj(player, floor)},
            {"msg": "Vertical acceleration of player", "args": round(player.vertical_a, 2)},
            {"msg": "Vertical velocity of player", "args": round(player.vertical_velocity, 2)},
        )

if __name__ == "__main__":
    main()
