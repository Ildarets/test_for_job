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
aircrafts = 5
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


class Aircraft():
    """ Созданеи самолета"""
    c = 0
    color = RED

    # def __init__(self, position):
    #     self._rect_cannon = pg.Rect(0, 0, 20 * 2, 28 * 2)
    #     self._rect_cannon.center = position
    #     self._angle_cannon = 0


    def __init__(self, x, y, dir, long_iter):
        """ Конструктор самолета"""
        self.dir = dir
        self.long_iter = long_iter
        self.x = x
        self.y = y
        self.rect_aircraft = pygame.Rect(x, y, 20,20)



    def direct_air(self, dir):
        """ Direct aircraft"""
        self.dir = dir

    def rect_air(self, x, y):
        """Create rectangle of aicraft"""
        rect =   pygame.Rect(x, y, 20, 20)
        return rect

    def color_air(self,color):
        """ Color of aircraft"""
        self.color = RED

    def coun_iter(self):
        """Count iteration flying aircraft"""
        self.c += 1

    def long_iteration(self):
        """ Long flying of aircraft to choice direct"""
        iter_ = random.randint(10, 50)
        return iter_



"""Create box of aircrafts"""
boxes = []
for i in range(aircrafts):
    x_coord = random.randint(0, WINDOWWIDTH)
    y_coord = random.randint(0, WINDOWHEIGHT)
    direct = random.choice([UP, DOWNRIGHT, DOWN, DOWNLEFT, UPRIGHT, UPLEFT, LEFT, RIGHT])
    long_iter = random.randint(5, 20)
    air = Aircraft(x_coord, y_coord, direct,long_iter)
    boxes.append(air)



while True:
    # Проверка наличия события QUIT
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for air in boxes:







