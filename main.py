import numpy as np
import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((500, 750))

BACKGROUND_IMAGE = pygame.image.load('background.jpg')

BIRD_IMAGE = pygame.image.load('самолет-removebg-preview.png').convert_alpha()
bird_x = 50
bird_y = 300
bird_y_change = 0


def display_bird(x, y):
    SCREEN.blit(BIRD_IMAGE, (x, y))


OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150, 399)
OBSTACLE_COLOR = (15, 230, 15)
OBSTACE_X_CHANGE = -0.3
OBSTACLE_DISTANCE = 150
obstacle_x = 500


def collision_detection(obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False


score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)


def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
    SCREEN.blit(display, (10, 10))


startFont = pygame.font.Font('freesansbold.ttf', 32)


def start():
    # display = startFont.render(f"Нажми пробел для старта", True, (255, 255, 255))
    # SCREEN.blit(display, (20, 200))
    pygame.display.update()


score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)


def game_over():
    maximum = max(score_list)

    display1 = game_over_font1.render(f"GAME OVER", True, (200, 35, 35))
    SCREEN.blit(display1, (50, 300))

    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))

    if score == maximum:
        display3 = game_over_font2.render(f"Новый рекодр!!!", True, (200, 35, 35))
        SCREEN.blit(display3, (80, 100))


running = True

waiting = True

collision = False

obstacle_image = pygame.image.load('здание.png')

xrenx = obstacle_x


def display_obstacle(OBSTACLE_HEIGHT):
    if OBSTACLE_HEIGHT < 400:
        xrenx = 0 - (400 - OBSTACLE_HEIGHT)

    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    bottom_obstacle_height = 750 - OBSTACLE_HEIGHT - 150
    # pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x - 10, height - 20, OBSTACLE_WIDTH * 1.3, 35))
    SCREEN.blit(obstacle_image, (obstacle_x - 10, xrenx))
    shopa = OBSTACLE_HEIGHT + 150
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, shopa, OBSTACLE_WIDTH, bottom_obstacle_height))
    # pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x - 10, shopa , OBSTACLE_WIDTH *1.3, 35))
    SCREEN.blit(obstacle_image, (obstacle_x - 10, shopa))


i = 0
some = random.random()

b1 = random.random()
b2 = random.random()
b3 = random.random()

tr1 = int(bird_y)
tr2 = int(obstacle_x)
tr3 = int(OBSTACLE_HEIGHT)

Summ = tr1 * b1 + tr2 * b2 + tr3 * b3 + some

arr = [b1, b2, b3, some, score]


def Sigmoid():
    sigmoid = 1 / (1 + np.exp(-tr1))
    return sigmoid * (Summ)


while running:
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

    while waiting:
        if collision:
            game_over()
            start()

            print(arr)
            b1 = random.random()
            b2 = random.random()
            b3 = random.random()
            Summ = tr1 * b1 + tr2 * b2 + tr3 * b3 + some
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    bird_y = 300
                    obstacle_x = 500
                    waiting = False
            if event.type == pygame.QUIT:
                waiting = False
                running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # BIRD_IMAGE = pygame.transform.rotate(BIRD_IMAGE, 30)
                # SCREEN.blit(BIRD_IMAGE, (bird_x, bird_y))
                bird_y_change = -0.4
                # bird_y = bird_y - 30
                # BIRD_IMAGE = pygame.transform.rotate(BIRD_IMAGE, 60)
                # SCREEN.blit(BIRD_IMAGE, (bird_x, bird_y))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                # BIRD_IMAGE = pygame.transform.rotate(BIRD_IMAGE, 330)
                # SCREEN.blit(BIRD_IMAGE, (bird_x, bird_y))
                bird_y_change = 0.3
                # BIRD_IMAGE = pygame.transform.rotate(BIRD_IMAGE, 330)
                # SCREEN.blit(BIRD_IMAGE, (bird_x, bird_y))

    bird_y += bird_y_change

    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 570:
        bird_y = 570
        game_over()
        score_list.append(score)

    obstacle_x += OBSTACE_X_CHANGE
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + OBSTACLE_DISTANCE)

    if collision:
        score_list.append(score)
        waiting = True

    if obstacle_x <= -1:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1

    display_obstacle(OBSTACLE_HEIGHT)
    display_bird(bird_x, bird_y)
    score_display(score)
    pygame.display.update()

    if Sigmoid() <= 0.75:
        bird_y = bird_y - 30

pygame.quit()
