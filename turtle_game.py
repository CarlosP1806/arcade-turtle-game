import sys
import pygame 
import random
import time

from settings import Settings
from player import TurtlePlayer
from ground import Ground
from enemy import Enemy
from coin import Coin
from scoreboard import Scoreboard

class TurtleGame:
    """Overall class to manage game assets"""

    def __init__(self):
        """Initialize game instance and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tortuguita")

        self.background_image = pygame.image.load('images/background.jpg')

        # Scoring system
        self.score = 0
        self.scoreboard = Scoreboard(self)

        # Instantiate resources
        self.turtle = TurtlePlayer(self)
        self.ground = pygame.sprite.Group()
        self.ground.add(Ground(self, 0, 520))

        # Enemy spawner
        self.enemies = pygame.sprite.Group()
        self.enemy_timer = 30

        # Coin spawner
        self.coins = pygame.sprite.Group()
        self.coin_timer = 30

    def run_game(self):
        """Start game loop for game"""
        while True:
            self._check_events() 
            self._update_screen()
            self._spawn_enemies()
            self._spawn_coins()

            self.clock.tick(60)
            pygame.display.flip()
        
    def _check_events(self):
        """Respond to user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.turtle.jump()

    def _update_screen(self):
        """Redraw screen and resources"""
        self.screen.blit(self.background_image, (0,0))
        self.scoreboard.show_score()
        self.ground.draw(self.screen)
        self.enemies.draw(self.screen)
        self.coins.draw(self.screen)
        self.turtle.blitme()

        # Update ground
        if len(self.ground) <= 2:
            self.ground.add(Ground(self, self.settings.screen_width, 520))

        self.ground.update()
        self.turtle.update()
        self.enemies.update()
        self.coins.update()

        # Check for collisions
        if (pygame.sprite.spritecollideany(self.turtle, self.enemies)
            or pygame.sprite.spritecollideany(self.turtle, self.ground)):
            self._turtle_hit()

        # Update score
        collected_coin = pygame.sprite.spritecollideany(self.turtle, self.coins) 
        if collected_coin:
            self.score += 1
            self.scoreboard.prep_score()
            collected_coin.kill()
    
    def _spawn_enemies(self):
        """Spawn enemies into game"""
        if self.enemy_timer <= 0:
            enemy_x = 550
            enemy_y = random.randint(30, 500)
            self.enemies.add(Enemy(self, enemy_x, enemy_y))
            self.enemy_timer = random.randint(100, 150)
        self.enemy_timer -= 1
    
    def _spawn_coins(self):
        """Spawn coins"""
        if self.coin_timer <= 0:
            coin_x = 550
            coin_y = random.randint(30, 500)
            self.coins.add(Coin(self, coin_x, coin_y))
            self.coin_timer = random.randint(100, 150)
        self.coin_timer -= 1
    
    def _turtle_hit(self):
        """Respond to turtle being hit by an enemy"""
        self.enemies.empty()
        self.coins.empty()
        self.turtle.center()

        self.score = 0
        self.scoreboard.prep_score()

        # Pause
        time.sleep(0.5)


if __name__ == '__main__':
    game = TurtleGame()
    game.run_game()
