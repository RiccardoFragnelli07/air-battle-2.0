import pygame
from funzioni import genera_proiettili

HEIGHT = 700
WIDTH = 500
VEL = 10

proiettile_x, proiettile_y = 40, 65


class Proiettile:
    def __init__(self, rect, img, np, aereo_rect, screen):
        self.rect = rect
        self.img = img
        self.screen = screen
        self.proiettili = []
        self.np = np
        self.img = pygame.transform.scale(self.img, (proiettile_x, proiettile_y))
        
        self.distanza_proiettili = 15
        posizioni = genera_proiettili(self.np, self.distanza_proiettili, aereo_rect, self.rect)
        for i in range(self.np):
            self.proiettili.append(pygame.Rect((posizioni[i][0]), posizioni[i][1], proiettile_x, proiettile_y))
            
        
def move_proiettili(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i].proiettili)):
            lista[i].proiettili[j].y -= VEL
        
    tmp = []
    for i in range(len(lista)):
        for j in range(len(lista[i].proiettili)):
            if lista[i].proiettili[j].y >= 0:
                tmp.append(lista[i])
    return tmp
           
                
def draw_proiettili(lista, screen):
    # for i in range(len(lista)):
    #     screen.blit(lista[i].img, (lista[i].rect.x, lista[i].rect.y))
    for i in range(len(lista)):
        for j in range(len(lista[i].proiettili)):
            screen.blit(lista[i].img, (lista[i].proiettili[j].x, lista[i].proiettili[j].y))