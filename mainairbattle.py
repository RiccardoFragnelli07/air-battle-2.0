import pygame
import math
import os
import time

from random import randint
from aereo import Aereo
from pianeta import Pianeta
from proiettile import Proiettile, draw_proiettili, move_proiettili
from nemico import Nemico, move_nemico, draw_nemico
from funzioni import carica_texture_spaceships, carica_texture_nemici, calculate_speeds, genera_rettangoli_casuali
from funzioni import collisione_pn, crea_posizioni, frequenze_lista, genera_proiettili, generate_rectangles_on_edges
from funzioni import generate_pentagon_rectangles, mothership_nello_schermo, distanza_punti, calcola_direzione
from explosion import Esplosione
from powerup import Powerup

pygame.init()

WIDTH, HEIGHT = 500, 700
WHITE = (255,255,255)
BLACK = (0,0,0)
VEL_SFONDO = 5
FREQ_PROIETTILI = 0.15
POWERUP_PERC = 3

sound_game = pygame.mixer.Sound("suoni\\Legend.mp3")
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

pianeti = []
for i in range(8):
    img = pygame.image.load(f"immagini\\pianeti\\{i+1}.gif")
    pianeti.append(img)
pianeti.append(pygame.image.load(f"immagini\\pianeti\\8.gif"))

aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 150, 545, 110, 110
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 50, 50, 45, 60
dim_powerup_x, dim_powerup_y = 60, 60
dim_fuoco_x, dim_fuoco_y = 800, 100
pianeta_width, pianeta_height = 150, 150
aereo_rect = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
jetNemico_y, dim_jetNemico_x, dim_jetNemico_y = 0, 50, 50
lista_nemici = []

nemico1_x, nemico1_y, dim_nemico1_x, dim_nemico1_y = 0, -10, 70, 70       # Scout
nemico2_x, nemico2_y, dim_nemico2_x, dim_nemico2_y = 0, -10, 70, 70       # Bomber
nemico3_x, nemico3_y, dim_nemico3_x, dim_nemico3_y = 0, -10, 90, 90       # Frigate
nemico4_x, nemico4_y, dim_nemico4_x, dim_nemico4_y = 0, -10, 130, 130     # Cruiser
nemico6_x, nemico6_y, dim_nemico6_x, dim_nemico6_y = 0, -10, 200, 200     # Heavycruiser
nemico5_x, nemico5_y, dim_nemico5_x, dim_nemico5_y = 0, -10, 200, 200     # Battleship
nemico7_x, nemico7_y, dim_nemico7_x, dim_nemico7_y = 0, -10, 220, 220,    # Mothership 
nemico8_x, nemico8_y, dim_nemico8_x, dim_nemico8_y = 0, -10, 220, 220,    # Spacestation 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR BATTLE")


# INTRO

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
sfondo = pygame.image.load("immagini\\Background.jpg")
width_riquadro, height_riquadro = 40, 40
texture_pow = pygame.image.load("immagini\\pow.png")
texture_pow = pygame.transform.scale(texture_pow, (width_riquadro, height_riquadro))
rect_texture_pow = pygame.Rect(WIDTH - width_riquadro - 20, HEIGHT - height_riquadro - 60, width_riquadro, height_riquadro)
texture_laser = pygame.image.load("immagini\\laser_texture.png")
texture_laser = pygame.transform.scale(texture_laser, (width_riquadro, height_riquadro))
rect_texture_laser = pygame.Rect(WIDTH - width_riquadro - 20, HEIGHT - height_riquadro - 60, width_riquadro, height_riquadro)
img_laser_pw = pygame.image.load("immagini\\proiettile_laser.png")
img_laser_pw = pygame.transform.rotate(img_laser_pw, 270)
img_proiettile = pygame.image.load("immagini\\laser_jet.png")
img_proiettile = pygame.transform.rotate(img_proiettile, 270)
img_proiettile_nemico = pygame.image.load("immagini\\laser_nemico.png")
img_proiettile_nemico = pygame.transform.rotate(img_proiettile_nemico, 90)
img_effetti = pygame.image.load("immagini\\EngineEffect.png")
sfondo = pygame.transform.rotate(sfondo, 90)
sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
img_effetti = pygame.transform.scale(img_effetti, (dim_fuoco_x, dim_fuoco_y))
# se si cambia jet cambia la navicella (max = 3)
jet = 3
# jedi_nave = carica_texture_jedi()
aereo = Aereo(aereo_rect, jet_texture[1][jet], screen, jet)

