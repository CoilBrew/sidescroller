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
        if key[pygame.K_d]:
            player.move("right")
        elif key[pygame.K_a] and not(self.beginningOfWorld(player.world_scroll)):
            player.move("left")
        # collision
        for obst in obstacles:
            # This can only deal with one obstacle at a time atm
            if key[pygame.K_d]:
                if player.rect.colliderect(obst.rect) and player.collisionLeft == False:
                    player.collisionRight = True
                elif not(player.rect.colliderect(obst.rect)):
                    player.collisionRight = False
            if key[pygame.K_a]:
                if player.rect.colliderect(obst.rect) and player.collisionRight == False:
                    player.collisionLeft = True
                elif not(player.rect.colliderect(obst.rect)):
                    player.collisionLeft = False
            # jump
            if player.jumpDown and (self.inXColumn(player.rect, obst.rect)):
                if player.rect.bottom <= obst.rect.top:
                    player.jumpDown = False # stop jumping

            # gravity
            if not(self.inXColumn(player.rect, obst.rect)) and player.rect.bottom < player.floor:
                player.collisionRight = False
                player.collisionLeft= False
                player.jumpDown = True

        # jump
        if key[pygame.K_w] or key[pygame.K_SPACE]:
            player.jumpAttempt = True

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

    def inXColumn(self, rect1, rect2):
        if rect1.center[0] >= rect2.left and rect1.center[0] <= rect2.right:
            return True
        return False
