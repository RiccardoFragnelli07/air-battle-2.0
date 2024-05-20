# funzioni utili
import pygame
from random import randint
import math

def carica_texture_spaceships():
    immagini = []
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
    
    return immagini


    
def carica_texture_nemici(immagini = []):
    immagini = []
    immagini.append(pygame.image.load("immagini\\Alien-Scout.png"))
    immagini.append(pygame.image.load("immagini\\Alien-Bomber.png"))
    immagini.append(pygame.image.load("immagini\\Alien-Frigate.png"))
    immagini.append(pygame.image.load("immagini\\Alien-Cruiser.png"))
    immagini.append(pygame.image.load("immagini\\Alien-Heavycruiser.png"))
    immagini.append(pygame.image.load("immagini\\Alien-Battleship.png"))
    immagini.append(pygame.image.load("immagini\\Alien-Mothership.png"))
    immagini.append(pygame.image.load("immagini\\Alien-Spacestation.png"))
    return immagini

def genera_navicella(time):
    if time >= 0 and time <= 15:
        navicella = randint(0, 1)
    elif time > 15 and time <= 60:
        navicella = randint(0, 3)
    else:
        num = randint(1, 100)
        if num >= 1 and num <= 30:
            navicella = randint(0, 1)
        elif num > 30 and num <= 80:
            navicella = randint(2, 3)
        else:
            navicella = randint(4, 5)
    return navicella

def collisione_pn(l1, l2, punteggio, temp):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i].rect.colliderect(l2[j]):
                l1.pop(i)
                l2.pop(j)
                punteggio[0] += temp+100
                return 0
            
def multiplo(tempo, num):
    a = tempo / num
    if (int(tempo / num) == a):
        return True
    return False

def distanza_punti(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**(0.5)


def carica_texture_jet():
    immagini = []
    immagini.append(pygame.image.load("immagini\\jet_images\\jet0.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet16.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet17.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet18.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet19.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet20.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet21.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet22.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet23.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet24.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet26.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet25.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet27.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet28.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet30.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet29.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet15.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet14.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet13.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet12.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet11.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet10.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet9.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet8.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet7.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet6.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet5.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet4.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet3.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet2.png"))
    immagini.append(pygame.image.load("immagini\\jet_images\\jet1.png"))
    return immagini