class GameStats():
    """ Monitorowanie danych statystycznych w grze arkanoid """

    def __init__(self, ai_settings):
        """ Inicjalizacja danych statystycznych """
        self.ai_settings = ai_settings
        self.reset_status()

    def reset_status(self):
        self.stick_left = self.ai_settings.stick_limit
        self.score = 0

        
