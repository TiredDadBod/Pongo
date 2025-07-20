import pygame as pg
from settings import Settings
from paddles import Paddle
from ball import Ball

class Computer(Paddle):
    """A class to represent the computer-controlled paddle."""
    
    def __init__(self):
        super().__init__()
        self.settings = Settings()
        self.ball = Ball()
        self.speed = 10
        self.rect = pg.Rect(0, 0, self.settings.paddle_width, self.settings.paddle_height)
        self.rect.x = self.settings.screen_width - self.settings.paddle_width - 10  # Position on the right side
        self.rect.y = (self.settings.screen_height - self.height) // 2  # Center vertically

    def update(self, ball):
        """Update the paddle's position based on the ball's position."""
        dead_zone = 5  
        if ball.rect.centery < self.rect.centery - dead_zone:
            self.rect.y -= self.speed
        elif ball.rect.centery > self.rect.centery + dead_zone:
            self.rect.y += self.speed
        
        # Keep the paddle within the screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height

    def draw_computer(self, screen):
        """Draw the paddle on the screen."""
        pg.draw.rect(screen, self.settings.paddle_color, self.rect)

    def reset_position(self):
        """Reset the paddle's position to the initial state."""
        self.rect.y = (self.settings.screen_height - self.height) // 2
        self.rect.x = self.settings.screen_width - self.settings.paddle_width - 10