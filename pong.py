import pygame

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# initialize pygame stuff, and create a display to draw on and a clock to keep time
pygame.init()
display = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# this value will keep track of whether the game is running or not
isRunning = True

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

BALL_RADIUS = 10

# keep track of some keys
p1UpPressed = False
p1DownPressed = False

p2UpPressed = False
p2DownPressed = False

p1Position = WINDOW_HEIGHT / 2
p2Position = WINDOW_HEIGHT / 2

ballPositionX = WINDOW_WIDTH / 2
ballPositionY = WINDOW_HEIGHT / 2 - 3 * WINDOW_WIDTH / 10

ballVelocityX = 5
ballVelocityY = 3

def rectsCollide(rect1, rect2):
    return  rect1[0] <= (rect2[0] + rect2[2]) and \
            rect2[0] <= (rect1[0] + rect1[2]) and \
            rect1[1] <= (rect2[1] + rect2[3]) and \
            rect2[1] <= (rect1[1] + rect1[3])

# this is the game loop. since it continues while isRunning is true,
# setting it to false in the game loop ends the game
while isRunning:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            elif event.key == pygame.K_w:
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

    ballPositionX += ballVelocityX
    ballPositionY += ballVelocityY

    p1Rect = (0, p1Position - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    p2Rect = (WINDOW_WIDTH - PADDLE_WIDTH, p2Position - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ballRect = (ballPositionX - BALL_RADIUS / 2, ballPositionY - BALL_RADIUS / 2, BALL_RADIUS, BALL_RADIUS)

    if rectsCollide(p1Rect, ballRect):
        ballPositionX = PADDLE_WIDTH + BALL_RADIUS / 2
        ballVelocityX = -ballVelocityX

    if rectsCollide(p2Rect, ballRect):
        ballPositionX = WINDOW_WIDTH - (PADDLE_WIDTH + BALL_RADIUS / 2)
        ballVelocityX = -ballVelocityX

    if ballPositionY - BALL_RADIUS < 0 or ballPositionY + BALL_RADIUS > WINDOW_HEIGHT:
        ballVelocityY = -ballVelocityY

    # draw code
    # clear display
    display.fill((0, 0, 0))

    # draw first player
    pygame.draw.rect(display, (255, 255, 255), (0, p1Position - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))

    # draw second player
    pygame.draw.rect(display, (255, 255, 255), (WINDOW_WIDTH - PADDLE_WIDTH, p2Position - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))

    # draw ball
    pygame.draw.circle(display, (255, 255, 255), (ballPositionX, ballPositionY), BALL_RADIUS)

    # print display to the screen
    pygame.display.flip()

    # delay game so it runs at a specific framerate. If you didn't do this the game would run way too fast,
    # and would run at a different speed depending on the speed of your computer.
    clock.tick(60)
