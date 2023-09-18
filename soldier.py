import consts
import game_field
import screen


def draw_solider(scrn):
    soldier = {"x_val": 0, "y_val": 0}
    scrn.blit(consts.SOLDIER, (0, 0))
    # screen.scrn[0][0] = consts.SOLDIER
    return soldier


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
