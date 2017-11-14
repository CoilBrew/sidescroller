import pygame, sys
from pygame.locals import *

class Event(object):
    """This is the event handler"""
    def __init__(self):
        pass

    def update(self, events, player, obstacles):
        """Event loop"""
        key = pygame.key.get_pressed()
        # move
        print(player.collisionRight)
        if key[pygame.K_d]:
            player.move("right")
        elif key[pygame.K_a] and not(self.beginningOfWorld(player.world_scroll)):
            player.move("left")
        # collision
        for obst in obstacles:
            print(obst.rect)
            print(player.rect)
            if key[pygame.K_d]:
                if player.rect.colliderect(obst.rect) and player.collisionLeft == False:
                    player.collisionRight = True
                elif not(player.rect.colliderect(obst.rect)):
                    player.collisionRight = False
            elif key[pygame.K_a]:
                if player.rect.colliderect(obst.rect) and player.collisionRight == False:
                    player.collisionLeft = True
                elif not(player.rect.colliderect(obst.rect)):
                    player.collisionLeft = False

        # jump
        if key[pygame.K_w] or key[pygame.K_SPACE]:
            player.jump()
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
