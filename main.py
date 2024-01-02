import pygame
from initializer import Initializer
from movement import Movement

initializer = Initializer()
movement = Movement(initializer)

def run_game():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        movement.keys_pressed(pygame.key.get_pressed())

        pygame.draw.circle(initializer.screen, (255, 0, 0), (int(initializer.player_pos.x), int(initializer.player_pos.y)), 40)

        pygame.display.flip()


        initializer.dt = initializer.timer.tick(144) / 1000

    pygame.quit()

if __name__ == "__main__":
    run_game()
