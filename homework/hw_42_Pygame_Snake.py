#Продолжить разработку игры. Доработать еду для змейки(змейка увеличивается при поедании чего-нибудь)
# По желанию добавить:
# -Фон
# -Счётчик очков

import pygame
import random

pygame.init()
WINDOW = 600
STEP = 20
x1 = 300
y1 = 300
lenght = 1
snake = [(x1,y1)]
score = 0
fps = 10

x2 = 360
y2 = 300
# apple = (x2,y2)

x1_change = 0
y1_change = 0

white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)

dis = pygame.display.set_mode((WINDOW, WINDOW)) #задание началного окна
pygame.display.set_caption("Snake")
game_over = False

img = pygame.image.load('2.jpg').convert()
font_score = pygame.font.SysFont('Arial', 26, bold=True) #шрифт для подсчёта очков
clock = pygame.time.Clock() #создать объект, чтобы помочь отслеживать время

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN: #нажатие клавиш
            if event.key == pygame.K_LEFT:
                x1_change = -STEP
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = STEP
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -STEP
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = STEP


    if x1>WINDOW-STEP or x1<0 or y1>WINDOW-STEP or y1<0:
        game_over = True
    if len(snake) != len(set(snake)): #нельзя себя кушать и соответственно нельзя нажимать кнопки противохода
        game_over = True


    dis.blit(img,(0,0)) # фоновая картинка и кординаты ее вставки
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('white'))  # рендерим надпись с очками
    dis.blit(render_score, (5, 5))  # закрепление надписи в верхнем левом углу

    [pygame.draw.rect(dis, blue, [x1, y1, STEP-1, STEP-1]) for x1, y1 in snake]
    pygame.draw.rect(dis, red, [x2, y2, STEP, STEP])
    x1 += x1_change
    y1 += y1_change
    snake.append((x1,y1))
    snake = snake[-lenght:] #срез по данной длинне змеи
    if snake[-1] == (x2,y2):
        x2 = random.randint(0,int(WINDOW/STEP)-2) * STEP #так замудрено что бы яблоко было в пределах поля
        y2 = random.randint(0, int(WINDOW/STEP)-2) * STEP
        lenght +=1
        score +=1
        fps+=1



    pygame.display.update()

    clock.tick(fps) #частота кадров в секунду и обновить

pygame = quit()
quit()