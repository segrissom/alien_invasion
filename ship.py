import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initializes the ship and sets the starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # time to load the ship image
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starting all ships at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # now creating a movement flag, which will be set to false while the
        # ship is still
        self.moving_right = false
        self.moving_left = false

        # setting the ship's speed
        self.ship_speed_factor = 1.5

    def update(self):
        """ This is to update the ship's position based on the movement flag"""
        # this will update the value of the center of the ship, but
        # not it's rectangle which we do because we're moving by partial pixels
        # and the rect will only store integer portions of decimals

        # adding in the and statement so that the ship doesn't go past the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # updating the rect obj from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
