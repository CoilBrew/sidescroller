class Player(object):
    """This defines the player"""
    def __init__(self):
        # create base_velocity
        # create health
        # create image/asset

        # The below commented out stuff was just me playing around - haven't spent any time trying to make it work and i don't think the syntax is correct
        # STARTX = 0.5*WIDTH
        # STARTY = 0.75*HEIGHT
        # self.burritoMan = pygame.image.load('burrito.png')
        # self.DISPLAY.blit(burritoMan, (STARTX, STARTY))

    def move(self, direction):
        """Takes a character representing the direction of movement"""
        if direction == "l":
            # move left
        elif direction == "r":
            # move right
        elif direction == "u":
            # move up
        else:
            print("Error")
