import pygame

HEIGHT = 700
WIDTH = 500
VEL = 10

class Proiettile:
    def __init__(self, rect, img, screen):
        self.rect = rect
        self.img = img
        self.screen = screen
        self.check = False
        
        proiettile_width = self.img.get_width() // 5
        proiettile_height = self.img.get_height()
        
        self.img = self.img.subsurface((0, 0, proiettile_width, proiettile_height))
        
        # for i in range(5):
        #     startx = i * proiettile_width
        #     img_part = self.img.subsurface((startx, 0, proiettile_width, proiettile_height))
        #     img_part = pygame.transform.scale(img_part, (50, 50))
        #     self.proiettile.append(img_part)
        

    def move(self, aereo, key, dimx):
        self.rect.y = aereo.rect.y - VEL
        if self.check == False:
            self.rect.x = aereo.rect.x + dimx//2
            self.check = True

    def draw(self, screen, ind):
        screen.blit(self.proiettile[0], (self.rect.x, self.rect.y))
        

def move_proiettili(lista, key):
    if key[pygame.K_SPACE]:
        for i in range(len(lista)):
            lista[i].rect.y -= VEL
        # for i in range(len(lista)):
        #     if lista[i].rect.y < 0:
        #         lista.remove(lista[i])
        #         i += 1
                
def draw_proiettili(lista, screen):
    for i in range(len(lista)):
        screen.blit(lista[i].img, (lista[i].rect.width, lista[i].rect.height))