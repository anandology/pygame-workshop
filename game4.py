import sys
import pygame

pygame.init()

# Set the window size
size = 600, 500
w, h = size

screen = pygame.display.set_mode(size)

BLACK = 0, 0, 0
RED = 255, 0, 0
YELLOW = 255, 255, 0
r = 25

def draw_ball(x, y, color):
    center = (x, y)
    pygame.draw.circle(screen, color, center, r)

x = 200
y = 200

def paint():
    screen.fill(BLACK)
    draw_ball(x, y, RED)

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
                    x = bound(x+2*r, r, w-r)
                elif event.key == pygame.K_LEFT:
                    x = bound(x-2*r, r, w-r)

        paint()
        pygame.display.flip()
        pygame.time.wait(50)

main()
