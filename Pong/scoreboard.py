import pygame as pg
from settings import Settings
from paddles import Paddle
from ball import Ball
from computer import Computer

class Scoreboard:
    """A class to manage the scoreboard for the Pong game."""
    
    def __init__(self, ball):
        """Initialize the scoreboard settings."""
        self.settings = Settings()
        self.font = self.settings.score_font
        self.left_score = self.settings.score_left
        self.right_score = self.settings.score_right
        self.ball = ball

    def draw_scoreboard(self, screen):
        """Draw the current scores on the screen."""
        left_text = self.font.render(str(self.left_score), True, self.settings.score_color)
        right_text = self.font.render(str(self.right_score), True, self.settings.score_color)
        
        # Draw scores
        screen.blit(left_text, self.settings.score_left_rect)
        screen.blit(right_text, self.settings.score_right_rect)

    def update_scores(self):
        """Update the scores."""
        if self.ball.rect.x < 0:
            self.right_score += 1
            self.ball.reset_position()
        elif self.ball.rect.x > self.settings.screen_width:
            self.left_score += 1
            self.ball.reset_position()

    def reset_scores(self):
        """Reset the scores to zero."""
        self.left_score = 0
        self.right_score = 0
        self.update_scores()