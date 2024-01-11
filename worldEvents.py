import pygame

class worldEvents():
    def __init__(self):
        self.LEFT = 1
        self.RIGHT = 3
        self.mouse_pos = (0, 0)
        self.mouse_event = None

    def update(self):
        run = True
        while run:
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_event = pygame.mouse.get_pressed()
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == self.RIGHT:
                    print("place")
                elif event.button == self.LEFT:
                    print("shoot")
