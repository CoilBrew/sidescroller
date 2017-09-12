import pygame, sys
from pygame.locals import * 

class Event(object):
    """This is the event handler"""
    def __init__(self):
        pass

    def update(self, events):
        """Event loop"""
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
