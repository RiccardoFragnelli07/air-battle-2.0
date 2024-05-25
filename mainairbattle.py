import pygame
import math
import os
import time

from random import randint
from aereo import Aereo
from proiettile import Proiettile, draw_proiettili, move_proiettili, genera_proiettile
from nemico import Nemico, move_nemico, draw_nemico
from funzioni import carica_texture_spaceships, carica_texture_nemici, carica_texture_jedi, collisione_pn, multiplo
from explosion import Esplosione

pygame.init()

WIDTH, HEIGHT = 500, 700
WHITE = (255,255,255)
BLACK = (0,0,0)
VEL_SFONDO = 3
FREQ_PROIETTILI = 0.15     # i proiettili possono venire sparati dopo 0.1 secondi dal proiettile precedente
sound_death = pygame.mixer.Sound("suoni\\dark-souls-you-died-sound-effect.mp3")
sound_laser = pygame.mixer.Sound("suoni\\laser-sound-1.mp3")
sound_intro = pygame.mixer.Sound("suoni\\epic-sound.mp3")
sound_menu = pygame.mixer.Sound("suoni\\drum-loop.mp3")
sound_aereo = pygame.mixer.Sound("suoni\\sound-jet.mp3")
font_air = pygame.font.SysFont("Copperplate Gothic", 50)
surf_text_air = font_air.render("AIR", True, WHITE)
font_battle = pygame.font.SysFont("Copperplate Gothic", 50)
surf_text_battle = font_battle.render("BATTLE", True, WHITE)
font_number = pygame.font.SysFont("Copperplate Gothic", 50)
surf_text_number = font_number.render("2.0", True, WHITE)
font_play = pygame.font.SysFont("Copperplate Gothic", 20)
surf_text_play = font_play.render("PREMI UN TASTO PER CONTINUARE", True, WHITE)
rect_nero = pygame.Rect(50, 400, surf_text_play.get_width(), surf_text_play.get_height())

# aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 150, 545, 100, 100
aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 150, 545, 120, 120
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 50, 50, 60, 60
dim_fuoco_x, dim_fuoco_y = 800, 100
aereo_rect = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
jetNemico_y, dim_jetNemico_x, dim_jetNemico_y = 0, 50, 50
lista_nemici = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR BATTLE")
screen.fill(BLACK)
sound_intro.play()
time.sleep(1)
screen.blit(surf_text_air, (90, 200))
pygame.display.update()
time.sleep(2)
screen.blit(surf_text_battle, (200, 200))
pygame.display.update()
time.sleep(2)
screen.blit(surf_text_number, (200, 250))
pygame.display.update()
time.sleep(2)
screen.blit(surf_text_play, (50, 400))
run = True
pygame.display.update()

while run:
    sound_menu.play()
    screen.blit(surf_text_air, (90, 200))
    screen.blit(surf_text_battle, (200, 200))
    screen.blit(surf_text_number, (200, 250))
    time.sleep(1)
    pygame.draw.rect(screen, BLACK, (rect_nero.x, rect_nero.y, rect_nero.width, rect_nero.height))
    pygame.display.update()
    time.sleep(1)
    screen.blit(surf_text_play, (50, 400))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            run = False

sound_menu.stop()
jet_texture = carica_texture_spaceships()
# jet_texture = carica_texture_jet()
nemici_texture = carica_texture_nemici()
jedi = pygame.image.load("immagini\\jedi_spaceship\\jedi0.png")
jedi = pygame.transform.scale(jedi, (480, 270))
sfondo = pygame.image.load("immagini\\Background.jpg")
img_proiettile = pygame.image.load("immagini\\Laser.png")
img_proiettile = pygame.transform.rotate(img_proiettile, 270)
img_effetti = pygame.image.load("immagini\\EngineEffect.png")
sfondo = pygame.transform.rotate(sfondo, 90)
sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
img_effetti = pygame.transform.scale(img_effetti, (dim_fuoco_x, dim_fuoco_y))
jet = 0
jedi_nave = carica_texture_jedi()
# aereo = Aereo(aereo_rect, jet_texture[1][jet], img_effetti, screen, jet)
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
lista_esplosioni = []
spazzatura = []
font_punteggio = pygame.font.SysFont("Times New Roman", 20)
font_punteggio_finale = pygame.font.SysFont("Times New Roman", 30)
font_record = pygame.font.SysFont("Times New Roman", 30)

