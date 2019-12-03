import pygame
git pugit
# Kenney.nl has tons of great textures for you to use - make sure to check it out!


class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('background.jpg')
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('snake.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


