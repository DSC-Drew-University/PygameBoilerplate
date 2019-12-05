import pygame
from pygame.locals import *

# Kenney.nl has tons of great textures for you to use - make sure to check it out!

# If you want to make your own sprites - head over to www.piskelapp.com
# it's an amazing online tool for making pixel art

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('source/background.jpg')
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    speed = 5  # How many pixels the player sprite will move on a button press

    def process(self, input_event):

        if input_event.type == KEYDOWN:

            if input_event.key == K_LEFT or input_event.key == ord('a'):
                self.moving_left = True
            if input_event.key == K_RIGHT or input_event.key == ord('d'):
                self.moving_right = True
            if input_event.key == K_UP or input_event.key == ord('w'):
                self.moving_up = True
            if input_event.key == K_DOWN or input_event.key == ord('s'):
                self.moving_down = True

        if input_event.type == KEYUP:

            if input_event.key == K_LEFT or input_event.key == ord('a'):
                self.moving_left = False
            if input_event.key == K_RIGHT or input_event.key == ord('d'):
                self.moving_right = False
            if input_event.key == K_UP or input_event.key == ord('w'):
                self.moving_up = False
            if input_event.key == K_DOWN or input_event.key == ord('s'):
                self.moving_down = False

    def move(self):
        if self.moving_left:
            self.rect.left = self.rect.left - self.speed
        if self.moving_right:
            self.rect.left = self.rect.left + self.speed
        if self.moving_up:
            self.rect.top = self.rect.top - self.speed
        if self.moving_down:
            self.rect.top = self.rect.top + self.speed

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('source/chicken.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

