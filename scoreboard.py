import pygame.font

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, game):
        """Initialize score attributes"""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        """Render the score into a message"""
        score_str = str(self.game.score)
        self.score_image = self.font.render(score_str, True,
            self.text_color, None)
        
        # Display score at top
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Print score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        
