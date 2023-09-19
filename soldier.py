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
    if solider["x_val"] >= 0:
        solider["x_val"] -= 12.5
        if solider["x_val"] >= 0:
            scrn.blit(consts.SOLDIER, (solider["x_val"], solider["y_val"]))
            pygame.display.update()


def move_right(scrn, solider):
    if solider["x_val"] <= 920:
        solider["x_val"] += 12.5
        if solider["x_val"] <= 920:
            scrn.blit(consts.SOLDIER, (solider["x_val"], solider["y_val"]))
            pygame.display.update()


def move_up(scrn, solider):
    if solider["y_val"] >= 12.5:
        solider["y_val"] -= 12.5
        if solider["y_val"] >= 12.5:
            scrn.blit(consts.SOLDIER, (solider["x_val"], solider["y_val"]))
            pygame.display.update()


def move_down(scrn, solider):
    if solider["y_val"] <= 420:
        solider["y_val"] += 12.5
        if solider["y_val"] <= 420:
            scrn.blit(consts.SOLDIER, (solider["x_val"], solider["y_val"]))
            pygame.display.update()
