import sys

import pygame

class AlienInvasion:
    """A general class designed to magage resources and hot the gaame works"""

    def __init__(self):
        """Initializing the game and creating its resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien invasion")

    def run_game(self):
        """Starting the main game loop."""
        while True:
            #Waiting for a key or mouse button to be pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Display the last modified screen
            pygame.display.flip()

if __name__ == '__main__':
    #Creating a copy of the game and lauching it
    ai = AlienInvasion()
    ai.run_game()