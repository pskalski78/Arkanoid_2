import pygame
from pygame.sprite import Sprite

class Brick(Sprite):
    """ Class brick """

    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """ load image and define image rect """
        self.image = pygame.image.load('game_graphics/brick1.png')
        self.rect = self.image.get_rect()

        """ brick location """
        self.rect.centerx = self.rect.width
        self.rect.centery = 3*self.rect.height

        self.center_x = float(self.rect.centerx)

    def blitme(self):
        """ show the brick """
        self.screen.blit(self.image, self.rect)



