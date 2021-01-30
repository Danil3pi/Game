import pygame

pygame.init()

# screen
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# planform, платформа - устанавливаем в самом нижу экрана, и по середине
platform_width = 400
platform_height = 50
platform_left = (screen_width - platform_width) / 2
platform_bottom = screen_height - platform_height
platform_speed = 20

platform_1 = pygame.Rect(platform_left, platform_bottom, platform_width, platform_height)

# player_circle, добавляем шарик, который потом можно подправить есть метод Rect.center
circle_radius = 30
circle = pygame.Rect(screen_width / 2, 0, 2 * circle_radius, 2 * circle_radius)
circle.center = (screen_width / 2, circle_radius)
circle_x_speed = 5
circle_y_speed = 6

# FPS
clock = pygame.time.Clock()


def main():
    game_loop()


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
        # Движение платформы вправо или влево
        if key[pygame.K_RIGHT]:
            moving_platform_right()
        if key[pygame.K_LEFT]:
            moving_platform_left()

        screen.fill((123, 25, 45))
        moving_circle()

        # Добавляем платформу, от которой будет отскакивать шарик
        pygame.draw.rect(screen, (0, 0, 0), platform_1)
        pygame.display.update()
        clock.tick(60)


def moving_circle():
    """
    Функция выполняет движение шарика, и осткакивание его от стен.
    :return: Ничего не возвращает
    """
    global circle, circle_y_speed, circle_x_speed
    circle.x += circle_x_speed
    circle.y += circle_y_speed

    # Отскоки от стенок окна для нашего круга
    if circle.left <= 0 or circle.right >= screen_width:
        circle_x_speed *= -1
    if circle.top <= 0:
        circle_y_speed *= -1
    if circle.bottom >= screen_height:
        pygame.quit()

    # collision ball with platform
    possible_distance_collision = 5
    if circle.colliderect(platform_1):
        if abs(circle.bottom - platform_1.top) <= possible_distance_collision:
            circle_y_speed *= -1

    pygame.draw.circle(screen, 'green', circle.center, circle_radius)
    pygame.draw.line(screen, 'black', (screen_width / 2, 0), (screen_width / 2, screen_height))


def set_position_from_mouse():
    """Функция устанавливает позицию круга равной позиции мыши"""
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, 'green', pos, circle_radius)


def moving_platform_right():
    """Передвигает платформу вправо"""
    platform_1.x += platform_speed


def moving_platform_left():
    """Передвигает платформу влево"""
    platform_1.x -= platform_speed


main()
