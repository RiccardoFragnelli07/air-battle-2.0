import pygame
import math
from random import randint
from funzioni import genera_navicella

WIDTH, HEIGHT = 500, 700
VEL = 5
PIGRECO = math.pi


nemico1_x, nemico1_y, dim_nemico1_x, dim_nemico1_y = 0, 0, 70, 70       # Scout
nemico2_x, nemico2_y, dim_nemico2_x, dim_nemico2_y = 0, 0, 70, 70       # Bomber
nemico3_x, nemico3_y, dim_nemico3_x, dim_nemico3_y = 0, 0, 90, 90       # Frigate
nemico4_x, nemico4_y, dim_nemico4_x, dim_nemico4_y = 0, 0, 130, 130     # Cruiser
nemico6_x, nemico6_y, dim_nemico6_x, dim_nemico6_y = 0, 0, 200, 200     # Heavycruiser
nemico5_x, nemico5_y, dim_nemico5_x, dim_nemico5_y = 0, 0, 200, 200     # Battleship
nemico7_x, nemico7_y, dim_nemico7_x, dim_nemico7_y = 0, 0, 220, 220,    # Mothership 
nemico8_x, nemico8_y, dim_nemico8_x, dim_nemico8_y = 0, 0, 220, 220,    # Spacestation          

arr = [[nemico1_x, nemico1_y, dim_nemico1_x, dim_nemico1_y],
       [nemico2_x, nemico2_y, dim_nemico2_x, dim_nemico2_y],
       [nemico3_x, nemico3_y, dim_nemico3_x, dim_nemico3_y],
       [nemico4_x, nemico4_y, dim_nemico4_x, dim_nemico4_y],
       [nemico5_x, nemico5_y, dim_nemico5_x, dim_nemico5_y],
       [nemico6_x, nemico6_y, dim_nemico6_x, dim_nemico6_y],
       [nemico7_x, nemico7_y, dim_nemico7_x, dim_nemico7_y],
       [nemico8_x, nemico8_y, dim_nemico8_x, dim_nemico8_y]]

rectv = [[22, nemico1_y, dim_nemico1_x - 55, dim_nemico1_y],
        [24, nemico2_y, dim_nemico2_x - 51, dim_nemico2_y],
        [74, nemico3_y, dim_nemico3_x - 149, dim_nemico3_y],
        [49, nemico4_y, dim_nemico4_x - 99, dim_nemico4_y],
        [44, nemico5_y, dim_nemico5_x - 89, dim_nemico5_y],
        [34, nemico6_y, dim_nemico6_x - 74, dim_nemico6_y],
        [40, nemico7_y, dim_nemico7_x - 81, dim_nemico7_y],
        [0, nemico8_y, dim_nemico8_x, dim_nemico8_y]]


health = [1, 1, 2, 3, 4, 6, 6]


class Nemico:
    def __init__(self, time, texture):
        self.time = time
        num = genera_navicella(self.time)   
        self.rect = pygame.Rect(arr[num][0], arr[num][1], arr[num][2], arr[num][3])
        self.rectv = pygame.Rect(rectv[num][0], rectv[num][1], rectv[num][2], rectv[num][3])
        self.img = texture[num]
        self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
        self.tipo_img = num
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rectv.x = self.rect.x + rectv[num][0]
        self.arrivo = randint(0, WIDTH - self.rect.width)
        self.health = health[num]
        self.esplosioni = []
        self.centro = pygame.math.Vector2(self.rectv.x + (self.rectv.width // 2), self.rectv.y + (self.rectv.height // 2))
        # self.rect.x = WIDTH
        # self.rectv.x = self.rect.x + rectv[num][0]
        
        self.jet = []
        
        cat2 = self.arrivo - self.rect.x
        if cat2 != 0:
            alfa = math.atan(abs(HEIGHT / cat2))
            self.velx = VEL * math.cos(alfa)
            self.vely = VEL * math.sin(alfa)
            self.alfa = alfa
        else:
            self.velx = 0
            self.vely = VEL
            self.alfa = math.radians(90)
        if cat2 < 0:
            self.velx *= -1
                
        

def move_nemico(lista):
    temp = []
    for nemico in lista:
        nemico.rect.x += nemico.velx
        nemico.rect.y += nemico.vely
        nemico.rectv.x += nemico.velx
        nemico.rectv.y += nemico.vely
        # nemico.rect.y += VEL
        # nemico.rectv.y += VEL
    for nemico in lista:
        if nemico.rect.y <= HEIGHT:
            temp.append(nemico)

    return temp

def draw_nemico(lista, screen):
    for nemico in lista:
        screen.blit(nemico.img, (nemico.rect.x, nemico.rect.y))