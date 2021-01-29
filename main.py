import pygame

pygame.init()


# player
class Player():
    pass

player_width = 100
player_height = 100
player = pygame.Rect(100, 100, 110, 120)


# screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


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
        pygame.draw.rect(screen, (154, 222, 223), player)
        pygame.display.update()

game_loop()
