import pygame

class Movement:
    def __init__(self, initializer):
        self.initializer = initializer

    def keys_pressed(self, keys):
        if keys[pygame.K_w]:
            self.initializer.player_pos.y -= 300 * self.initializer.dt
            self.initializer.screen.fill((0, 0, 0))
        if keys[pygame.K_s]:
            self.initializer.player_pos.y += 300 * self.initializer.dt
            self.initializer.screen.fill((0, 0, 0))
        if keys[pygame.K_a]:
            self.initializer.player_pos.x -= 300 * self.initializer.dt
            self.initializer.screen.fill((0, 0, 0))
        if keys[pygame.K_d]:
            self.initializer.player_pos.x += 300 * self.initializer.dt
            self.initializer.screen.fill((0, 0, 0))
        if keys[pygame.K_0]:
            self.initializer.screen.fill((0, 0, 0))
