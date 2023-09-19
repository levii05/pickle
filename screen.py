import random
import pygame
import consts
import game_field

scrn = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))


def draw_bushes():
    locate_list = []
    scrn.fill(consts.BACKGROUND_COLOR)
    grass = pygame.transform.scale(consts.BUSH, (50, 50))

    for i in range(20):
        x = random.randint(0, 900)
        y = random.randint(0, 450)
        scrn.blit(grass, (x, y))
        locate_list.append(x, y)

def keep
def draw_game():
    draw_bushes()
    draw_flag(scrn)
    pygame.display.flip()


def draw_flag(scrn):
    flag = {"x_val": 0, "y_val": 0}
    consts.FLAG = pygame.transform.scale(consts.FLAG, (consts.FLAG_HEIGHT, consts.FLAG_WIDTH))
    scrn.blit(consts.FLAG, (consts.FLAG_X, consts.FLAG_Y))
    pygame.display.flip()
    return flag


def draw_bomb(scrn):
    for i in range(20):
        bomb = {"x_val": 0, "y_val": 0}
        consts.BOMB = pygame.transform.scale(consts.BOMB, (consts.BOMB_HEIGHT, consts.BOMB_WIDTH))
        bomb["x_val"], bomb["y_val"] = game_field.bomb_generate_locate()
        scrn.blit(consts.BOMB, (bomb["x_val"] * 20, bomb["y_val"] * 20))
        pygame.display.flip()
    return bomb


def create_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    sized_arrow = pygame.transform.scale(soldier, (
        consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    return soldier


def draw_soldier():
    draw_game().blit(create_soldier())
