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
platform_buttom = screen_height - platform_height
platform = pygame.Rect(platform_left, platform_buttom, platform_width, platform_height)

# player_rect, потом можно удалить
player_width = 100
player_height = 100
player_rect = pygame.Rect(100, 101, 120, 120)  # what is left?
# left - это координата левой грани нашего прямоугольника

# player_circle, добавляем шарик, который потом можно подправить есть метод Rect.center
center_x = 100
center_y = 100
circle_x_speed = 50
circle_y_speed = 50
circle_radius = 60

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

        screen.fill((123, 25, 45))
        moving_circle()
        #Добавляем платформу, от которой будет отскакивать шарик
        pygame.draw.rect(screen, (0, 0, 0), platform)
        pygame.display.update()
        clock.tick(60)


def moving_circle():
    """
    Функция выполняет движение шарика, и осткакивание его от стен.
    :return: Ничего не возвращает
    """
    global center_x, center_y, circle_y_speed, circle_x_speed
    center_x += circle_x_speed
    center_y += circle_y_speed

    # Отскоки от стенок окна для нашего круга
    if center_x - circle_radius <= 0 or center_x + circle_radius >= screen_width:
        circle_x_speed *= -1
    if center_y - circle_radius <= 0 or center_y + circle_radius >= screen_height:
        circle_y_speed *= -1

    pygame.draw.circle(screen, 'green', (center_x, center_y), circle_radius)


def set_position_from_mouse():
    """Функция устанавливает позицию круга равной позиции мыши"""
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, 'green', pos, circle_radius)


main()