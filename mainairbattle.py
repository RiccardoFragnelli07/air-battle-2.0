import pygame
import os
from random import randint
from aereo import Aereo
from proiettile import Proiettile, draw_proiettili, move_proiettili
from nemico import Nemico, move_nemico, draw_nemico

pygame.init()

WIDTH, HEIGHT = 500, 700
WHITE = (255,0,0)
VEL_SFONDO = 3


def carica_texture(immagini = []):
    immagini.append([])
    immagini.append([])

    immagini[0].append(pygame.image.load("immagini\\SF01.png"))
    immagini[0].append(pygame.image.load("immagini\\SF02.png"))
    immagini[0].append(pygame.image.load("immagini\\SF03.png"))
    immagini[0].append(pygame.image.load("immagini\\SF04.png"))

    immagini[1].append(pygame.image.load("immagini\\SF01a_strip60.png"))
    immagini[1].append(pygame.image.load("immagini\\SF02a_strip60.png"))
    immagini[1].append(pygame.image.load("immagini\\SF03a_strip60.png"))
    immagini[1].append(pygame.image.load("immagini\\SF04a_strip60.png"))
    
def carica_img_nemici(immagini = []):
    immagini.append([pygame.image.load("immagini\\NFighter.png"), pygame.image.load("immagini\\KFighter.png")])
    immagini.append([pygame.image.load("immagini\\NBomber.png"), pygame.image.load("immagini\\KBomber.png")])
    immagini.append([pygame.image.load("immagini\\NBomber.png"), pygame.image.load("immagini\\KBomber.png")])


aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 150, 545, 100, 100
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 50, 50, 60, 60
dim_fuoco_x, dim_fuoco_y = 800, 100
aereo_rect = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
jetNemico_y, dim_jetNemico_x, dim_jetNemico_y = 0, 50, 50
img_jetNemico = pygame.image.load("immagini\\NBomber.png")
img_jetNemico = pygame.transform.rotate(img_jetNemico, 180)
lista_nemici = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR BATTLE")

jet_texture = []
carica_texture(jet_texture)
sfondo = pygame.image.load("immagini\\Background.jpg")
img_proiettile = pygame.image.load("immagini\\Laser.png")
img_proiettile = pygame.transform.rotate(img_proiettile, 270)
img_effetti = pygame.image.load("immagini\\EngineEffect.png")

sfondo = pygame.transform.rotate(sfondo, 90)
sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
img_effetti = pygame.transform.scale(img_effetti, (dim_fuoco_x, dim_fuoco_y))
aereo = Aereo(aereo_rect, jet_texture[1][1], img_effetti, screen)

lista_proiettili = []
conta = 0
FPS = 60
clock = pygame.time.Clock()
gameover = False
tempo = 50
conta1 = 0

while gameover == False:
    spara = False
    clock.tick(FPS)
    lasciato_ad = [False, False]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                proiettile_rect = pygame.Rect(aereo.rect.x + (aereo_rect.width // 2) - 10, aereo_rect.y, dim_proiettile_x, dim_proiettile_y)
                p = Proiettile(proiettile_rect, img_proiettile, screen)
                lista_proiettili.append(p)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                lasciato_ad[0] = True
            if event.key == pygame.K_d:
                lasciato_ad[-1] = True

    key_pressed = pygame.key.get_pressed()
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    if conta1 == tempo:
        nemico_x = randint(0, WIDTH-dim_jetNemico_x)
        nemico_rect = pygame.Rect(nemico_x, jetNemico_y, dim_jetNemico_x, dim_jetNemico_y)
        q = Nemico(nemico_rect, img_jetNemico)
        lista_nemici.append(q)
        conta1 = 0

    lista_nemici = move_nemico(lista_nemici)
    
    aereo.move(screen, key_pressed, lasciato_ad, mouse_pos)
    lista_proiettili = move_proiettili(lista_proiettili)
    screen.blit(sfondo, (0, -HEIGHT + conta))
    screen.blit(sfondo, (0, 0 + conta))
    aereo.draw(screen) 
    draw_nemico(lista_nemici, screen)
    draw_proiettili(lista_proiettili, screen)
    
    if conta >= HEIGHT:
        conta = 0
    else:
        conta += VEL_SFONDO
    
    for nemico in lista_nemici:
        if aereo.rect.colliderect(nemico.rect):
            gameover = True
    conta1 += 1
    pygame.display.update()
    

pygame.quit()



# carriata da glucozio (10 in pagella per lui obbligatorio)