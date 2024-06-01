import pygame
from random import randint

HEIGHT = 700
WIDTH = 500
MAX_PROIETTILI = 6

texture = pygame.image.load("immagini\\powerup.png")

class Powerup:
    def __init__(self, rect, nemico_rect, vel, aereo):
        percentuale = randint(0, 100)
        self.rect = rect
        self.ncollisioni = 0
        self.max_collisioni = 2
        self.vel = vel
        self.rect.x = nemico_rect.x + nemico_rect.width / 2 - self.rect.width / 2
        self.rect.y = nemico_rect.y + nemico_rect.height / 2 - self.rect.height / 2
        self.img = texture
        self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
        if percentuale < 40 and aereo.proiettili <= MAX_PROIETTILI:
            self.tipo = 0
        elif percentuale < 75:
            self.tipo = 1
        else:
            self.tipo = 2
        if aereo.pow or aereo.laser:
            self.tipo = 0
            
    def move(self):
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
        if self.rect.x < 0 and self.ncollisioni <= self.max_collisioni:
            self.rect.x = 0
            self.vel[0] *= -1
            self.ncollisioni += 1
        if self.rect.y < 0 and self.ncollisioni <= self.max_collisioni:
            self.rect.y = 0
            self.vel[1] *= -1
            self.ncollisioni += 1
        if self.rect.x > WIDTH - self.rect.width and self.ncollisioni <= self.max_collisioni:
            self.rect.x = WIDTH - self.rect.width
            self.vel[0] *= -1
            self.ncollisioni += 1
        if self.rect.y > HEIGHT - self.rect.height and self.ncollisioni <= self.max_collisioni:
            self.rect.y = HEIGHT - self.rect.height
            self.vel[1] *= -1
            self.ncollisioni += 1
            
    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
            
        
        