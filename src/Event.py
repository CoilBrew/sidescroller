import pygame, sys
from pygame.locals import *

class Event(object):
    """This is the event handler"""
    def __init__(self):
        pass

    def update(self, events, player):
        """Event loop"""
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            player.move("left")
        elif key[pygame.K_d]:
            player.move("right")
        elif key[pygame.K_w]:
            player.move("jump")
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
