import pygame
import consts
import random


def create_field():
    board = []
    for i in range(25):
        for j in range(50):
            board.append(" ")
    return board


def bush_random():
    board = create_field()
    for bush in range(20):
        element = random.randint(0, 25)
        element2 = random.randint(0, 50)
        board[element][element2] = consts.BUSH
    return board
