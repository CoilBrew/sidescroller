import pygame

class Timer(object):
    def __init__(self, display, fontColour, bg):
        self.display = display
        self.fontColour = fontColour
        self.bg = bg

    def render(self, x, y, ticks):
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        timer = fontObj.render("Timer: " + str(ticks)[:-3], True, self.fontColour, self.bg)
        timer_rect = timer.get_rect(center = (x, y))
        self.display.blit(timer, timer_rect)
