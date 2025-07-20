import pygame as pg
from settings import Settings
from paddles import Paddle
from ball import Ball  
from computer import Computer

class Difficulty:
    def __init__(self):
        """Initialize the difficulty settings."""
        self.settings = Settings()
        self.box_width = 200
        self.box_height = 100
        self.box_spacing = 20
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height

        self.name_rect = pg.Rect(
            300,
            50,
            200,
            100
        )

        self.easy_rect = pg.Rect(
            60,
            250,
            self.box_width,
            self.box_height
        )
        self.medium_rect = pg.Rect(
            60 + self.box_width + (2 *self.box_spacing),
            250,
            self.box_width,
            self.box_height
        )
        self.hard_rect = pg.Rect(
            60 + 2 * (self.box_width + (2 * self.box_spacing)),
            250,
            self.box_width,
            self.box_height
        )

        self.goal_rect = pg.Rect(
            300,
            450,
            200,
            100
        )

    def difficulty_screen(self, screen):
        font = pg.font.Font(None, 48)
        running = True
        while running:
            screen.fill((30, 30, 30))
            # Draw boxes
            pg.draw.rect(screen, (0, 0, 200), self.name_rect)
            pg.draw.rect(screen, (0, 200, 0), self.easy_rect)
            pg.draw.rect(screen, (200, 200, 0), self.medium_rect)
            pg.draw.rect(screen, (200, 0, 0), self.hard_rect)
            pg.draw.rect(screen, (0, 0, 200), self.goal_rect)
            # Draw text
            name_text = font.render("Pongo!", True, (255, 255, 255))
            easy_text = font.render("Easy", True, (255, 255, 255))
            medium_text = font.render("Medium", True, (255, 255, 255))
            hard_text = font.render("Hard", True, (255, 255, 255))
            goal_text = font.render("First to 5!", True, (255, 255, 255))
            screen.blit(name_text, name_text.get_rect(center=self.name_rect.center))
            screen.blit(easy_text, easy_text.get_rect(center=self.easy_rect.center))
            screen.blit(medium_text, medium_text.get_rect(center=self.medium_rect.center))
            screen.blit(hard_text, hard_text.get_rect(center=self.hard_rect.center))
            screen.blit(goal_text, goal_text.get_rect(center=self.goal_rect.center))
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    return None
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.easy_rect.collidepoint(event.pos):
                        return 'easy'
                    elif self.medium_rect.collidepoint(event.pos):
                        return 'medium'
                    elif self.hard_rect.collidepoint(event.pos):
                        return 'hard'