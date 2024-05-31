import pygame

HEIGHT = 700
WIDTH = 500
VEL = 10

dim_proiettile_x, dim_proiettile_y = 40, 65

class Proiettile:
    def __init__(self, rect, img, vel, ismissile = False):
        self.rect = rect
        self.img = img
        self.proiettili = []
        self.vel = vel
        self.missile = ismissile
        self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
        

def move_proiettili(lista):
    for i in range(len(lista)):
        lista[i].rect.x += lista[i].vel[0]
        lista[i].rect.y += lista[i].vel[1]
        
    tmp = []
    for i in range(len(lista)):
        if lista[i].rect.y >= 0:
            tmp.append(lista[i])
    return tmp
           
                
def draw_proiettili(lista, screen):
    for i in range(len(lista)):
        screen.blit(lista[i].img, (lista[i].rect.x, lista[i].rect.y))