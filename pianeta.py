import pygame
from random import randint

WIDTH, HEIGHT = 500, 700

class Pianeta:
    def __init__(self, rect, vely, textures):
        self.rect = rect
        self.vely = vely
        self.img = textures[randint(0, 7)]
        self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
    
    def move(self):
        self.rect.y += self.vely
        
    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
    
        