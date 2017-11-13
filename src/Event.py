import pygame, sys
from pygame.locals import *

class Event(object):
    """This is the event handler"""
    def __init__(self):
        pass

    def update(self, events, player, obstacles):
        """Event loop"""
        key = pygame.key.get_pressed()
        for obst in obstacles:
            print(obst.rect)
            print(player.rect)
            if player.rect.colliderect(obst.rect):
                print("COLLISION")
                if key[pygame.K_d]:
                    player.rect.right = obst.rect.left
                    return 0
                elif key[pygame.K_a]:
                    player.rect.left = obst.rect.right
                    return 0
        if key[pygame.K_w] or key[pygame.K_SPACE]:
            player.jump()
        elif key[pygame.K_a]:
            if not(self.beginningOfWorld(player.world_scroll)):
                player.world_scroll = player.world_scroll - player.velocity
        elif key[pygame.K_d]:
            player.world_scroll = player.world_scroll + player.velocity
        # Exit
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

    def beginningOfWorld(self, world_scroll):
        """If the player is at point 0 of the world,
        then return true"""
        return world_scroll <= 0

    def gameOver(self):
        pass
