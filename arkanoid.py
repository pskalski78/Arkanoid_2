# arkanoid

import pygame
from settings import Settings
from ball import Ball
from stick import Stick
from brick import Brick
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))

    pygame.display.set_caption('Arkanoid_2')

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)


    #the ball
    # ball = Ball(screen, ai_settings)
    stick = Stick(screen, ai_settings)
    #brick = Brick(screen, ai_settings)

    balls = gf.create_balls(Ball, screen, ai_settings, 1)

    wall = gf.create_wall(Brick, screen, ai_settings, 14, 7)



    #game loop
    while True:

        #check events
        gf.check_events(stick)

        gf.update_screen(ai_settings, screen, stick, wall, balls, sb, stats)






if __name__ == "__main__":
    run_game()



