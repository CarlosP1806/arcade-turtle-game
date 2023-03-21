class Settings:
    """A class to store all settings for game"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 551
        self.screen_height = 720

        # Backgorund settings
        self.bg_color = (23, 161, 226)
        self.scroll_speed = 1

        # Turtle settings
        self.turtle_starting_position = (100,200)
        self.turtle_max_velocity = 7

        # Enemy settings
        self.enemy_velocity = 12

        # Coin settings
        self.coin_velocity = 7
        