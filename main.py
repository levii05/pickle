import pygame
from pygame import event, QUIT, display
import sys
import game_field
import screen
import soldier

screen.draw_game()


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False

display.update()


def handle_user_events():
    running = True
    solider = soldier.draw_solider(screen.scrn)
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    soldier.move_left(screen.scrn, solider)
                    pygame.display.update()


                elif event.key == pygame.K_RIGHT:
                    soldier.move_right(screen.scrn, solider)
                    pygame.display.update()


                elif event.key == pygame.K_UP:
                    soldier.move_up(screen.scrn, solider)


                elif event.key == pygame.K_DOWN :
                    soldier.move_down(screen.scrn, solider)
                    pygame.display.update()


                elif event.key == pygame.K_KP_ENTER:
                    game_field.draw_grid()

                elif event.key == pygame.K_SPACE:
                    game_field.draw_grid_dark()
                    flad = game_field.draw_grid_dark()
                    if flad:
                        game_field.draw_grid()
                        screen.draw_game()
                        soldier.draw_solider(screen.scrn)


                elif event.key == pygame.K_ESCAPE:
                    running = False
handle_user_events()
quit()
