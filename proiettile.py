import pygame

HEIGHT = 700
WIDTH = 500
VEL = 10

class Proiettile:
    def __init__(self, rect, img, screen):
        self.rect = rect
        self.img = img
        self.screen = screen
        self.proiettili = []
        self.check = False
        
        proiettile_width = self.img.get_width() // 5
        proiettile_height = self.img.get_height()
        for i in range(5):
           startx = i * proiettile_width
           img_part = self.img.subsurface((startx, 0, proiettile_width, proiettile_height))
           img_part = pygame.transform.scale(img_part, (30, 30))
           self.proiettili.append(img_part)
        

def move_proiettili(lista):
    for i in range(len(lista)):
        lista[i][0].rect.y -= VEL
        if lista[i][1] > 4:
            lista[i][1] = 0
        lista[i][1] += 0.2
        
    tmp = []
    for i in range(len(lista)):
        if lista[i][0].rect.y >= 0:
            tmp.append(lista[i])
    return tmp
                
def draw_proiettili(lista, screen):
    for i in range(len(lista)):
        screen.blit(lista[i][0].proiettili[int(lista[i][1])], (lista[i][0].rect.x, lista[i][0].rect.y))