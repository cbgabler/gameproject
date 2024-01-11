import pygame

class Movement:
    def __init__(self, initializer):
        self.initializer = initializer

    def keys_pressed(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.mod == pygame.KMOD_NONE:
                    print('No modifier keys were in a pressed state when this '
                          'event occurred.')
            else:
                if keys[pygame.K_w]:
                    self.initializer.player_pos.y -= 300 * self.initializer.dt
                    ##self.initializer.screen.fill((self.initializer.bg_image))
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

    def mouse_pressed(self):
        print(pygame.mouse.get_pressed()[0] and self.rect)
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
