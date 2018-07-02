# this is the class for the alien in alien_invasions
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """This is the class that is responsible for the aliens"""
    def __init__(self, ai_settings, screen):
        """initialize the alien and set the starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # need to load up our alien image
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top of the
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
