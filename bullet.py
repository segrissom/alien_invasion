import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """This is in charge of the bullets that come from the ship"""

  def __init__(self, ai_settings, screen, ship):
      """This creates the bullet where the ship is, which is nice"""
      super(Bullet, self).__init__()
      self.screen = screen

      #creating the bullet's rectangle at (0,0) and then set correct position
      self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
      
