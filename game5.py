import sys
import pygame

pygame.init()

# Set the window size
size = 600, 500
w, h = size

screen = pygame.display.set_mode(size)

BLACK = 0, 0, 0
RED = 255, 0, 0
GRAY = 150, 150, 150
YELLOW = 255, 255, 0
r = 25

BALL_COLOR = RED
BALL_RADIUS = 20
WALL_COLOR = GRAY
CELL_WIDTH = 50
CELL_HEIGHT = 50

WALLS = [
    (3, 4),
    (3, 5),
    (2, 2)
]

# ball coordinates
x = 3
y = 2

def draw_ball(x, y):
    center = (x*CELL_WIDTH + CELL_WIDTH//2, y*CELL_HEIGHT + CELL_HEIGHT//2)
    pygame.draw.circle(screen, BALL_COLOR, center, BALL_RADIUS)

def draw_wall(x, y):
    rect = (x*CELL_WIDTH, y*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
    pygame.draw.rect(screen, WALL_COLOR, rect)

def draw_walls():
    for x, y in WALLS:
        draw_wall(x, y)

def draw_grid():
    for y in range(0, h, CELL_HEIGHT):
        pygame.draw.line(screen, YELLOW, (0, y), (w, y))
    for x in range(0, w, CELL_WIDTH):
        pygame.draw.line(screen, YELLOW, (x, 0), (x, h))

def paint():
    screen.fill(BLACK)
    draw_grid()
    draw_walls()
    draw_ball(x, y)

def bound(x, minvalue, maxvalue):
    if x < minvalue:
        return minvalue
    elif x > maxvalue:
        return maxvalue
    else:
        return x

def main():
    global x
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if (x+1, y) in WALLS:
                        print("Not possible!")
                    else:
                        x = x+1
                elif event.key == pygame.K_LEFT:
                    x = x-1

        paint()
        pygame.display.flip()
        pygame.time.wait(50)

main()
