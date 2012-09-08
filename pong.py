import pygame

# initialize pygame stuff, and create a display to draw on and a clock to keep time
pygame.init()
display = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

# this value will keep track of whether the game is running or not
isRunning = True

# this is the game loop. since it continues while isRunning is true,
# setting it to false in the game loop ends the game
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
