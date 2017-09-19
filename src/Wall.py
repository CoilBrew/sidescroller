import pygame

class Wall(pygame.sprite.Sprite):
    """This defines the wall"""
    def __init__(self, display):
        """
        abs_pos is position not relative to camera, but entire universe
        velocity is the rate at which the wall moves to the right, in absolute terms
        """
        self.abs_pos = 0
        self.velocity = 5
        self.display = display

    def move(self):
        """Update the wall's absolute position"""
        self.abs_pos += self.velocity
