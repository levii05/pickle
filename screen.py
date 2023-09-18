import pygame
import consts

def screen_size():
    pygame.init()
    screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))

def screen_color():
    screen.fill(consts.BACKGROUND_COLOR)

# def random_bush():
