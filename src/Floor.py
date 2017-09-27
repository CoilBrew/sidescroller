class Floor(Universe):
    """This class defines the floor"""
    def __init__(self, display, level):
        Universe.__init__(self, level)
        self.display = display # Takes a display argument and stores it internally
        self.colour = "Fill me in" # RBG colours: i.e. (0, 0, 0) = black :: (Int, Int, Int)
        self.startpoint = 0
        self.endpoint = self.levellength #inheritesd from the Universe class?    # The endpoint of the floor, where the level ends :: (Int, Int)

    def segments(self):
        """Segments is a list of segments"""
        pass # TODO
