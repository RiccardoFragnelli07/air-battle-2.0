import pygame
import math
from random import randint
from funzioni import genera_navicella, crea_posizioni, calcola_direzione

WIDTH, HEIGHT = 500, 700
VEL = 5
PIGRECO = math.pi


nemico1_x, nemico1_y, dim_nemico1_x, dim_nemico1_y = 0, -10, 70, 70       # Scout
nemico2_x, nemico2_y, dim_nemico2_x, dim_nemico2_y = 0, -10, 70, 70       # Bomber
nemico3_x, nemico3_y, dim_nemico3_x, dim_nemico3_y = 0, -10, 90, 90       # Frigate
nemico4_x, nemico4_y, dim_nemico4_x, dim_nemico4_y = 0, -10, 130, 130     # Cruiser
nemico6_x, nemico6_y, dim_nemico6_x, dim_nemico6_y = 0, -10, 200, 200     # Heavycruiser
nemico5_x, nemico5_y, dim_nemico5_x, dim_nemico5_y = 0, -10, 200, 200     # Battleship
nemico7_x, nemico7_y, dim_nemico7_x, dim_nemico7_y = 0, -10, 220, 220,    # Mothership 
nemico8_x, nemico8_y, dim_nemico8_x, dim_nemico8_y = 0, -10, 220, 220,    # Spacestation          

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
    def __init__(self, aereo, pos, vel, tipo, time, texture):
        self.time = time
        self.tipo = tipo
        self.vel = vel
        if self.tipo == -1:
            self.tipo = genera_navicella(self.time)  
        self.rect = pygame.Rect(arr[self.tipo][0], arr[self.tipo][1], arr[self.tipo][2], arr[self.tipo][3])
        self.rectv = pygame.Rect(rectv[self.tipo][0], rectv[self.tipo][1], rectv[self.tipo][2], rectv[self.tipo][3])
        if pos != None:
            self.rect.x = pos[0]
            self.rectv.x = self.rect.x + rectv[self.tipo][0]
            self.rect.y = pos[1]
            self.rectv.x = self.rect.y
        self.img = texture[self.tipo]
        self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
        self.tipo_img = self.tipo
        self.health = health[self.tipo]
        self.esplosioni = []
        self.nemici = [] 
        self.velocita = []
        self.num_nemici = 0
        self.ondata = -1
           
        # if self.main == True:
        #     self.num_nemici = randint(4, 6)
        #     self.num_nemici = 3
        #     percentuale = randint(0, 100)
        #     percentuale = 30
        #     if percentuale < 40:
        #         self.ondata = 0
        #         self.nemici = crea_posizioni(self.num_nemici, WIDTH-(self.num_nemici*self.rect.width)/(self.num_nemici-1), pygame.Rect(0, 0, WIDTH, 0), self.rect)
        #         self.velocita = []
        #         for i in range(self.num_nemici):
        #             arrivo = [aereo.rect.x + aereo.rect.width / 2, aereo.rect.y + aereo.rect.height / 2]
        #             self.velocita.append(calcola_direzione(self.rectv, arrivo))
        #     elif percentuale < 80:
        #         self.ondata = 1
        #     else:
        #         self.ondata = 2
            
        
                
        

def move_nemico(lista, punteggio):
    for nemico in lista:
        nemico.rect.x += nemico.vel[0]
        nemico.rect.y += nemico.vel[1]
        nemico.rectv.x += nemico.vel[0]
        nemico.rectv.y += nemico.vel[1]
    
    temp = []
    for nemico in lista:
        if nemico.rect.y <= HEIGHT:
            temp.append(nemico)
        else:
            punteggio[0] -= 10
    
    return temp

def draw_nemico(lista, screen):
    for nemico in lista:
        screen.blit(nemico.img, (nemico.rect.x, nemico.rect.y))