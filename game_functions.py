import sys
import pygame
from pygame.sprite import Group


def check_events(stick):
    """
        Reakcja na zdarzenia generowane przez klawiature i mysz
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or (event.key == pygame.K_RIGHT):
                stick.moving_right = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                stick.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                stick.moving_right = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                stick.moving_left = False


def update_wall(balls, wall,stats, sb, ai_settings):
    for ball in balls:
        if pygame.sprite.spritecollideany(ball, wall):
            # print('Boom')
            ball.dy = -ball.dy
    collisions = pygame.sprite.groupcollide(balls, wall, False, True)
    if collisions:
        stats.score += ai_settings.brick_points
        sb.prep_score()



def update_screen(ai_settings, screen, stick, wall, balls, sb, stats):
    """ uakturalnienie obrazow na ekranie i przejscie do nowego ekranu"""
    # first fill everything with a background color
    screen.fill(ai_settings.bg_color)

    stick.blitme()
    stick.update()

    #wyswietlenie inforamacji o punktacji
    sb.show_score()

    for brick in wall.sprites():
        brick.blitme()

    for ball in balls.sprites():
        ball.blitme()
        ball.update()
        if ball.rect.colliderect(stick.rect):
            ball.dy = -ball.dy

    update_wall(balls, wall,stats, sb, ai_settings)
    pygame.display.flip()

def create_balls(Ball, screen, ai_settings,quantity):
    balls = Group()
    for i in range(quantity):
        ball = Ball(screen, ai_settings)
        balls.add(ball)
    return balls

def create_wall(Brick, screen, ai_settings, columns_nr, row_nr):
    wall = Group()

    brick = Brick(screen, ai_settings)
    brick_width = brick.rect.width
    brick_height = brick.rect.height
    for row in range(row_nr):
        for brick_number in range(columns_nr):
            brick = Brick(screen, ai_settings)
            brick.x = brick_width + 1.5 * brick_width * brick_number
            brick.y = 4 * brick_height + 1.5 * brick_height * row
            brick.rect.x = brick.x
            brick.rect.y = brick.y
            wall.add(brick)

    return wall