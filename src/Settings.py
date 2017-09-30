import json

class Settings(object):
    def __init__(self):
        self.settingsFile = json.load(open("./settings.json"))
        self.fps = self.settingsFile["FPS"]
        self.width = self.settingsFile["resolution"]["width"] # Width is the width of the screen
        self.height = self.settingsFile["resolution"]["height"] # Height is the screen height divided by 2

