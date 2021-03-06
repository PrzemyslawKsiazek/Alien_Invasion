import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class designed to manage a spaceship"""

    def __init__(self, ai_game):
        """initialization of ship and its initial position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()



        #laading the spacehsip image and downloading the rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #each new spaceship appears at the bottom of the sreeen
        self.rect.midbottom = self.screen_rect.midbottom

        #The horizontal position of the ship is stored as floating number
        self.x = float(self.rect.x)

        #options indicating the movement of the starship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the position of the starship based on the option indicating its movement"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

        #Update the X coordinate value of a ship, not its rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update the rect object based on the value of self.x
        self.rect.x =self.x

    def blitme(self):
        """display th spaceship in its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Placing the ship in the middle at the bottom edge of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)