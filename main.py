import pygame
from initializer import Initializer
from movement import Movement

initializer = Initializer()
movement = Movement(initializer)

run = True

def update():
    LEFT = 1
    RIGHT = 3
    mouse_pos = pygame.mouse.get_pos()
    mouse_event = pygame.mouse.get_pressed()
    while run:
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print("walk")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print("shoot")

def run_game():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        initializer.screen.blit(initializer.bg_image, (0, 0))
        movement.keys_pressed(pygame.key.get_pressed())
        update()

        pygame.draw.circle(initializer.screen, (255, 0, 0), (int(initializer.player_pos.x), int(initializer.player_pos.y)), 40)

        pygame.display.flip()


        initializer.dt = initializer.timer.tick(60) / 1000

    pygame.quit()
#edit

if __name__ == "__main__":
    run_game()
