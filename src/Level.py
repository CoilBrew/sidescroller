from src.Obstacle import *

class Level(object):
    """ This is a class used to define a level. """

    def __init__(self, display, width, height, floor_height_percentage):
        self.display = display
        self.width = width
        self.height = height
        self.floor_height_percentage = floor_height_percentage


# Here we want to store a list of Obstacles.

# Generate obstacles method.
    def generateObstacles(self, obstacle_num=10):
        obstacle_list = []

        for n in range(1, obstacle_num):
            obstacle_list.append(Obstacle(
                    self.display,
                    self.width,
                    self.height,
                    self.floor_height_percentage
            ))
        return obstacle_list
