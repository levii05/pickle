import pygame.display
from pygame import event, QUIT, display

import screen
import consts

while True:
    screen.screen_start()
    for EVENT in event.get():
        if EVENT.type == QUIT:
            quit()
    display.update()

quit()
# pygame.display.quit()