class Universe(object):
    def __init__(self,level):
        self.level = level
        self.levellength = WIDTH * (3 * level)#the length of the level will be the width of the screen * the level number * 3
        self.start = 50 #Start 'flag'
        self.endpoint = levellength - 50 #End 'flag', 50 px away from the end of the level
