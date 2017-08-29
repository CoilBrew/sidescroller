class Floor(object):
    """This class defines the floor"""
    def __init__(self, display):
        self.display = display # Takes a display argument and stores it internally
        self.colour = "Fill me in" # RBG colours: i.e. (0, 0, 0) = black :: (Int, Int, Int)
        self.endpoint = "Fill me in" # The endpoint of the floor, where the level ends :: (Int, Int)

    def segments(self):
        """Segments is a list of segments"""
        pass # TODO

    def draw(self):
        """Creates the floor as a rectangle"""
        pass # TODO
