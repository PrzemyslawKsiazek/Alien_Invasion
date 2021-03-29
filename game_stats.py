class GameStats:
    """Monitoring in game statistic"""

    def __init__(self, ai_game):
        """Initialization of statistical data"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Run the game in the active state
        self.game_active = False

        #The best score should never be zeroed out
        self.high_score = 0

    def reset_stats(self):
        """Initialization of statistical data that may change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

