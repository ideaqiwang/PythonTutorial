import sys, pygame
pygame.init()

size = width, height = 660, 400

speed = [0, 2] # 1: x speed, 1: y speed
colors = [(0,0,0), (255,255,255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
black = 0, 0, 0

# Set the size of the display window
screen = pygame.display.set_mode(size) # input is a tuple, not a list

ball = pygame.image.load("images/intro_ball.gif")
ballrect = ball.get_rect()
#print('ballrect', ballrect)

color_index = 0

FPS = 30
fps_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pprint('Press down Q key to quit.')
                sys.exit()

    # ballrect.top += 1
    ballrect = ballrect.move(speed) # move modifies the coordinate of top-left point

    # write to the background frame
    color_index = (color_index+1) % len(colors)
    screen.fill(colors[color_index]) # refresh the window
    screen.blit(ball, ballrect)

    # switch the background frame to foreground frame
    # forground frame becomes to the backgournd frame
    pygame.display.flip()
    fps_clock.tick(FPS)
    """
    There are two frames.
    """
