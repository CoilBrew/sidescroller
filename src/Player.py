import pygame
class Player(object):
    """This defines the player"""
    def __init__(self, startx, starty): # Constructor method
        self.x = startx
        self.y = starty
        self.velocity = 10
        self.health = 100
        self.image = pygame.image.load('assets/burrito_man.png')

    def move(self, direction):
        """Takes a character representing the direction of movement"""
        key = pygame.key.get_pressed()
        if direction == "left":
            self.x = self.x - self.velocity
        elif direction == "right":
            self.x = self.x + self.velocity
        elif direction == "jump":
            self.y = self.y - 100
        # else:
        #     print("Error")
