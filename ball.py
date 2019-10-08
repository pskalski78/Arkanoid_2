import pygame
import random
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        """Ball initialization and its initial position"""

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('game_graphics/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


        """midpoint of the ball in float numbers"""
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)


        """ dx dy """
        self.dx, self.dy = random.choice(self.ai_settings.v)

        """ ball speed factor """
        self.ball_speed = self.ai_settings.ball_speed_factor


    def update(self):
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <=0:
            self.dy = -self.dy


        if self.rect.right >= self.screen_rect.right or self.rect.left <=0:
            self.dx = -self.dx

        """ ball position - calculation """

        self.center_x += self.dx * self.ball_speed
        self.center_y += self.dy * self.ball_speed
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y


    def blitme(self):
        """ show ball in actual position """
        self.screen.blit(self.image, self.rect)

