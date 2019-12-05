import pygame
import sys
from pygame.locals import *
from source import Sprites
from source import Logic

screen_size = (1600, 900)  # This variable sets the size of the screen
frame_delay = 24  # Don't worry about this too much - it just ensures the game runs at a constant frame rate
game_title = "PyGame Boilerplate"  # Change this to the name of your game

background = Sprites.Background()

player = (Sprites.Player((0, 0)))

enemy_sprites = pygame.sprite.RenderUpdates()  # This variable contains all the enemy sprites

neutral_sprites = pygame.sprite.RenderUpdates()  # This variable contains all neutral sprites


def main():  # this function is the main game loop - everything that happens in the game happens here
    # This is the set up portion of the game loop - you initialize anything you may need

    screen = pygame.display.set_mode(screen_size)  # This sets the screen size
    pygame.display.set_caption(game_title)  # This sets the screen caption

    while True:  # Here is where all the game logic happens

        player.move()

        screen.blit(background.image, background.rect)  # Draws the background before anything else

        screen.blit(player.image, player.rect)

        enemy_sprites.draw(screen)  # Draws all the enemy sprites

        neutral_sprites.draw(screen)  # Draws all the neutral sprites

        pygame.display.flip()  # Renders the screen
        pygame.time.delay(frame_delay)  # Maintains the frame rate

        for event in pygame.event.get():  # This closes the game if you press the quit button on the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            player.process(event)
            # This processes any input that may have occurred.
            # Change the player process function to add your own functionality.


if __name__ == "__main__":  # This makes the code run, don't worry about it
    main()