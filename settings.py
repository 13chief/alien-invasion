class Settings:
    """A class to store settings for Alien Invasion."""

    def __init__(self):
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = "images/space.bmp"
        
        # Ship settings
        self.ship_speed = 10

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (252, 37, 228)
        self.bullets_allowed = 5 # originally 3