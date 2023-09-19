import consts
import screen
import pygame


def draw_solider(scrn):
    soldier = {"x_val": 0, "y_val": 0}
    consts.SOLDIER = pygame.transform.scale(consts.SOLDIER, (80, 80))
    scrn.blit(consts.SOLDIER, (0, 0))
    pygame.display.flip()
    return soldier


def draw_night_soldier(scrn):
    soldier_night = {"x_val": 0, "y_val": 0}
    consts.SOLDIER_NIGHT = pygame.transform.scale(consts.SOLDIER_NIGHT, (80, 80))
    scrn.blit(consts.SOLDIER_NIGHT, (0, 0))
    pygame.display.flip()
    return soldier_night


def move_left(scrn, solider):
    solider["x_val"] += 1
    scrn.blit(consts.SOLDIER, (solider["x_val"], solider["x_val"]))


def move_right(scrn, solider):
    solider["x_val"] -= 1
    scrn.blit(consts.SOLDIER, (solider["x_val"], solider["x_val"]))


def move_up(scrn, solider):
    solider["y_val"] -= 1
    scrn.blit(consts.SOLDIER, (solider["x_val"], solider["x_val"]))


def move_down(scrn, solider):
    solider["y_val"] += 1
    scrn.blit(consts.SOLDIER, (solider["x_val"], solider["x_val"]))