while gameover == False:
    spara = False
    clock.tick(FPS)
    lasciato_ad = [False, False]
    #sound_aereo.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound_laser.play()
                proiettile_rect = pygame.Rect(aereo.rectv.x + (aereo.rectv.width // 2) - 10, aereo.rect.y, dim_proiettile_x, dim_proiettile_y)
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
        
    # if key_pressed[pygame.K_SPACE] and tempo - ultimo_proiettile >= FREQ_PROIETTILI:
    #     sound_laser.play()
    #     proiettile_rect = pygame.Rect(aereo.rect.x + (aereo_rect.width // 2) - 10, aereo_rect.y, dim_proiettile_x, dim_proiettile_y)
    #     p = Proiettile(proiettile_rect, img_proiettile, screen)
    #     lista_proiettili.append(p)
    #     ultimo_proiettile = tempo

    lista_nemici = move_nemico(lista_nemici)
    aereo.move(key_pressed, lista_proiettili, lasciato_ad, mouse_pos)
    lista_proiettili = move_proiettili(lista_proiettili)
    screen.blit(sfondo, (0, -HEIGHT + conta))
    screen.blit(sfondo, (0, 0 + conta))
    draw_nemico(lista_nemici, screen)
    for esp in lista_esplosioni:
        esp.draw(screen)
    
    # for i in range(len(explosion_point)):
    #     explosion_point[i][0].esplodi(screen, explosion_point[i][1], explosion_point[i][2])
    #     explosion_point[i][2] += 1
    #     if explosion_point[i][2] > 5:
    #         spazzatura.append(i)
    # for i in range(len(spazzatura)):
    #     if explosion_point[i] != 0:
    #         explosion_point.pop(spazzatura[i])
    #         spazzatura[i] = 0 
        
    aereo.draw(screen) 
    draw_proiettili(lista_proiettili, screen)
    
    for nemico in lista_nemici:
        if aereo.rectv.colliderect(nemico.rectv):
            gameover = True
    
    # ho dovuto fare questa roba con la funzione pk se no dava l'errore out of range
    tmp = collisione_pn(lista_proiettili, lista_nemici, punteggio, temporanea, nemici_texture)
    proiettili_colpiti = tmp[0]
    nemici_colpiti = tmp[1]
    for p in proiettili_colpiti:
        lista_proiettili.remove(p)
    for n in nemici_colpiti:
        e = Esplosione(n.rect.x + n.rect.width/2, n.rect.y + n.rect.height/2, 0)
        lista_esplosioni.append(e)
        lista_nemici.remove(n)
    
    surf_text_punteggio = font_punteggio.render(f"PUNTEGGIO: {punteggio[0]}", True, WHITE)
    screen.blit(surf_text_punteggio, (0,0))      
    if conta >= HEIGHT:
        conta = 0
    else:
        conta += VEL_SFONDO
    contatore += 1
    tempo = contatore / 60
    pygame.display.update()

surf_text_punteggio = font_punteggio_finale.render(f"PUNTEGGIO: {punteggio[0]}", True, WHITE)
stringa = []
with open('record.txt', 'r', encoding = 'utf-8') as f:
    for riga in f:
        stringa.append(riga)

if int(stringa[0]) < punteggio[0]:
    with open('record.txt', 'w', encoding = 'utf-8') as f:
        f.write(str(punteggio[0]))
    surf_text_record = font_record.render(f"NEW RECORD: {punteggio[0]}", True, WHITE)
else:
    surf_text_record = font_record.render(f"Record: {stringa[0]}", True, WHITE)

sound_death.play()
for i in range(150):
    sfondo_gameover = pygame.image.load("immagini\\youdied-sfondo.jpg")
    sfondo_gameover = pygame.transform.scale(sfondo_gameover, (600, 600))
    screen.fill(BLACK)
    screen.blit(sfondo_gameover, (-60, 10))
    screen.blit(surf_text_punteggio, (0, 500))
    screen.blit(surf_text_record, (0, 550))
    pygame.display.update()

pygame.quit()



# carriata da glucozio (10 in pagella per lui obbligatorio)