lista_proiettili = []
da_rimuovere = []
tempo = 0
conta = 0
contatore = 0
FPS = 60
clock = pygame.time.Clock()
gameover = False
autorizza = False
stop = False
conta1 = 0
punteggio = [0]
punteggio[0] = 0
temporanea = 0
vel_nemici_default = [0, 7]
ultimo_proiettile = 0
t_invulnerabilita = 0
lista_esplosioni = []
spazzatura = []
pos_rect_nemici = []
vel_nemici = []
pow_false = False
muovi_con_aereo = False
spara_laser = False
lista_pianeta = []
lista_proiettili_nemici = []
tempo_laser = 0
lista_powerup = []
font_punteggio = pygame.font.SysFont("Times New Roman", 20)
font_punteggio_finale = pygame.font.SysFont("Times New Roman", 30)
font_record = pygame.font.SysFont("Times New Roman", 30)

while gameover == False:
    sound_game.play(-1)
    run1 = True
    run2 = True
    spara = False
    clock.tick(FPS)
    lasciato_ad = [False, False]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT and spara_laser == False:
                sound_laser.play()
                proiettile_rect = pygame.Rect(0, 0, dim_proiettile_x, dim_proiettile_y)
                pos_proiettili = genera_proiettili(int(aereo.proiettili), 15, aereo.rect, proiettile_rect)
                for pos in pos_proiettili:
                    proiettile_rect = pygame.Rect(pos[0], pos[1], dim_proiettile_x, dim_proiettile_y)
                    p = Proiettile(proiettile_rect, img_proiettile, [0, -10])
                    lista_proiettili.append(p)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aereo.pow:
                    for n in lista_nemici:
                        e = Esplosione(n.rect.x + n.rect.width/2, n.rect.y + n.rect.height/2, 0.7)
                        lista_esplosioni.append(e)
                    lista_nemici.clear()
                    aereo.pow = False
                if aereo.laser:
                    tempo_laser = tempo
                    spara_laser = True 
                    muovi_con_aereo = True   
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                lasciato_ad[0] = True
            if event.key == pygame.K_d:
                lasciato_ad[-1] = True


    for nemico in lista_nemici:
        if nemico.tipo >= 3 and nemico.tipo <= 6:
            if int(tempo) % 1 == 0 and int(tempo) == (contatore / 60):
                p = Proiettile(pygame.Rect(nemico.rect.x + nemico.rect.width/2 - dim_proiettile_x*1.5/2, nemico.rect.bottom, dim_proiettile_x*1.5, dim_proiettile_y*1.5), img_proiettile_nemico, [0, 10])
                lista_proiettili_nemici.append(p)
            

    key_pressed = pygame.key.get_pressed()
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])


    if (tempo != 0 and int(tempo) % 2 == 0 and int(tempo) == (contatore / 60) and autorizza == False) or (autorizza and tempo != 0 and int(tempo) % 1 == 0 and int(tempo) == (contatore / 60)): 
        q1 = Nemico(0, None, vel_nemici_default, nemici_texture)
        nnemici = randint(3, 6)
        percentuale = randint(0, 100)
        
        if percentuale < 35:
            tipo = 0
            q1.tipo = tipo
            pos_rect_nemici = genera_rettangoli_casuali(nnemici, q1.rect)
            for i in range(len(pos_rect_nemici)):
                q2 = Nemico(q1.tipo, (pos_rect_nemici[i].x, pos_rect_nemici[i].y), [0, randint(4, 7)], nemici_texture)
                lista_nemici.append(q2)
                
        elif percentuale < 70:
            tipo = 2
            q1.tipo = tipo
            pos_rect_nemici = crea_posizioni(nnemici, (q1.rect.width, q1.rect.height), (0, 0), (WIDTH, 0))
            vel_nemici = calculate_speeds(randint(2, 6), pos_rect_nemici, (aereo.rectv.x + aereo.rect.width/2, aereo.rectv.y + aereo.rect.height/2))
            for i in range(len(pos_rect_nemici)):
                q2 = Nemico(q1.tipo, (pos_rect_nemici[i].x, pos_rect_nemici[i].y), [vel_nemici[i][0], vel_nemici[i][1]], nemici_texture)
                lista_nemici.append(q2)
                
        else:
            tipo = 1
            q1.tipo = tipo
            pos_rect_nemici = generate_rectangles_on_edges(nnemici, q1.rect.width, q1.rect.height, q1.rect.height, 300)
            vel_nemici = calculate_speeds(randint(3, 8), pos_rect_nemici, (aereo.rectv.x + aereo.rect.width/2, aereo.rectv.y + aereo.rect.height/2))
            for i in range(len(pos_rect_nemici)):
                q2 = Nemico(q1.tipo, (pos_rect_nemici[i].x, pos_rect_nemici[i].y), [vel_nemici[i][0], vel_nemici[i][1]], nemici_texture)
                lista_nemici.append(q2)
        
        
    if tempo >= 10 and int(tempo) % 5 == 0 and int(tempo) == (contatore / 60) and stop == False:
        spawn_x = randint(0, WIDTH - dim_nemico4_x)
        vel = [0, 1]
        if randint(0, 1) == 0:
            vel = [-1, 0]
        q1 = Nemico(randint(3, 5), (spawn_x, 0), vel, nemici_texture)
        lista_nemici.append(q1)
            
    if tempo >= 20 and int(tempo) % 60 == 0 and int(tempo) == (contatore / 60) and autorizza == False:
        stop = True
        autorizza = True
        spawn_x = (WIDTH / 2 - dim_nemico7_x / 2, 0)
        vel = [0, 0]
        q1 = Nemico(6, spawn_x, vel, nemici_texture)
        lista_nemici.append(q1)
        
    
    if not mothership_nello_schermo(lista_nemici):
        stop = False
        autorizza = False
        
        
    if tempo >= 5 and int(tempo) % 5 == 0 and int(tempo) == (contatore / 60):
        r = pygame.Rect(randint(0, WIDTH - pianeta_width), pianeta_height * -1, pianeta_width, pianeta_height)
        pianeta = Pianeta(r, VEL_SFONDO, pianeti)
        lista_pianeta.append(pianeta)
        
        
    lista_nemici = move_nemico(lista_nemici, punteggio)
    aereo.move(key_pressed, lista_proiettili, lasciato_ad, mouse_pos)
    lista_proiettili = move_proiettili(lista_proiettili, aereo.rect, muovi_con_aereo)
    lista_proiettili_nemici = move_proiettili(lista_proiettili_nemici, aereo.rect)
    for w in lista_powerup:
        w.move()
    for pianeta in lista_pianeta:
        pianeta.move()
        
    screen.blit(sfondo, (0, -HEIGHT + conta))
    screen.blit(sfondo, (0, 0 + conta))
    for pianeta in lista_pianeta:
        pianeta.draw(screen)
    aereo.draw_lifebar(screen)
    draw_nemico(lista_nemici, screen)
    aereo.draw(screen) 
    for esp in lista_esplosioni:
        esp.draw(screen)
    for powerup in lista_powerup:
        powerup.draw(screen)
    if aereo.pow:
        screen.blit(texture_pow, (rect_texture_pow.x, rect_texture_pow.y))
    if aereo.laser:
        screen.blit(texture_laser, (rect_texture_laser.x, rect_texture_laser.y))
        
    draw_proiettili(lista_proiettili, screen)
    draw_proiettili(lista_proiettili_nemici, screen)    
    if spara_laser and tempo - tempo_laser < 5:
        sound_laser.play()
        proiettile_rect = pygame.Rect(aereo.rectv.x + aereo.rectv.width/2 - dim_proiettile_x/2, aereo.rectv.y - dim_proiettile_y/2, dim_proiettile_x, dim_proiettile_y)
        p = Proiettile(proiettile_rect, img_laser_pw, [0, -10], True)
        lista_proiettili.append(p)
    elif tempo - tempo_laser <= 6 and spara_laser == True:    
        spara_laser = False
        aereo.laser = False
        muovi_con_aereo = False
        rubbish = []
        for p in lista_proiettili:
            if p.trapassa == True:
                rubbish.append(p)
        for r in rubbish:
            lista_proiettili.remove(r)
    print(aereo.vita)       
    for nemico in lista_nemici:
        if aereo.rectv.colliderect(nemico.rect) and tempo - t_invulnerabilita > 1:
            aereo.vita -= 3
            t_invulnerabilita = tempo
            e = Esplosione(aereo.rect.x + aereo.rect.width/2, aereo.rect.y + aereo.rect.height/2, 1)
            lista_esplosioni.append(e)
    for p in lista_proiettili_nemici:
        if aereo.rectv.colliderect(p.rect) and tempo - t_invulnerabilita > 1:
            aereo.vita -= 1
            t_invulnerabilita = tempo
            e = Esplosione(aereo.rect.x + aereo.rect.width/2, aereo.rect.y + aereo.rect.height/2, 1.6)
            lista_esplosioni.append(e)
    if aereo.vita <= 0 :
        gameover = True
    tmp = collisione_pn(lista_proiettili, lista_nemici)
    proiettili_colpiti = tmp[0]
    nemici_colpiti = frequenze_lista(tmp[1])
    
    for w in lista_powerup:
        if aereo.rect.colliderect(w.rect):
            if w.tipo == 0:
                aereo.proiettili += 0.75
            if w.tipo == 1:
                aereo.pow = True
                aereo.laser = False
            if w.tipo == 2:
                aereo.laser = True
                aereo.pow = False
            da_rimuovere.append(w)
    for w in da_rimuovere:
        lista_powerup.remove(w)
    da_rimuovere.clear()
        
    
    for el in nemici_colpiti:
        punteggio[0] += temporanea+50+(el.tipo_img*50)
    
    for p in proiettili_colpiti:
        lista_proiettili.remove(p)
    for key in nemici_colpiti:
        key.health -= nemici_colpiti[key]
        if key.health <= 0:
            if randint(0, 100) < POWERUP_PERC:
                velx = randint(1, 6)
                vely = randint(1, 6)
                if randint(0, 1) == 0:
                    velx *= -1
                if randint(0, 1) == 0:
                    vely *= -1
                w = Powerup(pygame.Rect(key.rect.x + key.rect.width/2, key.rect.y + key.rect.height/2, dim_powerup_x, dim_powerup_y), key.rect, [velx, vely], aereo.proiettili)
                lista_powerup.append(w)
            e = Esplosione(key.rect.x + key.rect.width/2, key.rect.y + key.rect.height/2, 1.5)
            lista_esplosioni.append(e)
            if key in lista_nemici:  
                lista_nemici.remove(key)
        else:
            e = Esplosione(key.rect.x + key.rect.width/2, key.rect.y + key.rect.height/2, 3)
            lista_esplosioni.append(e)
    
    if pow_false:
        aereo.pow = False
        pow_false = True
    
    surf_text_punteggio = font_punteggio.render(f"PUNTEGGIO: {punteggio[0]}", True, WHITE)
    pygame.draw.rect(screen, WHITE, rect_pausa_grande, 2)
    pygame.draw.rect(screen, WHITE, rect_pausa_piccolo1)
    pygame.draw.rect(screen, WHITE, rect_pausa_piccolo2)

    mouse_pos_2 = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if (mouse_pressed[2] == True and rect_pausa_grande.collidepoint(mouse_pos_2)) or key_pressed[pygame.K_ESCAPE] == True:
        sound_game.stop()
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
                    if mouse_pressed[0] == True and rect_yes.collidepoint(mouse_pos_2):
                        run2 = False
                        run1 = False
                        gameover = True
                    if mouse_pressed[0] == True and rect_no.collidepoint(mouse_pos_2):
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
    
    sound_game.play()
    
    screen.blit(surf_text_punteggio, (0,0))      
    if conta >= HEIGHT:
        conta = 0
    else:
        conta += VEL_SFONDO
    contatore += 1
    tempo = contatore / 60


    pygame.display.update()

sound_game.stop()

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