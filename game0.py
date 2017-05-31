"""
Hello world program using python.

This just opens a blank window  with title "Hello world!" and waits for 5 seconds before quitting.

PROBLEMS:

* Try changing the size of the window
* Try changing the title of the window
* What happens if you don't have the wait?

"""

import pygame

pygame.init()

# Set the window size
size = 400, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hello world!') 

# wait for 5 seconds so that we can see the window
pygame.time.wait(5000)
