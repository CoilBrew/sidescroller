from src.Obstacle import *
from pprint import pprint
import operator

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
        # Sort the instances of Obstacle in ascending x order
        obstacle_list = sorted(obstacle_list, key=operator.attrgetter('x'))
        return obstacle_list

    # Create end co-ordinates 300 px after the last obstacle
    def createEnd(self, obstacle_list):
        final_obst = obstacle_list[len(obstacle_list)-1]
        obst_end = final_obst.x + final_obst.obstacle_length
        self.x = obst_end + 300
        self.y = self.height * self.floor_height_percentage
        end_coord = [self.x, self.y]
        return end_coord

    # Draw the finish line & check if it needs moving with world scroll
    def drawFinish(self, end_coord, world_scroll=0):
        finish = self.updateEnd(end_coord, world_scroll)
        pygame.draw.line(self.display, WHITE, finish, [finish[0], finish[1]-100], 10)

    # Move finish line due to world scroll
    def updateEnd(self, end_coord, world_scroll=0):
        finish_line = [end_coord[0] - world_scroll, end_coord[1]]
        return finish_line