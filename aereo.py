import pygame
import math
from funzioni import carica_texture_spaceships, distanza_punti

VEL = 7
ROTAZIONE = 0.6
MAX_ROTAZIONE = 12
DEROTAZIONE = 1.2
HEIGHT = 690
WIDTH = 500
IND = 0
TOT_VITE = 20

RED = (255, 0, 0)
GREEN = (0, 255, 0)

base_rect = pygame.Rect(150, 545, 100, 100)
img_texture = carica_texture_spaceships()
aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 150, 545, 120, 120
arr = [[base_rect.x + 12*dim_aereo_x/100, base_rect.y + 9*dim_aereo_x/100, 74*dim_aereo_x/100, 67*dim_aereo_x/100],
       [base_rect.x + 11*dim_aereo_x/100, base_rect.y + 14*dim_aereo_x/100, 78*dim_aereo_x/100, 40*dim_aereo_x/100],
       [base_rect.x + 12*dim_aereo_x/100, base_rect.y + 9*dim_aereo_x/100, 74*dim_aereo_x/100, 67*dim_aereo_x/100],
       [base_rect.x + 21*dim_aereo_x/100, base_rect.y + 12*dim_aereo_x/100, 56*dim_aereo_x/100, 69*dim_aereo_x/100]]

class Aereo:
    def __init__(self, rect, img, screen, num, time = 0):
        self.rect = rect
        self.img = img
        self.screen = screen
        self.time = time
        self.var = False
        self.effetti = []
        self.positivo = True
        self.num = num
        self.ind = 0
        self.rectv = pygame.Rect(arr[num][0], arr[num][1], arr[num][2], arr[num][3])
        self.vita = TOT_VITE
        self.proiettili = 1
        self.pow = False
        self.laser = False
        

        
        self.jet = []
        jet_width = self.img.get_width() // 60
        jet_height = self.img.get_height()
        for i in range(60):
            startx = i * jet_width
            img_part = self.img.subsurface((startx, 0, jet_width, jet_height))
            img_part = pygame.transform.scale(img_part, (self.rect.width, self.rect.height))
            self.jet.append(img_part)
        

            
        
    def move(self, key, lista, lasc, pos):
        if key[pygame.K_w] and self.rectv.y - VEL >= 0:
            self.rect.y -= VEL
            self.rectv.y -= VEL
        if key[pygame.K_s] and self.rectv.y + VEL <= HEIGHT-self.rectv.width:
            self.rect.y += VEL
            self.rectv.y += VEL
        if key[pygame.K_a] and self.rectv.x - VEL >= 0:
            self.rect.x -= VEL
            self.rectv.x -= VEL
            # if key[pygame.K_SPACE]:
            #     for p in lista:
            #         p.rect.x -= VEL
        if key[pygame.K_d] and self.rectv.x + VEL <= WIDTH-self.rectv.height:
            self.rect.x += VEL
            self.rectv.x += VEL
            # if key[pygame.K_SPACE]:
            #     for p in lista:
            #         p.rect.x += VEL
            
        if self.var == True:
            if int(self.ind) > 0 and self.positivo == True:
                self.ind -= DEROTAZIONE
            elif int(self.ind) < 0 and self.positivo == False:
                self.ind += DEROTAZIONE
            else:
                self.var = False
        else:
            if key[pygame.K_a]:
                self.ind -= ROTAZIONE
                if self.ind <= -MAX_ROTAZIONE:
                    self.ind += ROTAZIONE
            if key[pygame.K_d]:
                self.ind += ROTAZIONE
                if self.ind >= MAX_ROTAZIONE:
                    self.ind -= ROTAZIONE
        if lasc[0] == True or lasc[-1] == True:
            self.var = True
            if self.ind < 0:
                self.positivo = False
            else:
                self.positivo = True

        
    def draw(self, screen):
        screen.blit(self.jet[int(self.ind)], (self.rect.x, self.rect.y))
        # screen.blit(self.effetti[int(self.time) % 8], (self.rect.x, self.rect.y + 2))
        self.time += 0.2
        
    def draw_lifebar(self, screen):
        dimx, dimy = 40, 8
        rosso_rect = pygame.Rect(0, 0, dimx, dimy)
        rosso_rect.x = WIDTH - rosso_rect.width - 20
        rosso_rect.y = HEIGHT - rosso_rect.height - 20
        percentuale = self.vita / TOT_VITE * 100
        verde_rect = pygame.Rect(rosso_rect.x, rosso_rect.y, dimx * percentuale / 100, dimy)
        pygame.draw.rect(screen, RED, rosso_rect)
        pygame.draw.rect(screen, GREEN, verde_rect)
        