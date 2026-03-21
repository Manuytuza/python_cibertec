import pygame
import random

# Inicializar pygame
pygame.init()

# 🔹 Dimensiones de la ventana
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Sr Manuel")

# 🔹 Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 🔹 Variables del juego
snake_block = 20
snake_speed = 10

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 35)

# Función para mostrar mensajes
def mensaje(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [WIDTH/6, HEIGHT/3])

# 🔹 Loop principal
def gameLoop():
    game_over = False
    game_close = False

    # Posición inicial de la snake
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Posición inicial de la comida
    foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            win.fill(BLACK)
            mensaje("¡Perdiste! C-Continuar o Q-Salir", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # 🔹 Actualizar posición
        x1 += x1_change
        y1 += y1_change

        # 🌟 Wrap around - atraviesa paredes
        if x1 >= WIDTH:
            x1 = 0
        elif x1 < 0:
            x1 = WIDTH - snake_block
        if y1 >= HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = HEIGHT - snake_block

        win.fill(BLACK)
        pygame.draw.rect(win, RED, [foodx, foody, snake_block, snake_block])

        # 🐍 Cuerpo de la snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Colisión consigo misma
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Dibujar snake
        for block in snake_list:
            pygame.draw.rect(win, GREEN, [block[0], block[1], snake_block, snake_block])

        pygame.display.update()

        # 🥩 Comer comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 🔹 Ejecutar juego
gameLoop()