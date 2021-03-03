import sys

import pygame

from settings import Settings

class AlienInvasion:
    """A general class designed to magage resources and hot the gaame works"""

    def __init__(self):
        """Initializing the game and creating its resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Starting the main game loop."""
        while True:
            #Waiting for a key or mouse button to be pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Refresh the screen ruring each loop iteration
            self.screen.fill(self.settings.bg_color)

            #Display the last modified screen
            pygame.display.flip()

if __name__ == '__main__':
    #Creating a copy of the game and lauching it
    ai = AlienInvasion()
    ai.run_game()
###################################################################################