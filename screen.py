import pygame
import consts


def screen_start():
    pygame.init()
    consts.screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
