import pygame
from settings import Settings
from random import randint

class Ball:
    def __init__(self):

        self.settings = Settings()
        # Initialize the ball's position, size, color, and speed
        self.rect = pygame.Rect(
                                400,
                                300,
                                self.settings.ball_width,
                                self.settings.ball_height
                                )
        self.color = self.settings.ball_color
        self.speed = self.settings.ball_speed
        self.direction_x = randint(-1, 1) * self.speed
        self.direction_y = randint(-1, 1) * self.speed

    def update_ball(self):
        self.rect.x += self.direction_x
        self.rect.y += self.direction_y
        self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.settings.screen_height:
            self.rect.bottom = self.settings.screen_height
        elif self.direction_x == 0:
            # The ball is not moving on the X axis
            self.direction_x = self.speed if randint(0, 1) == 0 else -self.speed

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def reset_position(self):
        self.rect.x = 400
        self.rect.y = 300
        self.speed = self.settings.ball_speed
        self.direction_x = randint(-1, 1) * self.speed
        self.direction_y = randint(-1, 1) * self.speed