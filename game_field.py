import pygame
import consts
import random

import screen


def draw_grid():
    block_size = 20
    for x in range (consts.SCREEN_WIDTH):
        for y in range(consts.SCREEN_HEIGHT):
            rect = pygame.rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen.screen, consts.BACKGROUND_COLOR, rect, 1)
    pygame.display.flip()


# def create_field():
#     board = []
#     for i in range(25):
#         row = []
#         for j in range(50):
#             row.append(" ")
#         board.append(row)
#     return board


def bush_random():
    board = create_field()
    for i in range(20):
        element = random.randint(1, 23)
        element2 = random.randint(1, 48)
        board[element][element2-1] = consts.BUSH
        board[element][element2] = consts.BUSH
        board[element][element2 + 1] = consts.BUSH
    return board
