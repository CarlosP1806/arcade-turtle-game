import random
import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A general class to create enemy instances"""

    def __init__(self, game, x, y):
        """Initialize enemy resources"""
        super().__init__()

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image_list = [
            pygame.image.load('images/shark1.png'),
            pygame.image.load('images/shark2.png'),
            pygame.image.load('images/shark3.png'),
        ]

        # Set image
        self.image = self.image_list[0]
        self.image_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Movement settings
        self.x_velocity = self.settings.enemy_velocity

    def update(self):
        """Update enemy position"""
        # Animation
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = self.image_list[self.image_index // 10]

        # Movement
        self.rect.x -= self.x_velocity
        if self.rect.x <= -self.settings.screen_width:
            self.kill()
