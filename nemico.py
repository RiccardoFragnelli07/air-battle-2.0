import pygame
from random import randint

WIDTH, HEIGHT = 500, 700
VEL = 7


nemico1_x, nemico1_y, dim_nemico1_x, dim_nemico1_y = 0, 0, 50, 50       # Fighter
nemico2_x, nemico2_y, dim_nemico2_x, dim_nemico2_y = 0, 0, 50, 50       # Bomber
nemico3_x, nemico3_y, dim_nemico3_x, dim_nemico3_y = 0, 0, 80, 80       # Torpedo
nemico4_x, nemico4_y, dim_nemico4_x, dim_nemico4_y = 0, 0, 80, 80       # Frigate
nemico5_x, nemico5_y, dim_nemico5_x, dim_nemico5_y = 0, 0, 120, 120     # Battlecruiser
nemico6_x, nemico6_y, dim_nemico6_x, dim_nemico6_y = 0, 0, 120, 120     # Dreadnought

diz = {0 : pygame.Rect(nemico1_x, nemico1_y, dim_nemico1_x, dim_nemico1_y), 
       1 : pygame.Rect(nemico2_x, nemico2_y, dim_nemico2_x, dim_nemico2_y),
       2 : pygame.Rect(nemico3_x, nemico3_y, dim_nemico3_x, dim_nemico3_y),
       3 : pygame.Rect(nemico4_x, nemico4_y, dim_nemico4_x, dim_nemico4_y),
       4 : pygame.Rect(nemico5_x, nemico5_y, dim_nemico5_x, dim_nemico5_y),
       5 : pygame.Rect(nemico6_x, nemico6_y, dim_nemico6_x, dim_nemico6_y)}


class Nemico:
    def __init__(self, time, texture):
        self.time = time
        if self.time >= 0 and self.time <= 30:
            navicella = randint(0, 1)
        elif self.time > 30 and self.time <= 60:
            navicella = randint(0, 3)
        else:
            num = randint(1, 100)
            if num >= 1 and num <= 30:
                navicella = randint(0, 1)
            elif num > 30 and num <= 80:
                navicella = randint(2, 3)
            else:
                navicella = randint(4, 5)
                
        self.rect = diz[navicella]
        self.img = texture[navicella][randint(0, 1)]
        
        self.rect.y = 0
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.arrivo = randint(0, WIDTH - self.rect.width)


def move_nemico(lista):
    temp = []
    for nemico in lista:
        nemico.rect.y += VEL
    for nemico in lista:
        if nemico.rect.y < HEIGHT:
            temp.append(nemico)

    return temp

def draw_nemico(lista, screen):
    for nemico in lista:
        screen.blit(nemico.img, (nemico.rect.x, nemico.rect.y))