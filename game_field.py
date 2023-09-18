import pygame
import consts

import screen


def draw_grid():
    block_size = 20
    for x in range(consts.SCREEN_WIDTH):
        for y in range(consts.SCREEN_LENGTH):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(screen.scrn, consts.BACKGROUND_COLOR, rect, 1)
    pygame.display.flip()


def draw_grid_dark():
    screen.scrn.fill(consts.BACKGROUND_COLOR_DARK)
    blockSize = 20  # Set the size of the grid block
    for x in range(0, consts.SCREEN_WIDTH, blockSize):
        for y in range(0, consts.SCREEN_LENGTH, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen.scrn, consts.BACKGROUND_COLOR, rect, 1)
    pygame.display.flip()

# def bush_random():
#     board = draw_grid()
#     for i in range(20):
#         element = random.randint(1, 23)
#         element2 = random.randint(1, 48)
#         board[element][element2-1] = consts.BUSH
#         board[element][element2] = consts.BUSH
#         board[element][element2 + 1] = consts.BUSH
#     return board
