import math

class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawien gry"""

    def __init__(self):
        """Inicjalizacja ustawien gry"""
        #ustawienia ekranu
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = 230, 230, 230




        #ball speed settings
        self.ball_speed_factor = .5

        #stick speed settings
        self.stick_speed_factor = .4
        self.stick_limit = 3

        self.brick_points = 20

        m = 2 * math.pi / 360
        self.v = [(math.sin(m * degree), math.cos(m * degree)) for degree in range(10, 360, 10)]



