
from pygame import event, QUIT, display
import screen


while True:
    screen.draw_game()
    for EVENT in event.get():
        if EVENT.type == QUIT:
            quit()
    display.update()

# print(game_field.bush_random())

quit()
# pygame.display.quit()