import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class designed to menage the bullet fired by a ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rectangle at point (0,0) an then
        #defining an appropriate position for it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Bullet position is defined by a floating point value
        self.y = float(self.rect.y)


    def update(self):

        """Moving a bullet across the screen"""
        #bullet position update
        self.y -= self.settings.bullet_speed

        #updaate the postion of the bullet rectangle
        self.rect.y = self.y

    def draw_bullet(self):
        """Dysplay the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
