import sys
import pygame

def check_keydown_events(event, ship):
    """This responds to kepresses"""
    if event.key == pygame.K_RIGHT:
        # this will move the ship over while the right key is held
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # this will move the ship over left while the left key is pressed
        ship.moving_left = True
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
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def update_screen(ai_settings, screen, ship):
    """Updating images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
