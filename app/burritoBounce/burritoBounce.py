import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

burrito = pygame.image.load("burrito.png")
burritorect = burrito.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        burritorect = burritorect.move(speed)
        if burritorect.left < 0 or burritorect.right > width:
            speed[0] = -speed[0]
        if burritorect.top <0 or burritorect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(burrito, burritorect)
        pygame.display.flip()
