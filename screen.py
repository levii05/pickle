import random
import pygame
import consts

scrn = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_LENGTH))


def draw_game():
    scrn.fill(consts.BACKGROUND_COLOR)
    grass = pygame.transform.scale(consts.BUSH, (50, 50))

    for i in range(20):
        x = random.randint(0, 900)
        y = random.randint(0, 450)
        scrn.blit(grass, (x, y))
    # game_field.create_field()
    # game_field.bush_random()
    pygame.display.flip()


def create_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    sized_arrow = pygame.transform.scale(soldier, (
        consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    return soldier


def draw_soldier():
    draw_game().blit(create_soldier())
