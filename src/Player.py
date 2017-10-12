import pygame
class Player(object):
    """This defines the player"""
    def __init__(self, startx, starty): # Constructor method
        # create base_velocity
        # create health
        # create image/asset
        # Set the resolution settings
        self.x = startx
        self.y = starty

    def move(self, direction):
        """Takes a character representing the direction of movement"""
        key = pygame.key.get_pressed()
        if direction == "left":
            # move left
            self.x = self.x - 10  # moves left ten pixels
        elif direction == "right":
            # move right
            self.x = self.x + 10
        elif direction == "jump":
            self.y = self.y - 100
        # else:
        #     print("Error")
