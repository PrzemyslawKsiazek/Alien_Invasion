import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """A general class designed to manage resources and hot the game works"""

    def __init__(self):
        """Initializing the game and creating its resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.height =  self.screen.get_rect().height
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Starting the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._upadte_screen()


    def _check_events(self):
        # Waiting for a key or mouse button to be pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Response to key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Response to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creating a new bullet and adding it to a group of bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _upadte_screen(self):
        """update iamges on the screen and move to a new screen"""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet( )
        # Display the last modified screen
        pygame.display.flip()

if __name__ == '__main__':
    #Creating a copy of the game and lauching it
    ai = AlienInvasion()
    ai.run_game()
###################################################################################