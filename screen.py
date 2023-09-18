import pygame
import consts
import game_field


def draw_game():
    consts.screen.fill(consts.BACKGROUND_COLOR)
    # draw_arrow(game_state["rotated_arrow"])

    game_field.create_field()
    pygame.display.flip()

def create_soldier():
    soldier = pygame.image.load(consts.SOLDIER)
    sized_arrow = pygame.transform.scale(soldier, (
        consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
    return soldier

def draw_soldier():
    draw_game().blit(create_soldier())
