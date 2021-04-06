import pygame
import time

print('Hello From LocalRepositori!')
print('Hello')

value = 99000;

pygame.init()

def main():
    game_loop()

# screen
screen_width = 700
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# planform, платформа - устанавливаем в самом нижу экрана, и по середине
platform_width, platform_height  = 300, 50
platform_left = (screen_width - platform_width) / 2
platform_bottom = screen_height - platform_height
platform_speed = 30

platform_1 = pygame.Rect(platform_left, platform_bottom, platform_width, platform_height)
platform_2 = pygame.Rect(platform_left, 0, platform_width, platform_height)

# player_circle
ball_radius = 30
ball = pygame.Rect(screen_width / 2, 0, 2 * ball_radius, 2 * ball_radius)
ball.center = (screen_width / 2, screen_height / 2)
ball_x_speed = 5
ball_y_speed = 6

# FPS
clock = pygame.time.Clock()


# main game loop
def game_loop():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        # Движение нижней платформы вправо или влево
        if key[pygame.K_RIGHT]:
            moving_platform_right(platform_1)
        if key[pygame.K_LEFT]:
            moving_platform_left(platform_1)

        # движение верхней платформы
        if key[pygame.K_d]:
            moving_platform_right(platform_2)
        if key[pygame.K_a]:
            moving_platform_left(platform_2)

        screen.fill((123, 25, 45))
        moving_circle()

        # Добавляем платформу, от которой будет отскакивать шарик
        pygame.draw.rect(screen, (0, 0, 0), platform_2)
        pygame.draw.rect(screen, (0, 0, 0), platform_1)
        pygame.display.update()
        clock.tick(60)


def moving_circle():
    """
    Функция выполняет движение шарика, и осткакивание его от стен.
    :return: Ничего не возвращает
    """
    global ball, ball_y_speed, ball_x_speed
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    # Отскоки от стенок окна для нашего круга
    if ball.left <= 0 or ball.right >= screen_width:
        ball_x_speed *= -1
    if ball.bottom >= screen_height or ball.top <= 0:
        ball.center = (screen_width / 2, screen_height / 2)


    # collision ball with platform
    possible_distance_collision = 7
    if ball.colliderect(platform_1) or ball.colliderect(platform_2):
        if abs(ball.bottom - platform_1.top) <= possible_distance_collision:
            ball_y_speed *= -1
        if abs(ball.top - platform_2.bottom) <= possible_distance_collision:
            ball_y_speed *= -1

    pygame.draw.circle(screen, 'green', ball.center, ball_radius)
    pygame.draw.line(screen, 'black', (0, screen_height / 2), ( screen_width,  screen_height / 2))


def moving_platform_right(platform):
    """Передвигает платформу вправо, """

    if platform.right >= screen_width:
        return
    else:
        platform.x += platform_speed


def moving_platform_left(platform):
    """Передвигает платформу влево"""
    if platform.left <= 0:
        return
    else:
        platform.x -= platform_speed

main()