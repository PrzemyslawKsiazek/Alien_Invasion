import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """A general class designed to manage resources and hot the game works"""

    def __init__(self):
        """Initializing the game and creating its resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        #Create a copy that stores statistical data about the game
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #creating a play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Starting the main game loop."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updating the position of bullets and removing those not visible on the screen"""

        #Updating the position bullets
        self.bullets.update()

        #Remove bullets that are outside the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Response to a collision between a bullet and an alien"""
        #Removal of all bullets nd aliens objects between which there has ben a collision
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #Getting rid of existing missiles and creating a new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Update the location of all aliens in the fleet and update the location of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #Collision detection between ship and alien
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Search for aliens reaching the bottom adge of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """The reaction to an alien hitting the ship"""
        #Reaction to an alien hitting the ship
        if self.stats.ships_left > 0:
            #Decrease the value stored in ship_left
            self.stats.ships_left -= 1
            # Deleting the contents of aliens and bullets lists
            self.aliens.empty()
            self.bullets.empty()

            # Creating a new fleet and centering the ship
            self._create_fleet()
            self.ship.center_ship()

            #Pause
            sleep(0.5)

        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Checking if any aliens have reached the bottom edge of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Just like when a ship collides with an alien
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create a full fleet aliens"""
        #Creating of alien and determining the number of alines who will fit in a row
        #The distance between each alien is equal to the width of the alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Determine how many alien rows will fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Create a full fleet of alien
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        #Creating an alien and placing it in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately when the alien reaches the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Moving the entire fleet down and changing the direction in which it moves"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _upadte_screen(self):
        """update iamges on the screen and move to a new screen"""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet( )
        self.aliens.draw(self.screen)

        #Display button only when game is not active
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display the last modified screen
        pygame.display.flip()


if __name__ == '__main__':
    #Creating a copy of the game and lauching it
    ai = AlienInvasion()
    ai.run_game()
###################################################################################