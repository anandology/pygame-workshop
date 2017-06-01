import sys
import pygame

pygame.init()

BLACK = 0, 0, 0
RED = 255, 0, 0
GRAY = 150, 150, 150
YELLOW = 255, 255, 0


COLS = 8
ROWS = 6
BALL_COLOR = RED
BALL_RADIUS = 20
WALL_COLOR = GRAY
CELL_WIDTH = 50
CELL_HEIGHT = 50

# Set the window size
size = COLS*CELL_WIDTH, ROWS*CELL_HEIGHT
w, h = size

screen = pygame.display.set_mode(size)


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

def move(new_x, new_y):
    """Move the ball to (new_x, new_y) if possible.
    If moving there is not possible, the ball position
    will not be changed.
    """
    global x, y
    # if new_x < 0 or new_x >= COLS:
    #     return
    # if new_y < 0 or new_y >= ROWS:
    #     return
    # if (new_x, new_y) in WALLS:
    #     return
    if is_move_allowed(new_x, new_y):
        x, y = new_x, new_y
    else:
        # TODO: play beep sound
        print("Not possible!")

def is_move_allowed(x, y):
    return (
        0 <= x < COLS
        and 0 <= y < ROWS
        and (x, y) not in WALLS
        )

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move(x+1, y)
                elif event.key == pygame.K_LEFT:
                    move(x-1, y)
                elif event.key == pygame.K_UP:
                    move(x, y-1)
                elif event.key == pygame.K_DOWN:
                    move(x, y+1)

        paint()
        pygame.display.flip()
        pygame.time.wait(50)

main()
