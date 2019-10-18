import pygame, sys, time, random, math
from pygame.locals import *

# Устнановка pygame
pygame.init()

# Настройка окна
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Анимация')

# Количество самолетов
aircrafts = 10

# Функция  выбора координат выстрела ракеты
def roket_coord(dir):
    global roc_shot
    if dir == UP:
        roc_shot = b['rect'].midtop
    if b['dir'] == DOWN:
        roc_shot = b['rect'].midbottom
    if b['dir'] == LEFT:
        roc_shot = b['rect'].midright
    if b['dir'] == RIGHT:
        roc_shot = b['rect'].midleft
    if b['dir'] == UPLEFT:
        roc_shot = b['rect'].topleft
    if b['dir'] == UPRIGHT:
        roc_shot = b['rect'].topright
    if b['dir'] == DOWNLEFT:
        roc_shot = b['rect'].bottomleft
    if b['dir'] == DOWNRIGHT:
        roc_shot = b['rect'].bottomright
    return roc_shot

# Создание переменных направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


MOVESPEED1 = 2
MOVESPEED2 = 5

# Настройка цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE_R = (255, 255, 230)

# Для имитации движения
c1 = 0
lost_vec = random.randint(5, 20)
long_iter = random.randint(5, 20)
long_iter2 = random.randint(5, 20)
vec_air1 = 4
vec_air2 = 7

# Создание структуры данных блока
boxes = []
rockets = []
for i in range(aircrafts):
    x_coord = random.randint(0, WINDOWWIDTH)
    y_coord = random.randint(0, WINDOWHEIGHT)
    direct = random.choice([UP, DOWNRIGHT, DOWN, DOWNLEFT, UPRIGHT, UPLEFT, LEFT, RIGHT])
    b = {'rect': pygame.Rect(x_coord, y_coord, 20, 20),
         'color': RED,
         'dir': direct,
         'long_iter': long_iter,
         'lost_vec': lost_vec,
         'c1':c1,
         'locator':{'rect_loc': pygame.Rect(x_coord, y_coord, 100, 100),
                    'loc_color': WHITE_R}}
    boxes.append(b)

