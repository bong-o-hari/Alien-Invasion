#import sys
import pygame

from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
    # Initiate pygame settings and screen object
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!")

    # Make a ship
    ship = Ship(screen)

    # Set the background colour
    bg_color = (230, 230, 230)

    # Start the main loop for game
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen through each pass of the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()