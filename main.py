
from pygame import event, QUIT, display
import screen

screen.draw_game()

while True:
    for EVENT in event.get():
        if EVENT.type == QUIT:
            quit()
    display.update()

# print(game_field.bush_random())

quit()
# pygame.display.quit()