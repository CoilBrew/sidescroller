class Player(object):
    """This defines the player"""
    def __init__(self):
        # create base_velocity
        # create health
        # create image/asset
        self.position = 0

        # The below commented out stuff was just me playing around - haven't spent any time trying to make it work and i don't think the syntax is correct (LEE?)
        # All this stuff lives in main.py... for now (ADAM)
        # STARTX = 0.5*WIDTH
        # STARTY = 0.75*HEIGHT
        # self.burritoMan = pygame.image.load('burrito.png')
        # self.DISPLAY.blit(burritoMan, (STARTX, STARTY))

    def move(self, direction):
        """Takes a character representing the direction of movement"""
        if direction == "A":
            # move left
            self.position == self.position - 10
        elif direction == "D":
            # move right
            self.position == self.position + 10
        # elif direction == "u":
        #     # move up
        else:
            print("Error")
