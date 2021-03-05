import pygame

class Ship:
    """Class designed to manage a spaceship"""

    def __init__(self, ai_game):
        """initialization of ship and its initial position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #laading the spacehsip image and downloading the rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #each new spaceship appears at the bottom of the sreeen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """display th spaceship in its current position"""
        self.screen.blit(self.image, self.rect)