# Запуск игрового цикла
while True:
    # Проверка наличия события QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # Выбор случайного направления самолета 1
    for b in boxes:
        if b['c1'] == b['long_iter']:
        # Делаем полет более реальным, выбор направления полета в зависимости от текущего направления
            if b['lost_vec'] == 0:
                vec_air1 = random.choice([7, 0, 1])
            elif b['lost_vec'] == 1:
                vec_air1 = random.choice([0, 1, 2])
            elif b['lost_vec'] == 2:
                vec_air1 = random.choice([1, 2, 3])
            elif b['lost_vec'] == 3:
                vec_air1 = random.choice([2, 3, 4])
            elif b['lost_vec'] == 4:
                vec_air1 = random.choice([3, 4, 5])
            elif b['lost_vec'] == 5:
                vec_air1 = random.choice([4, 5, 6])
            elif b['lost_vec'] == 6:
                vec_air1 = random.choice([5, 6, 7])
            elif b['lost_vec'] == 7:
                vec_air1 = random.choice([6, 7, 0])

            if vec_air1 == 0:
                b['dir'] = UP
            elif vec_air1 == 1:
                b['dir'] = UPRIGHT
            elif vec_air1 == 2:
                b['dir'] = RIGHT
            elif vec_air1 == 3:
                b['dir'] = DOWNRIGHT
            elif vec_air1 == 4:
                b['dir'] = DOWN
            elif vec_air1 == 5:
                b['dir'] = DOWNLEFT
            elif vec_air1 == 6:
                b['dir'] = LEFT
            elif vec_air1 == 7:
                b['dir'] = UPLEFT

            b['c1'] = 0
            b['lost_vec'] = vec_air1
            b['long_iter'] = random.randint(10, 30)
        else:
            continue


    # Создаем ракету
    # Условия запуска ракеты. Если по направлению движения самолета летит другой самолет.
    # Делаем локаторы.
    for b in boxes:
        if b['dir'] == UP:
            b['locator']['rect_loc'].midbottom = b['rect'].midtop
        if b['dir'] == DOWN:
            b['locator']['rect_loc'].midtop = b['rect'].midbottom
        if b['dir'] == LEFT:
            b['locator']['rect_loc'].midleft = b['rect'].midright
        if b['dir'] == RIGHT:
            b['locator']['rect_loc'].midright = b['rect'].midleft
        if b['dir'] == UPLEFT:
            b['locator']['rect_loc'].bottomright = b['rect'].topleft
        if b['dir'] == UPRIGHT:
            b['locator']['rect_loc'].bottomleft = b['rect'].topright
        if b['dir'] == DOWNLEFT:
            b['locator']['rect_loc'].topright = b['rect'].bottomleft
        if b['dir'] == DOWNRIGHT:
            b['locator']['rect_loc'].topleft = b['rect'].bottomright


    # Проверяем попадание каждого самолета в поле локатора другого. Если самолет попадает в локатор то запускается ракета.
    for i in range(len(boxes)-1):
        for b in boxes:
            if boxes[i]['rect'].colliderect(b['locator']['rect_loc']):
                r = {'rect_r': pygame.Rect((roket_coord(b['dir'])),( 5, 5)),
                     'color': BLUE,
                     'dir': b['dir'],
                     'long_iter': 100,
                     'c1': c1,
                     }
                rockets.append(r)


    for r in rockets:
        # Перемещение ракет.
        if r['dir'] == DOWNLEFT:
            r['rect_r'].centerx -= MOVESPEED2
            r['rect_r'].centery += MOVESPEED2
        elif r['dir'] == DOWNRIGHT:
            r['rect_r'].centerx += MOVESPEED2
            r['rect_r'].centery += MOVESPEED2
        elif r['dir'] == UPLEFT:
            r['rect_r'].centerx -= MOVESPEED2
            r['rect_r'].centery -= MOVESPEED2
        elif r['dir'] == UPRIGHT:
            r['rect_r'].centerx += MOVESPEED2
            r['rect_r'].centery -= MOVESPEED2
        elif r['dir'] == DOWN:
           r['rect_r'].centery += MOVESPEED2
        elif r['dir'] == UP:
            r['rect_r'].centery -= MOVESPEED2
        elif r['dir'] == LEFT:
            r['rect_r'].centerx += MOVESPEED2
        elif r['dir'] == RIGHT:
            r['rect_r'].centerx -= MOVESPEED2



    # Создание на поверхности белого фона.
    windowSurface.fill(WHITE)

    for b in boxes:

        # Перемещение структуры данных блока.
        if b['dir'] == DOWNLEFT:
            b['rect'].centerx -= MOVESPEED1
            b['rect'].centery += MOVESPEED1
            b['locator']['rect_loc'].centerx -= MOVESPEED1
            b['locator']['rect_loc'].centery += MOVESPEED1
        elif b['dir'] == DOWNRIGHT:
            b['rect'].centerx += MOVESPEED1
            b['rect'].centery += MOVESPEED1
            b['locator']['rect_loc'].centerx += MOVESPEED1
            b['locator']['rect_loc'].centery += MOVESPEED1
        elif b['dir'] == UPLEFT:
            b['rect'].centerx -= MOVESPEED1
            b['rect'].centery -= MOVESPEED1
            b['locator']['rect_loc'].centerx -= MOVESPEED1
            b['locator']['rect_loc'].centery -= MOVESPEED1
        elif b['dir'] == UPRIGHT:
            b['rect'].centerx += MOVESPEED1
            b['rect'].centery -= MOVESPEED1
            b['locator']['rect_loc'].centerx += MOVESPEED1
            b['locator']['rect_loc'].centery -= MOVESPEED1
        elif b['dir'] == DOWN:
           b['rect'].centery += MOVESPEED1
           b['locator']['rect_loc'].centery += MOVESPEED1
        elif b['dir'] == UP:
            b['rect'].centery -= MOVESPEED1
            b['locator']['rect_loc'].centery -= MOVESPEED1
        elif b['dir'] == LEFT:
            b['rect'].centerx += MOVESPEED1
            b['locator']['rect_loc'].centerx += MOVESPEED1
        elif b['dir'] == RIGHT:
            b['rect'].centerx -= MOVESPEED1
            b['locator']['rect_loc'].centerx -= MOVESPEED1


        # Проверка, переместился ли блок за пределы окна.
        if b['rect'].top < 0:
            # Прохождение блока через верхнюю границу.
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UP:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            # Прохождени блока через нижнюю границу.
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
            if b['dir'] == DOWN:
                b['dir'] = UPLEFT
        if b['rect'].left < 0:
            # Прохождени блока через левую границу.
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
            if b['dir'] == LEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # Прохождени блока через правую границу.
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
            if b['dir'] == RIGHT:
                b['dir'] = DOWNLEFT



        # Создание блока на поверхности
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
        pygame.draw.rect(windowSurface, b['locator']['loc_color'], b['locator']['rect_loc'])

    for r in rockets:
        for b in boxes:
            if b['rect'].colliderect(r['rect_r']):
                boxes.remove(b)

    for r in rockets:
        pygame.draw.rect(windowSurface, r['color'], r['rect_r'])


    for b in boxes:
        b['c1'] += 1


    # Вывод окна на экран.
    pygame.display.update()
    time.sleep(0.01)









