import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    """A class to manage the coins"""

    def __init__(self, game, x, y):
        """Initialize coin settings"""
        super().__init__()

        self.screen = game.screen 
        self.settings = game.settings

        self.image_list = [
            pygame.image.load('images/Gold_1.png'),
            pygame.image.load('images/Gold_2.png'),
            pygame.image.load('images/Gold_3.png'),
        ]

        self.image = self.image_list[0]
        self.image_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.velocity = self.settings.coin_velocity
    
    def update(self):
        """Update coin position"""
        # Animation
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = self.image_list[self.image_index // 10]

        # Movement
        self.rect.x -= self.velocity
        if self.rect.x <= -self.settings.screen_width:
            self.kill()
