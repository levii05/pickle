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
        locate_list.append([x, y])
    return locate_list


locate_list = draw_bushes()


def draw_game():
    scrn.fill(consts.BACKGROUND_COLOR)
    grass = pygame.transform.scale(consts.BUSH, (50, 50))
    for plant in locate_list:
        scrn.blit(grass, (plant[0], plant[1]))
    draw_flag(scrn)
    pygame.display.flip()
    # if main.state["state"] == consts.LOSE_STATE:
    #     draw_lose_message()
    # draw_bushes()
    # draw_flag(scrn)
    # pygame.display.flip()


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
        bomb["x_val"], bomb["y_val"], board , bomb_list= game_field.bomb_generate_locate()
        scrn.blit(consts.BOMB, (bomb["x_val"] * 20, bomb["y_val"] * 20))
        pygame.display.flip()
    return board , bomb_list


def create_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    soldier = pygame.transform.scale(soldier, (
        consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    return soldier


def draw_soldier():
    draw_game().blit(create_soldier())


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    scrn.blit(text_img, location)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)


def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)
