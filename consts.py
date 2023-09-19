import pygame

SCREEN_LENGTH = 500
SCREEN_WIDTH = 1000

BACKGROUND_COLOR = (0, 200, 0)
BACKGROUND_COLOR_DARK = (0, 0, 0)

BUSH = pygame.image.load("grass.png")
SOLDIER = pygame.image.load("soldier.png")
# SNAKE = pygame.image.load("snake.png")
FLAG = pygame.image.load("flag.png")
# EXPLOTION = pygame.image.load("explotion.png")
SOLDIER_NIGHT = pygame.image.load("soldier_nigth.png")
BOMB = pygame.image.load("mine.png")


SOLDIER_HEIGHT = 40
SOLDIER_WIDTH = 80

FLAG_WIDTH = 60
FLAG_HEIGHT = 80

FLAG_X = 920
FLAG_Y = 440

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3


BOMB_HEIGHT = 60
BOMB_WIDTH = 20

WIN_MESSAGE= "YOU WON!"
LOSE_MESSAGE = "YOU LOST! :("
BLACK = (0,0,0)
FONT_NAME = "Calibri"
LOSE_FONT_SIZE = int(0.15 * SCREEN_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * SCREEN_WIDTH, SCREEN_LENGTH / 2 - (LOSE_FONT_SIZE / 2))
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * SCREEN_WIDTH, SCREEN_LENGTH / 2 - (WIN_FONT_SIZE / 2))