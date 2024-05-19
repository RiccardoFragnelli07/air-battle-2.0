import pygame
import os
from random import randint
from aereo import Aereo
from proiettile import Proiettile, draw_proiettili, move_proiettili, genera_proiettile
from nemico import Nemico, move_nemico, draw_nemico
from funzioni import carica_texture_jet, carica_texture_nemici, collisione_pn, multiplo

pygame.init()

WIDTH, HEIGHT = 500, 700
WHITE = (255,0,0)
BLACK = (0,0,0)
VEL_SFONDO = 3
FREQ_PROIETTILI = 0.2     # i proiettili possono venire sparati dopo 0.1 secondi dal proiettile precedente

aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 150, 545, 100, 100
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 50, 50, 60, 60
dim_fuoco_x, dim_fuoco_y = 800, 100
aereo_rect = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
jetNemico_y, dim_jetNemico_x, dim_jetNemico_y = 0, 50, 50
lista_nemici = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR BATTLE")

jet_texture = carica_texture_jet()
nemici_texture = carica_texture_nemici()

sfondo = pygame.image.load("immagini\\Background.jpg")
img_proiettile = pygame.image.load("immagini\\Laser.png")
img_proiettile = pygame.transform.rotate(img_proiettile, 270)
img_effetti = pygame.image.load("immagini\\EngineEffect.png")
sfondo = pygame.transform.rotate(sfondo, 90)
sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
img_effetti = pygame.transform.scale(img_effetti, (dim_fuoco_x, dim_fuoco_y))
jet = 0
aereo = Aereo(aereo_rect, jet_texture[1][jet], img_effetti, screen, jet)

lista_proiettili = []
tempo = 0
conta = 0
contatore = 0
FPS = 60
clock = pygame.time.Clock()
gameover = False
conta1 = 0
punteggio = [0]
punteggio[0] = 0
temporanea = 0
ultimo_proiettile = 0

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

    if tempo != 0 and int(tempo) % 1 == 0 and int(tempo) == (contatore / 60):
        q = Nemico(tempo, nemici_texture)
        lista_nemici.append(q)
        
    if key_pressed[pygame.K_SPACE] and tempo - ultimo_proiettile >= FREQ_PROIETTILI:
        proiettile_rect = pygame.Rect(aereo.rect.x + (aereo_rect.width // 2) - 10, aereo_rect.y, dim_proiettile_x, dim_proiettile_y)
        p = Proiettile(proiettile_rect, img_proiettile, screen)
        lista_proiettili.append(p)
        ultimo_proiettile = tempo

    lista_nemici = move_nemico(lista_nemici)
    aereo.move(screen, key_pressed, lasciato_ad, mouse_pos)
    lista_proiettili = move_proiettili(lista_proiettili)
    screen.blit(sfondo, (0, -HEIGHT + conta))
    screen.blit(sfondo, (0, 0 + conta))
    aereo.draw(screen) 
    draw_nemico(lista_nemici, screen)
    draw_proiettili(lista_proiettili, screen)
    
    for nemico in lista_nemici:
        if aereo.rectv.colliderect(nemico.rect):
            gameover = True
    
    # ho dovuto fare questa roba con la funzione pk se no dava l'errore out of range
    while collisione_pn(lista_proiettili, lista_nemici, punteggio, temporanea) == 0:
        pass
                
    if conta >= HEIGHT:
        conta = 0
    else:
        conta += VEL_SFONDO
    contatore += 1
    tempo = contatore / 60
    pygame.display.update()

punteggio_finale = punteggio[0]
font = pygame.font.SysFont("Times New Roman", 50)
surf_text = font.render(f"Punteggio: {punteggio_finale}", True, "red")

for i in range(20):
    sfondo_gameover = pygame.image.load("immagini\\youdied-sfondo.jpg")
    sfondo_gameover = pygame.transform.scale(sfondo_gameover, (500, 500))
    screen.fill(BLACK)
    screen.blit(sfondo_gameover, (0, 100))
    screen.blit(surf_text, (0, 500))
    pygame.display.update()

pygame.quit()



# carriata da glucozio (10 in pagella per lui obbligatorio)