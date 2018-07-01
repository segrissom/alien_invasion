import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ship):
    """This responds to kepresses"""
    if event.key == pygame.K_RIGHT:
        # this will move the ship over while the right key is held
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # this will move the ship over left while the left key is pressed
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # This is checking to see if we've fired a bullet
        # and will also create the bullet
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event, ship):
    """This responds to the keyups"""
    if event.key == pygame.K_RIGHT:
        # This will stop moving the ship to the right once you release up on the right
        # key
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # this will stop moving the ship to the left
        # one the key is released
        ship.moving_left = False

def check_events():
    """Responds to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """Updating images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(bg_color)
    ship.blitme()
    # Need to redraw all of the bullets since they should all be moving
    for bullet in bullets.sprite():
        bullet.draw_bullet()
    # Make the most recently drawn screen visible
    pygame.display.flip()
