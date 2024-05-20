import pygame
import math
from funzioni import carica_texture_spaceships, distanza_punti

VEL = 7
ROTAZIONE = 0.7
MAX_ROTAZIONE = 11
DEROTAZIONE = 1.2
HEIGHT = 690
WIDTH = 500
IND = 0

base_rect = pygame.Rect(150, 545, 100, 100)
img_texture = carica_texture_spaceships()
arr = [[base_rect.x + 12, base_rect.y + 9, 74, 67],
       [base_rect.x + 11, base_rect.y + 14, 78, 40],
       [base_rect.x + 12, base_rect.y + 9, 74, 67],
       [base_rect.x + 21, base_rect.y + 12, 56, 69]]

class Aereo:
    def __init__(self, rect, img, img_effetti, screen, num, time = 0):
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
        
        effetti_width = img_effetti.get_width() // 8
        effetti_height = img_effetti.get_height()
        for i in range(8):
            startx = i * effetti_width
            img_part = img_effetti.subsurface((startx, 0, effetti_width, effetti_height))
            self.effetti.append(img_part)
        self.centro_aereo = pygame.math.Vector2(self.rect.x + self.rect.width, self.rect.y + self.rect.height)
        
        # self.jet = self.img
        # for i in range(len(self.jet)):
        #     self.jet[i] = pygame.transform.scale(self.jet[i], (120, 120))
        
        self.jet = []
        jet_width = self.img.get_width() // 60
        jet_height = self.img.get_height()
        for i in range(60):
            startx = i * jet_width
            img_part = self.img.subsurface((startx, 0, jet_width, jet_height))
            img_part = pygame.transform.scale(img_part, (100, 100))
            self.jet.append(img_part)

            
        
    def move(self, screen, key, lasc, pos):
        if key[pygame.K_w] and self.rect.y - VEL >= 0:
            self.rect.y -= VEL
            self.rectv.y -= VEL
        if key[pygame.K_s] and self.rect.y + VEL <= HEIGHT-100:
            self.rect.y += VEL
            self.rectv.y += VEL
        if key[pygame.K_a] and self.rect.x - VEL >= 0:
            self.rect.x -= VEL
            self.rectv.x -= VEL
        if key[pygame.K_d] and self.rect.x + VEL <= WIDTH-100:
            self.rect.x += VEL
            self.rectv.x += VEL
            
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