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


# Выбор случайного направления самолета
def direct_air(dir, c1, long_iter, lost_vec, vec_air1):
    if c1 == long_iter:
        # Делаем полет более реальным, выбор направления полета в зависимости от текущего направления
        if lost_vec == 0:
            vec_air1 = random.choice([7, 0, 1])
        elif lost_vec == 1:
            vec_air1 = random.choice([0, 1, 2])
        elif lost_vec == 2:
            vec_air1 = random.choice([1, 2, 3])
        elif lost_vec == 3:
            vec_air1 = random.choice([2, 3, 4])
        elif lost_vec == 4:
            vec_air1 = random.choice([3, 4, 5])
        elif lost_vec == 5:
            vec_air1 = random.choice([4, 5, 6])
        elif lost_vec == 6:
            vec_air1 = random.choice([5, 6, 7])
        elif lost_vec == 7:
            vec_air1 = random.choice([6, 7, 0])

        if vec_air1 == 0:
            dir = UP
        elif vec_air1 == 1:
            dir = UPRIGHT
        elif vec_air1 == 2:
            dir = RIGHT
        elif vec_air1 == 3:
            dir = DOWNRIGHT
        elif vec_air1 == 4:
            dir = DOWN
        elif vec_air1 == 5:
            dir = DOWNLEFT
        elif vec_air1 == 6:
            dir = LEFT
        elif vec_air1 == 7:
            dir = UPLEFT
        c1 = 0
        lost_vec = vec_air1
        long_iter = random.randint(10, 30)
    return dir, c1, lost_vec, long_iter



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

# Перемещение ракет.
def move_rockets(dir, rect_r):
    if dir == DOWNLEFT:
        rect_r.centerx -= MOVESPEED2
        rect_r.centery += MOVESPEED2
    elif dir == DOWNRIGHT:
        rect_r.centerx += MOVESPEED2
        rect_r.centery += MOVESPEED2
    elif dir == UPLEFT:
        rect_r.centerx -= MOVESPEED2
        rect_r.centery -= MOVESPEED2
    elif dir == UPRIGHT:
        rect_r.centerx += MOVESPEED2
        rect_r.centery -= MOVESPEED2
    elif dir == DOWN:
       rect_r.centery += MOVESPEED2
    elif dir == UP:
        rect_r.centery -= MOVESPEED2
    elif dir == LEFT:
        rect_r.centerx += MOVESPEED2
    elif dir == RIGHT:
        rect_r.centerx -= MOVESPEED2

# Создание класса Локатор
class Locator:
    def loc_coord(x, y):
        return pygame.Rect(x, y, 100, 100)
    loc_color =  WHITE_R

# Создание класса самолет
class Aircraft():
    """ Созданеи самолета"""
    def __init__(self, rect, dir, color, long_iter, lost_vec):
        """ Конструктор самолета"""
        self.rect = rect
        self.dir = dir
        self.color = color
        self.long_iter = long_iter
        self.lost_vec = lost_vec

    def direct_air(self, dir):
        self.dir = dir



    x_coord = random.randint(0, WINDOWWIDTH)
    y_coord = random.randint(0, WINDOWHEIGHT)
    direct = random.choice([UP, DOWNRIGHT, DOWN, DOWNLEFT, UPRIGHT, UPLEFT, LEFT, RIGHT])
    rect = pygame.Rect(x_coord, y_coord, 20, 20)
    color =  RED
    dir = direct
    long_iter = long_iter
    lost_vec = lost_vec
    c1 = c1
    locator = Locator.loc_coord(x_coord, y_coord)
    locator_color = Locator.loc_color

class Rockets:
    def rocket_rect (dir):
        rect_r = pygame.Rect((roket_coord(b.dir)), (5, 5))
        return rect_r
    color = BLUE
    def direct_rocket(dir):
        direct_rock = b.dir
        return direct_rock
    long_iter = 100
    c1 = c1


# Делаем локаторы.
def locator_dir(dir):
    if dir == UP:
        b.locator.midbottom = b.rect.midtop
    if dir == DOWN:
        b.locator.midtop = b.rect.midbottom
    if b.dir == LEFT:
        b.locator.midleft = b.rect.midright
    if b.dir == RIGHT:
        b.locator.midright = b.rect.midleft
    if dir == UPLEFT:
        b.locator.bottomright = b.rect.topleft
    if dir == UPRIGHT:
        b.locator.bottomleft = b.rect.topright
    if dir == DOWNLEFT:
        b.locator.topright = b.rect. bottomleft
    if dir == DOWNRIGHT:
        b.locator.topleft = b.rect.bottomright

# Создание структуры данных блока
boxes = []
rockets = []
for i in range(0, aircrafts):
    b = Aircraft()
    boxes.append(b)

while True:
    # Проверка наличия события QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # Выбор случайного направления самолета 1
    for b in boxes:
        direct_air(b.dir, b.c1, b.long_iter, b.lost_vec, vec_air1)
        locator_dir(b.dir)
        # Создание блока на поверхности
        pygame.draw.rect(windowSurface, b.color, b.rect)
        pygame.draw.rect(windowSurface, b.locator_color, b.locator)

    for i in range(len(boxes) - 1):
        for b in boxes:
            if boxes[i].rect.colliderect(b.locator):
                r = Rockets()
                rockets.append(r)

    for r in rockets:
        move_rockets(r.direct_rocket(dir), r.rect_r)


    # Создание на поверхности белого фона.
    windowSurface.fill(WHITE)
    # Перемещение структуры данных блока.

    pygame.display.update()
    time.sleep(0.01)




