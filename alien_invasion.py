import sys

import pygame

class AlienInvasion:
    """A general class designed to magage resources and hot the gaame works"""

    def __init__(self):
        """Initializing the game and creating its resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien invasion")
        #Define the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the main game loop."""
        while True:
            #Waiting for a key or mouse button to be pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Refresh the screen ruring each loop iteration
            self.screen.fill(self.bg_color)

            #Display the last modified screen
            pygame.display.flip()

if __name__ == '__main__':
    #Creating a copy of the game and lauching it
    ai = AlienInvasion()
    ai.run_game()
###################################################################################