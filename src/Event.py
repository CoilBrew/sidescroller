import pygame, sys
from pygame.locals import *

class Event(object):
    """This is the event handler"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def update(self, events, player):
        """Event loop"""
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_SPACE]:
            player.move("jump")
        elif key[pygame.K_a]:
            player.move(self.left)
        elif key[pygame.K_d]:
            player.move(self.right)
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def overlap(self, lst):
        """Returns all of the objects that overlap on the screen and the co-ordinates that overlap"""
        # lst is a list of objects
        pass
