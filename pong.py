import pygame

# initialize pygame stuff, and create a display to draw on and a clock to keep time
pygame.init()
display = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

# this value will keep track of whether the game is running or not
isRunning = True

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

# keep track of some keys
p1UpPressed = False
p1DownPressed = False

p2UpPressed = False
p2DownPressed = False

p1Position = 250
p2Position = 250

# this is the game loop. since it continues while isRunning is true,
# setting it to false in the game loop ends the game
while isRunning:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1UpPressed = True
            elif event.key == pygame.K_s:
                p1DownPressed = True
            elif event.key == pygame.K_UP:
                p2UpPressed = True
            elif event.key == pygame.K_DOWN:
                p2DownPressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1UpPressed = False
            elif event.key == pygame.K_s:
                p1DownPressed = False
            elif event.key == pygame.K_UP:
                p2UpPressed = False
            elif event.key == pygame.K_DOWN:
                p2DownPressed = False
     
    # update code
    if p1UpPressed:
        p1Position -= 5
    if p1DownPressed:
        p1Position += 5
    if p2UpPressed:
        p2Position -= 5
    if p2DownPressed:
        p2Position += 5

    # draw code
    # clear display
    display.fill((0, 0, 0))

    # draw first player
    pygame.draw.rect(display, (255, 255, 255), (0, p1Position - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))

    #draw second player
    pygame.draw.rect(display, (255, 255, 255), (500 - PADDLE_WIDTH, p2Position - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))

    # print display to the screen
    pygame.display.flip()

    # delay game so it runs at a specific framerate. If you didn't do this the game would run way too fast,
    # and would run at a different speed depending on the speed of your computer.
    clock.tick(60)
