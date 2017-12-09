import pygame, sys
from pygame.locals import *

class Physics(object):
    """This class handles the physics of the game (i.e. collisions, gravity, jumping)"""
    def __init__(self):
        self.gravity_a = 9 # acceleration of gravity (in m/s)

    def calculate_gravitional_a(self, obj, floor):
        """Work out the gravitational pull on any object"""
        if self.on_floor(obj, floor):
            # If obj is touching the floor
            return self.gravity_a - floor.vertical_a - obj.vertical_a
        # Otherwise assume in free-fall
        return self.gravity_a - obj.vertical_a

    def on_floor(self, obj, floor):
        """Work out if obj bottom is >= to floor top
        otherwise we assume player is in free-fall"""
        if obj.rect.bottom >= floor.rect.top:
            return True
        return False

    def calculate_v(self, obj, floor):
        """Calculate velocity of object"""
        if self.on_floor(obj, floor):
            # If touching floor, dissipate velocity
            return 0
        # Otherwise assume Newtonian mechanics are working as expected
        # and we add the acceleration of gravity on the object to its vertical velocity
        return obj.vertical_velocity + self.calculate_gravitional_a(obj, floor)
