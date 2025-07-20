import pygame as pg
from settings import Settings

class Paddle:
    def __init__(self):
        """Initialize the paddle's attributes."""
        self.settings = Settings()
        self.width = 20
        self.height = 100
        self.speed = 20
        self.rect = pg.Rect(0, 0, self.width, self.height)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def draw_paddle(self):
        self.rect = pg.draw.rect(pg.surface.Surface, self.width, self.height)
        self.rect.x = 10

    def update_paddle(self):
        """Update the paddle's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.rect.y += self.speed

        # Keep the paddle within the screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height

    def reset_position(self):
        self.rect.x = 10
        self.rect.y = 300
        self.moving_up = False
        self.moving_down = False