import pygame as pg

class Settings:
    """A class to store all settings for Pong game."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.screen_bg_color = (0, 0, 0)  # RGB color for the background
        self.screen_fps = 60  # Frames per second 

        # Ball settings
        self.ball_height = 20
        self.ball_width = 20
        self.ball_color = (255, 255, 255)  # RGB color for the ball
        self.ball_speed = 5

        # Paddle settings
        self.paddle_width = 20
        self.paddle_height = 100
        self.paddle_color = (255, 255, 255)  # RGB color
        self.paddle_speed = 10

        # Scoreboard settings
        self.score_font_size = 36
        self.score_color = (255, 255, 255)  # RGB color for the score text
        self.score_font = pg.font.Font(None, self.score_font_size)
        self.score_left = 0
        self.score_right = 0
        self.score_left_rect = pg.Rect(60, 10, 100, 50)
        self.score_right_rect = pg.Rect(self.screen_width - 150, 10, 100, 50)

        # Difficulty settings
        self.increased_ball_speed = 1.1  # Factor by which the ball speed increases
        self.hard_paddle_speed = 0.5  # Factor by which the paddle speed decreases in hard mode
        self.medium_paddle_speed = 0.25  # Factor for medium difficulty
        self.easy_paddle_speed = 0.1  # Factor for easy difficulty