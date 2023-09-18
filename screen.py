import pygame
import consts

def screen():
    pygame.init()
    screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))
    screen.fill(consts.BACKGROUND_COLOR)


