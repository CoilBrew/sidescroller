import pygame, sys
from pygame.locals import *

class Physics(object):
    """This class handles the physics of the game (i.e. collisions, gravity, jumping)"""
    def __init__(self):
        self.gravity_a = 9 # acceleration of gravity (in m/s)

    def calculate_vertical_acceleration(self, obj, floor):
        """Work out the vertical pull on any object"""
        if self.on_obj(obj, floor):
            # If obj is touching the floor
            return self.gravity_a - floor.vertical_a - obj.vertical_a
        # Otherwise assume in free-fall
        # g - obj_a, 
        #   we are taking objs acceleration away from gravity because they are heading in different directions
        return self.gravity_a - obj.vertical_a

    def on_obj(self, obj, target):
        """Work out if obj bottom is >= than target object
        top; otherwise we assume player is in free-fall
        (i.e. there is nothing beneath it)"""
        if obj.rect.bottom >= target.rect.top:
            return True
        return False

    def calculate_vertical_velocity(self, obj, floor):
        """Calculate vertical velocity of object"""
        # We add the acceleration of gravity on the object to its vertical velocity
        if obj.jumpAttempt is True:
            # v = obj_v + a - j
            return obj.vertical_velocity + self.calculate_vertical_acceleration(obj, floor) - obj.jump_potential
        
        if self.on_obj(obj, floor):
            # If touching floor, dissipate velocity
            return 0
        
        return obj.vertical_velocity + self.calculate_vertical_acceleration(obj, floor)

