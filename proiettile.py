import pygame

HEIGHT = 700
WIDTH = 500
VEL = 10

dim_proiettile_x, dim_proiettile_y = 40, 65

class Proiettile:
    def __init__(self, rect, img, screen):
        self.rect = rect
        self.img = img
        self.screen = screen
        self.proiettili = []
        self.check = False
        self.img = pygame.transform.scale(self.img, (dim_proiettile_x, dim_proiettile_y))
        
        
def genera_proiettile(lista, key, time):
    if key[pygame.K_SPACE]:
        pass
        
        

def move_proiettili(lista):
    for i in range(len(lista)):
        lista[i].rect.y -= VEL
        
    tmp = []
    for i in range(len(lista)):
        if lista[i].rect.y >= 0:
            tmp.append(lista[i])
    return tmp
           
                
def draw_proiettili(lista, screen):
    for i in range(len(lista)):
        screen.blit(lista[i].img, (lista[i].rect.x, lista[i].rect.y))