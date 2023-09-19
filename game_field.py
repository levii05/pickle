import pygame
import consts
import soldier
import screen
import random
import time


def draw_grid():
    block_size = 20
    for x in range(consts.SCREEN_WIDTH):
        for y in range(consts.SCREEN_LENGTH):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(screen.scrn, consts.BACKGROUND_COLOR, rect, 1)
    pygame.display.flip()

def wait_normal():
    pygame.time.wait(1000)
    draw_grid()

def draw_grid_dark():
    flad = True
    screen.scrn.fill(consts.BACKGROUND_COLOR_DARK)
    blockSize = 20  # Set the size of the grid block
    for x in range(0, consts.SCREEN_WIDTH, blockSize):
        for y in range(0, consts.SCREEN_LENGTH, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen.scrn, consts.BACKGROUND_COLOR, rect, 1)
    soldier.draw_night_soldier(screen.scrn)
    bomb_generate_locate()
    screen.draw_bomb(screen.scrn)
    pygame.display.flip()
    return flad

def draw_board():
    row_list = []
    board = []
    for i in range(50):
        row_list.append(" ")
        for J in range(25):
            board.append(row_list)
    return board


def bomb_generate_locate():
    board = draw_board()
    for i in range(20):

        bomb_x = random.randint(1, 47)
        bomb_y = random.randint(1, 22)
        while bomb_x < 4 and bomb_y < 4:
            bomb_x = random.randint(1, 47)
            bomb_y = random.randint(1, 22)
        board[bomb_x][bomb_y - 1] = consts.BOMB
        board[bomb_x][bomb_y] = consts.BOMB
        board[bomb_x][bomb_y + 1] = consts.BOMB
    return bomb_x, bomb_y

