import pygame
from random import randint

WIDTH, HEIGHT = 500, 700
VEL = 7


class Nemico:
    def __init__(self, jetNemico_rect, img_jetNemico) -> None:
        self.rect = jetNemico_rect
        self.img = img_jetNemico


def move_nemico(lista):
    temp = []
    for nemico in lista:
        nemico.rect.y += VEL
    for nemico in lista:
        if nemico.rect.y < HEIGHT:
            temp.append(nemico)

    return temp

def draw_nemico(lista, screen):
    for nemico in lista:
        screen.blit(nemico.img, (nemico.rect.x, nemico.rect.y))