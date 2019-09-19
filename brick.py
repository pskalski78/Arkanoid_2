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
        self.rect.x = 1*self.rect.width
        self.rect.y = 1*self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """ show the brick """
        self.screen.blit(self.image, self.rect)



