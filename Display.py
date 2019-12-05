import pygame
import sys
import random
from source import Sprites
from source import Logic

screen_size = (1600, 900)  # This variable sets the size of the screen
frame_delay = 24  # Don't worry about this too much - it just ensures the game runs at a constant frame rate
game_title = "PyGame Boilerplate"  # Change this to the name of your game
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
background = Sprites.Background()

player = (Sprites.Player((0, 0)))

enemy_sprites = pygame.sprite.RenderUpdates()  # This variable contains all the enemy sprites
number_of_enemies = 2
for i in range(number_of_enemies):  # Spawns enemies
    enemy_sprites.add(Sprites.Enemy((random.randint(0, screen_size[0]), random.randint(0, screen_size[1]))))


neutral_sprites = pygame.sprite.RenderUpdates()  # This variable contains all neutral sprites
number_of_seeds = 5
for i in range(number_of_seeds):  # Spawns seeds
    neutral_sprites.add(Sprites.Seed((random.randint(0, screen_size[0]), random.randint(0, screen_size[1]))))


def main():  # this function is the main game loop - everything that happens in the game happens here
    # This is the set up portion of the game loop - you initialize anything you may need
    dying = False  # Used to know when the player loses
    screen = pygame.display.set_mode(screen_size)  # This sets the screen size
    pygame.display.set_caption(game_title)  # This sets the screen caption

    while True:  # Here is where all the game logic happens

        if neutral_sprites.__len__() < number_of_seeds:  # This respawns seeds if there are too few
            neutral_sprites.add(Sprites.Seed((random.randint(0, screen_size[0]), random.randint(0, screen_size[1]))))

        player.move()  # moves the player if appropriate

        for seed in neutral_sprites:  # detects collisions and increases the player score
            if pygame.sprite.collide_rect(player, seed):
                neutral_sprites.remove(seed)
                player.score = player.score + 1

        screen.blit(background.image, background.rect)  # Draws the background before anything else

        neutral_sprites.draw(screen)  # Draws all the neutral sprites

        screen.blit(player.image, player.rect)  # These lines render the score on the screen
        score = font.render("Score : " + str(player.score), True, (0, 0, 0))
        screen.blit(score, (0, 0))

        enemy_sprites.draw(screen)  # Draws all the enemy sprites
        for enemy in enemy_sprites:
            enemy.seek_player(player)
            if pygame.sprite.collide_rect(player, enemy):
                lose_message = font.render("You Died! :(", True, (255, 0, 0))
                screen.blit(lose_message, (700, 450))
                dying = True

        pygame.display.flip()  # Renders the screen
        pygame.time.delay(frame_delay)  # Maintains the frame rate

        for event in pygame.event.get():  # This closes the game if you press the quit button on the window
            if event.type == pygame.QUIT or dying == True:
                pygame.time.delay(1500)
                pygame.quit()
                sys.exit()
            player.process(event)
            # This processes any input that may have occurred.
            # Change the player process function to add your own functionality.


if __name__ == "__main__":  # This makes the code run, don't worry about it
    main()