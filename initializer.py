import pygame

class Initializer:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.screen_width, self.screen_height = info.current_w, info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.player_pos = pygame.Vector2(self.screen_width / 2, self.screen_height / 2)
        self.timer = pygame.time.Clock()
        self.dt = 0
