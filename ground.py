import pygame
from pygame.sprite import Sprite 

class Ground(Sprite):
    """A class to manage ground sprite"""

    def __init__(self, game, x, y):
        """Initialize ground"""
        super().__init__()
        
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load('images/ground.png')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.x -= self.settings.scroll_speed
        if self.rect.x <= -self.settings.screen_width:
            self.kill()