import pygame.font

class Scoreboard():
    """ klasa przeznaczona do przedstawiania informacji o punktacji"""
    def __init__(self, ai_settings, screen, stats):
        """ inicjalizacja atrybutow dotyczacych punktacji"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.ai_settings = ai_settings

        #ustawienia czcionki dla informacji dotyczących punktacji
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #przygotowanie początkowych obrazow z punktacja
        self.prep_score()

    def prep_score(self):
        """ przekształcenie punkacji na wygenerowany obraz"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #wyswietlenie informacji w prawym górnym roogu ekranu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 10

    def show_score(self):
        """wyswietlenie punktacji na krenie """
        self.screen.blit(self.score_image, self.score_rect)


