import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """This is in charge of the bullets that come from the ship"""

  def __init__(self, ai_settings, screen, ship):
      """This creates the bullet where the ship is, which is nice"""
      super(Bullet, self).__init__()
      self.screen = screen

      #creating the bullet's rectangle at (0,0) and then set correct position
      # we don't have an image, so we have to build the bullet
      # from scratch using .Rect
      self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
      # we want the bullet to be centered on our ship
      self.rect.centerx = ship.rect.centerx
      # we want our bullet to come out of the top of the ship
      self.rect.top = ship.rect.top

      # We need to store the bullets position as a decimal
      # Remember that the speed of the ship has a decimal, thus
      # pushing this
      self.y = float(self.rect.y)

      # establishing the color and speed of the bullet
      self.color = ai_settings.bullet_color
      self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        """moves the bullet up the screen, which is important"""
        # this updates the position of the bullet
        self.y -= self.speed_factor
        # this updates the rectangle position for the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """This is what draws the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
