import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """A general class designed to manage resources and hot the game works"""

    def __init__(self):
        """Initializing the game and creating its resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Starting the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self._upadte_screen()


    def _check_events(self):
        # Waiting for a key or mouse button to be pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _upadte_screen(self):
        """update iamges on the screen and move to a new screen"""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Display the last modified screen
        pygame.display.flip()

if __name__ == '__main__':
    #Creating a copy of the game and lauching it
    ai = AlienInvasion()
    ai.run_game()
###################################################################################