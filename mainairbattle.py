import pygame
import math
import os
import time

from random import randint
from aereo import Aereo
from proiettile import Proiettile, draw_proiettili, move_proiettili
from nemico import Nemico, move_nemico, draw_nemico
from funzioni import carica_texture_spaceships, carica_texture_nemici, carica_texture_jedi
from funzioni import collisione_pn, multiplo, genera_proiettili, frequenze_lista
from explosion import Esplosione

pygame.init()

WIDTH, HEIGHT = 500, 700
WHITE = (255,255,255)
BLACK = (0,0,0)
VEL_SFONDO = 3
FREQ_PROIETTILI = 0.15
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
rect_pausa_grande = pygame.Rect(450, 10, 30, 30)
rect_pausa_piccolo1 = pygame.Rect(rect_pausa_grande.x+(rect_pausa_grande.width//2)-9, rect_pausa_grande.y+5, 3, 20)
rect_pausa_piccolo2 = pygame.Rect(rect_pausa_grande.x+(rect_pausa_grande.width//2)+7, rect_pausa_grande.y+5, 3, 20)
rect_exit = pygame.Rect(WIDTH//2-150, HEIGHT//2-50, 300, 100)
font_exit = pygame.font.SysFont("Copperplate Gothic", 50)
surf_text_exit = font_exit.render("EXIT", True, WHITE)
font_allert = pygame.font.SysFont("Copperplate Gothic", 30)
surf_text_allert = font_allert.render("SEI SICURO DI VOLER USCIRE", True, WHITE)
font_yes = pygame.font.SysFont("Copperplate Gothic", 50)
surf_text_yes = font_yes.render("SI", True, WHITE)
rect_yes = pygame.Rect(WIDTH//2-100, (HEIGHT//2)+58, 48, 37)
font_no = pygame.font.SysFont("Copperplate Gothic", 50)
surf_text_no = font_no.render("NO", True, WHITE)
rect_no = pygame.Rect((WIDTH//2)+5, (HEIGHT//2)+60, 80, 35)

aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 150, 545, 120, 120
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 50, 50, 45, 60
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
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            run = False
sound_menu.stop()


jet_texture = carica_texture_spaceships()
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
jet = 1
jedi_nave = carica_texture_jedi()
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
t_invulnerabilita = 0
lista_esplosioni = []
spazzatura = []
font_punteggio = pygame.font.SysFont("Times New Roman", 20)
font_punteggio_finale = pygame.font.SysFont("Times New Roman", 30)
font_record = pygame.font.SysFont("Times New Roman", 30)

while gameover == False:
    run1 = True
    run2 = True
    spara = False
    clock.tick(FPS)
    lasciato_ad = [False, False]
    #sound_aereo.play(-1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                sound_laser.play()
                pos_proiettili = genera_proiettili(3, 15, aereo.rect, dim_proiettile_x, dim_proiettile_y)
                for pos in pos_proiettili:
                    proiettile_rect = pygame.Rect(pos[0], pos[1], dim_proiettile_x, dim_proiettile_y)
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

    lista_nemici = move_nemico(lista_nemici)
    aereo.move(key_pressed, lista_proiettili, lasciato_ad, mouse_pos)

    lista_proiettili = move_proiettili(lista_proiettili)
    for i in range(len(lista_proiettili)):
        print(lista_proiettili[i].proiettili)
    screen.blit(sfondo, (0, -HEIGHT + conta))
    screen.blit(sfondo, (0, 0 + conta))
    aereo.draw_lifebar(screen)
    draw_nemico(lista_nemici, screen)
    for esp in lista_esplosioni:
        esp.draw(screen)
        
    aereo.draw(screen) 
    draw_proiettili(lista_proiettili, screen)
    
    for nemico in lista_nemici:
        if aereo.rectv.colliderect(nemico.rectv) and tempo - t_invulnerabilita > 1:
            aereo.vita = 0
            t_invulnerabilita = tempo
    if aereo.vita <= 0 :
        gameover = True
    
    tmp = collisione_pn(lista_proiettili, lista_nemici, punteggio, temporanea, nemici_texture)
    proiettili_colpiti = tmp[0]
    nemici_colpiti = frequenze_lista(tmp[1])
    for p in proiettili_colpiti:
        lista_proiettili.remove(p)
    for key in nemici_colpiti:
        key.health -= nemici_colpiti[key]
        if key.health <= 0:
            e = Esplosione(key.rect.x + key.rect.width/2, key.rect.y + key.rect.height/2, 0)
            lista_esplosioni.append(e)
            if key in lista_nemici:  
                lista_nemici.remove(key)
    
    surf_text_punteggio = font_punteggio.render(f"PUNTEGGIO: {punteggio[0]}", True, WHITE)
    pygame.draw.rect(screen, WHITE, rect_pausa_grande, 2)
    pygame.draw.rect(screen, WHITE, rect_pausa_piccolo1)
    pygame.draw.rect(screen, WHITE, rect_pausa_piccolo2)

    mouse_pos_2 = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[2] == True and rect_pausa_grande.collidepoint(mouse_pos_2):
        while run1:
            pygame.draw.rect(screen, WHITE, rect_exit, 2)
            screen.blit(surf_text_exit, (rect_exit.x+(rect_exit.width//2)-48, rect_exit.y+(rect_exit.height//2)-30))
            mouse_pos_2 = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0] == True and rect_exit.collidepoint(mouse_pos_2):
                while run2:
                    screen.fill(BLACK)
                    screen.blit(surf_text_allert, (WIDTH//2-240, HEIGHT//2))
                    screen.blit(surf_text_yes, (WIDTH//2-100, (HEIGHT//2)+50))
                    screen.blit(surf_text_no, ((WIDTH//2), (HEIGHT//2)+50))
                    mouse_pos_2 = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    if mouse_pressed[2] == True and rect_yes.collidepoint(mouse_pos_2):
                        run2 = False
                        run1 = False
                        gameover = True
                    if mouse_pressed[2] == True and rect_no.collidepoint(mouse_pos_2):
                        run2 = False
                        run1 = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run2 = False
                            run1 = False
                            gameover = True
                    
                    pygame.display.update()
            if mouse_pressed[0] == True and rect_pausa_grande.collidepoint(mouse_pos_2):
                run1 = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run1 = False
                    gameover = True
            
            pygame.display.update()
    
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