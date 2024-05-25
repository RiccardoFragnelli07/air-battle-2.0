import pygame
import os

EXPLOSION_SPEED = 1

espl = pygame.image.load("immagini\\animazioni_esplosione.png") 
coll = pygame.image.load("immagini\\animazioni_collisione.png")
nespx = 8
nespy = 6
nscala = 4

class Esplosione:
    def __init__(self, x, y, type):
        self.parts = []
        self.type = type
        self.img = None
        
        if self.type == 0:
            self.img = espl
            rettangolo = self.img.get_rect()
            self.rect = pygame.Rect(rettangolo.x, rettangolo.y, rettangolo.width//nespx, rettangolo.height//nespy)
            for i in range(nespy):
                for j in range(nespx):
                    startx = j * self.rect.width
                    starty = i * self.rect.height
                    img_part = self.img.subsurface((startx, starty, self.rect.width, self.rect.height))
                    img_part = pygame.transform.scale(img_part, (self.rect.width/nscala, self.rect.height/nscala))
                    self.parts.append(img_part)
                    
        elif type == 1:
            self.img = espl
            rettangolo = self.img.get_rect()
            self.rect = pygame.Rect(rettangolo.x, rettangolo.y, rettangolo.width//4, rettangolo.height)
            for i in range(4):
                startx = i * self.rect.width
                img_part = self.img.subsurface((startx, 0, self.rect.width, self.rect.height))
                img_part = pygame.transform.scale(img_part, (self.rect.width, self.rect.height))
                self.images.append(img_part)
        
        self.index = 0
        self.punto = pygame.Vector2(x - self.rect.width/nscala/2, y-self.rect.height/nscala/2)
        self.conta = 0
        self.fine = False

    def draw(self, screen):
        if self.fine == False:
            screen.blit(self.parts[self.index], (self.punto.x, self.punto.y))
            self.conta += 1
            if self.conta >= EXPLOSION_SPEED and self.index < len(self.parts) - 1:
                self.conta = 0
                self.index += 1

            if self.index >= len(self.parts) - 1 and self.conta >= EXPLOSION_SPEED:
                self.fine = True