import pygame as pg
from settings import Settings
from paddles import Paddle
from ball import Ball
from computer import Computer
from scoreboard import Scoreboard
import math
from time import sleep
from difficulty import Difficulty

class Pong:
    def __init__(self, game):
        """Initialize the game and create game resources."""
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.paused = False
        
        #self.screen = pg.display.set_mode((800, 600)) this was incorrect
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                          self.settings.screen_height))  
        self.paddle = Paddle()
        self.paddle.rect.x += 10
        self.ball = Ball()
        self.computer = Computer()
        self.sb = Scoreboard(self.ball)
        self.difficulty = Difficulty()
        self.last_paddle_hit = None  # Add this line to track last collision
         
        pg.display.set_caption("Pong Game")

    def run(self):
        """Main loop for the game."""
        while self.running:
            # Show difficulty selection at the start or after "Play Again"
            selected = self.difficulty.difficulty_screen(self.screen)
            if selected is None:
                self.running = False
                break

            # Set computer speed based on difficulty
            if selected == 'easy':
                self.computer.speed = self.settings.easy_paddle_speed * self.settings.paddle_speed
            elif selected == 'medium':
                self.computer.speed = self.settings.medium_paddle_speed * self.settings.paddle_speed
            elif selected == 'hard':
                self.computer.speed = self.settings.hard_paddle_speed * self.settings.paddle_speed

            # Reset everything for a new game
            self.sb.reset_scores()
            self.computer.reset_position()
            self.paddle.reset_position()
            self.ball.reset_position()
            self.last_paddle_hit = None

            # Game loop for a single match
            game_over = False
            while self.running and not game_over:
                self.check_events()
                if not self.paused:
                    self.paddle.update_paddle()
                    self.ball.update_ball()
                    self.computer.update(self.ball)
                    self.check_collisions()
                    self.reset_game()

                if self.sb.left_score >= 5 or self.sb.right_score >= 5:
                    self.end_game()
                    game_over = True
                else:
                    self.update_screen()
                self.clock.tick(60)  # Limit to 60 FPS

    def check_events(self):
        """Check for events and update paddle movement."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.paddle.moving_up = True
                elif event.key == pg.K_s:
                    self.paddle.moving_down = True
                elif event.key == pg.K_ESCAPE:
                    self.running = False
                elif event.key == pg.K_SPACE:
                    self.paused = not self.paused  # Pause the game
            elif event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.paddle.moving_up = False
                elif event.key == pg.K_s:
                    self.paddle.moving_down = False

    def check_collisions(self):
        """Check for collisions between the ball and paddles."""
        if self.ball.rect.top <= 0:
            self.ball.direction_y = -self.ball.direction_y
        elif self.ball.rect.bottom >= self.settings.screen_height:
            self.ball.direction_y = -self.ball.direction_y

        # Paddle collision
        if self.ball.rect.colliderect(self.paddle.rect):
            if self.last_paddle_hit != "player":
                self.ball.direction_x = -self.ball.direction_x
                self.ball.direction_y = (self.ball.rect.centery - self.paddle.rect.centery) / 10
                self.ball.speed *= self.settings.increased_ball_speed
                # Normalize direction and apply new speed
                dx = self.ball.direction_x
                dy = self.ball.direction_y
                length = math.hypot(dx, dy)
                if length != 0:
                    self.ball.direction_x = int(self.ball.speed * dx / length)
                    self.ball.direction_y = int(self.ball.speed * dy / length)
                self.last_paddle_hit = "player"
        elif self.ball.rect.colliderect(self.computer.rect):
            if self.last_paddle_hit != "computer":
                self.ball.direction_x = -self.ball.direction_x
                self.ball.direction_y = (self.ball.rect.centery - self.computer.rect.centery) / 10
                self.ball.speed *= self.settings.increased_ball_speed
                # Normalize direction and apply new speed
                dx = self.ball.direction_x
                dy = self.ball.direction_y
                length = math.hypot(dx, dy)
                if length != 0:
                    self.ball.direction_x = int(self.ball.speed * dx / length)
                    self.ball.direction_y = int(self.ball.speed * dy / length)
                self.last_paddle_hit = "computer"
        else:
            self.last_paddle_hit = None  # Reset when not colliding

    def reset_game(self):
        """Reset the game to its initial state."""
        if self.ball.rect.x < 0 or self.ball.rect.x > self.settings.screen_width:
            self.sb.update_scores()
            self.computer.reset_position()
            self.paddle.reset_position()
            self.ball.reset_position()
            sleep(0.5)  # Pause briefly before resetting

    def end_game(self):
        """End the game and display the final score."""
        self.screen.fill(self.settings.screen_bg_color)
        font = pg.font.Font(None, 74)
        again_font = pg.font.Font(None, 48)
        player_win = font.render("Player Wins!", True, (255, 255, 255))
        computer_win = font.render("Computer Wins!", True, (255, 255, 255))
        player_rect = player_win.get_rect(center=(self.settings.screen_width // 2,
                                       self.settings.screen_height // 2))
        computer_rect = computer_win.get_rect(center=(self.settings.screen_width // 2,
                                         self.settings.screen_height // 2))
        play_again_rect = pg.Rect(300, 450, 200, 100)
        play_again_text = again_font.render("Play Again?", True, (255, 255, 255))
            
        waiting = True
        while waiting and self.running:
            self.screen.fill(self.settings.screen_bg_color)
            pg.draw.rect(self.screen, (0,0,200), play_again_rect)
            if self.sb.left_score >= 5:
                self.screen.blit(player_win, player_rect)
            elif self.sb.right_score >= 5:
                self.screen.blit(computer_win, computer_rect)
            self.screen.blit(play_again_text, play_again_text.get_rect(center=play_again_rect.center))
            pg.display.flip()
        

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    waiting - False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if play_again_rect.collidepoint(event.pos):
                        waiting = False
            self.clock.tick(60)   
                    
    def update_screen(self):
        self.screen.fill(self.settings.screen_bg_color)
        pg.draw.rect(self.screen, self.settings.paddle_color, self.paddle.rect)
        self.computer.draw_computer(self.screen)
        self.ball.draw(self.screen)
        self.sb.draw_scoreboard(self.screen)
        pg.display.flip()  # Update the full display Surface to the screen

if __name__ == "__main__":
    game = Pong("Pong Game")
    game.run()
    pg.quit()