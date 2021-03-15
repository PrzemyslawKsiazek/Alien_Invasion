import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class representatnig a single alien in the flotilla"""

    def __init__(self, ai_game):
        """initialize the alien and define its initial position"""
        super().__init__()
        self.screen = ai_game.screen

        #Loading a alien image and defining ist attribute rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Placing a new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Storning the exact horizontal position of the alien
        self.x = float(self.rect.x)
