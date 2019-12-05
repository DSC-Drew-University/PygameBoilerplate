import pygame
from pygame.locals import *

# Kenney.nl has tons of great textures for you to use - make sure to check it out!

# If you want to make your own sprites - head over to www.piskelapp.com
# it's an amazing online tool for making pixel art


class Background(pygame.sprite.Sprite):  # Use this class to make your background - Display has all the other code you need
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('source/background.jpg') # Change this to get the image you want
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):  # You can use this class for creating your player object

    moving_left = False  # These boolean variables are used to know when the player is supposed to be moving or not
    moving_right = False
    moving_up = False
    moving_down = False

    speed = 6  # How many pixels the player sprite will move in a single game step

    def process(self, input_event):  # This functions is used to respond to events such as key presses

        if input_event.type == KEYDOWN:  # If a button is pressed down

            if input_event.key == K_LEFT or input_event.key == ord('a'):
                self.moving_left = True
            if input_event.key == K_RIGHT or input_event.key == ord('d'):
                self.moving_right = True
            if input_event.key == K_UP or input_event.key == ord('w'):
                self.moving_up = True
            if input_event.key == K_DOWN or input_event.key == ord('s'):
                self.moving_down = True

        if input_event.type == KEYUP:  # If a button is no longer being pressed

            if input_event.key == K_LEFT or input_event.key == ord('a'):
                self.moving_left = False
            if input_event.key == K_RIGHT or input_event.key == ord('d'):
                self.moving_right = False
            if input_event.key == K_UP or input_event.key == ord('w'):
                self.moving_up = False
            if input_event.key == K_DOWN or input_event.key == ord('s'):
                self.moving_down = False

    def move(self):  # This function moves the player if they are supposed to be moving
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
        self.image = pygame.image.load('source/chicken.png')  # Change this to change the skin of the player
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Enemy(pygame.sprite.Sprite):  # You can use this class to create enemies

    speed = 3  # This variable controls how many pixels the enemy will move in a single game step

    def seek_player(self, player):  # This makes the enemy follow the player
        target_x = player.rect.left
        target_y = player.rect.top

        if target_x > self.rect.left:
            self.rect.left = self.rect.left + self.speed
        elif target_x < self.rect.left:
            self.rect.left = self.rect.left - self.speed

        if target_y > self.rect.top:
            self.rect.top = self.rect.top + self.speed
        elif target_y < self.rect.top:
            self.rect.top = self.rect.top - self.speed

    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('source/snake.png')  # Change this to alter the skin of the enemies
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
