import pygame

class TurtlePlayer:
    """A class to manage the turtle"""

    def __init__(self, game):
        """Initialize turtle and its starting position"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        # Setup animation images
        self.image_list = [
            pygame.image.load('images/turtle1.png'),
            pygame.image.load('images/turtle2.png'),
            pygame.image.load('images/turtle3.png'),
        ]

        # Load and place image
        self.image = self.image_list[0]
        self.image_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.settings.turtle_starting_position

        # Movement settings
        self.velocity = 0
        self.jumping = False 
        self.y = float(self.rect.y)

    def update(self):
        """Update turtle image and position"""
        self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = self.image_list[self.image_index // 10]

        # Gravity and jump
        self.velocity += 0.5
        if self.velocity > self.settings.turtle_max_velocity:
            self.velocity = self.settings.turtle_max_velocity
        if self.rect.y < 500:
            self.y += self.velocity
            self.rect.y = self.y
        if self.velocity == 0:
            self.jumping = False
    
    def jump(self):
        """Move turtle upwards on user input"""
        if not self.jumping and self.rect.y > 0:
            self.jumping = True
            self.velocity = -self.settings.turtle_max_velocity
    
    def center(self):
        """Place turtle in starting position"""
        self.rect.center = self.settings.turtle_starting_position
        self.image = self.image_list[0]
        self.image_index = 0

        self.velocity = 0
        self.jumping = False 
        self.y = float(self.rect.y)


    def blitme(self):
        """Draw the turtle at current position"""
        self.screen.blit(self.image, self.rect)
