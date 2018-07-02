import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store the bullets in
    bullets = Group()

    # Setting the background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
