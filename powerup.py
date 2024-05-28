import pygame
from random import randint


class Powerup:
    def __init__(self, rect, img, nemico_rect):
        percentuale = randint(0, 100)
        self.rect = rect
        self.rect.x = nemico_rect.x + nemico_rect.width / 2 - self.rect.width / 2
        self.rect.y = nemico_rect.y + nemico_rect.height / 2 - self.rect.height / 2
        self.img = img
        if percentuale < 30:
            self.type = 0
        elif percentuale < 90:
            self.type = 1
        else:
            self.type = 2
        
        