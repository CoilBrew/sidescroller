import pygame
class Player(object):
    """This defines the player"""
    def __init__(self, startx): # Constructor method
        # create base_velocity
        # create health
        # create image/asset
        # Set the resolution settings
        self.position = startx

    def move(self):
        """Takes a character representing the direction of movement"""
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            # move left
            self.position = self.position - 10  # moves left ten pixels
        elif key[pygame.K_RIGHT]:
            # move right
            self.position = self.position + 10
        # elif direction = "u":
        #     # move up
        # else:
        #     print("Error")
