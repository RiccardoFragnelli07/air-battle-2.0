import pygame
import os
from aereo import Aereo

pygame.init()

WIDTH, HEIGHT = 500, 700
WHITE = (0,0,0)
VEL = 7


def carica_texture(immagini = []):
    immagini.append([])
    immagini.append([])

    immagini[0].append(pygame.image.load("air-battle-2.0\\immagini\\SF01.png"))
    immagini[0].append(pygame.image.load("air-battle-2.0\\immagini\\SF02.png"))
    immagini[0].append(pygame.image.load("air-battle-2.0\\immagini\\SF03.png"))
    immagini[0].append(pygame.image.load("air-battle-2.0\\immagini\\SF04.png"))
    
    immagini[1].append(pygame.image.load("air-battle-2.0\\immagini\\SF01a_strip60.png"))
    immagini[1].append(pygame.image.load("air-battle-2.0\\immagini\\SF02a_strip60.png"))
    immagini[1].append(pygame.image.load("air-battle-2.0\\immagini\\SF03a_strip60.png"))
    immagini[1].append(pygame.image.load("air-battle-2.0\\immagini\\SF04a_strip60.png"))


aereo_x, aereo_y, dim_aereo_x, dim_aereo_y  = 150, 545, 14400, 240
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 50, 50, 800, 100
aereo_rect = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
effetti_rect = pygame.Rect(proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

sfondo = pygame.image.load("air-battle-2.0\\immagini\\background.jpg")
sfondo = pygame.transform.rotate(sfondo, 90)
sfondo = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))

pygame.display.set_caption("AIR BATTLE")
# img_aereo = pygame.image.load("C:\\Users\\Matteo\\Desktop\\Pygame\\Videogioco\\Textures\\Navicelle\\Designs - Base\\PNGs\\Nairan - Torpedo Ship - Base.png")
img_effetti = pygame.image.load("air-battle-2.0\\immagini\\Nairan - Torpedo Ship - Engine.png")
jet_texture = []
carica_texture(jet_texture)

img_aereo = pygame.transform.scale(jet_texture[1][1], (dim_aereo_x, dim_aereo_y))
img_effetti = pygame.transform.scale(img_effetti, (dim_proiettile_x, dim_proiettile_y))
aereoPri = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
effettiPri = pygame.Rect(proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y)
aereo = Aereo(aereo_rect, img_aereo, img_effetti, screen)

conta = 0
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    spara = False
    clock.tick(FPS)
    lasciato_ad = [False, False]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         lasciato_ad[-1] == True
        #     if event.key == pygame.K_d:
        #         lasciato_ad[0] == True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                lasciato_ad[0] = True
            if event.key == pygame.K_d:
                lasciato_ad[-1] = True
    
    key_pressed = pygame.key.get_pressed()
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    aereo.move(screen, key_pressed, lasciato_ad, mouse_pos)
    
    screen.blit(sfondo, (0, -HEIGHT + conta))
    screen.blit(sfondo, (0, 0 + conta))
    aereo.draw(screen)
    if conta >= HEIGHT:
        conta = 0
    else:
        conta += 1
        
    pygame.display.update()
    

pygame.quit()



# carriata da glucozio (10 in pagella per lui obbligatorio)