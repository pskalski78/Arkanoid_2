# arkanoid

import sys, pygame, math
from settings import Settings
from ball import Ball
from stick import Stick
from brick import Brick

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))

    pygame.display.set_caption('Arkanoid')

    #the ball
    # ball = Ball(screen, ai_settings)
    stick = Stick(screen, ai_settings)
    brick = Brick(screen, ai_settings)

    balls = []
    for i in range(3):
        ball = Ball(screen,ai_settings)
        balls.append(ball)

    #game loop
    while True:

        #check event
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q)  :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    stick.moving_right = True
                elif event.key == pygame.K_a:
                    stick.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    stick.moving_right = False
                elif event.key == pygame.K_a:
                    stick.moving_left = False



        #first fill everything with a background color
        screen.fill(ai_settings.bg_color)

        # ball.update()
        # ball.blitme()



        stick.blitme()
        stick.update()

        brick.blitme()

        for ball in balls:
            ball.update()
            ball.blitme()
            if ball.rect.colliderect(stick.rect):
                ball.dy = -ball.dy

        # now the surface is ready, tell pygame to display it!
        pygame.display.flip()



if __name__ == "__main__":
    run_game()


