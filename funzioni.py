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
    lista_colpiti = []
    proiettili_colpiti = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i].rect.colliderect(l2[j]):
                l2[j].health -= 1
                if l2[j].health <= 0:
                    proiettili_colpiti.append(l1[i])  
                    lista_colpiti.append(l2[j])
                    punteggio[0] += temp+100
            
    return [proiettili_colpiti, lista_colpiti]
            
def multiplo(tempo, num):
    a = tempo / num
    if (int(tempo / num) == a):
        return True
    return False

def distanza_punti(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**(0.5)


def carica_texture_jedi():
    immagini = []
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi0.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi1.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi2.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi3.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi4.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi5.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi6.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi7.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi8.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi9.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi10.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi11.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi12.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi13.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi14.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi15.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-15.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-14.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-13.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-12.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-11.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-10.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-9.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-8.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-7.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-6.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-5.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-4.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-3.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-2.png"))
    immagini.append(pygame.image.load("immagini\\jedi_spaceship\\jedi-1.png"))
    immagini2 = []
    for a in immagini:
        immagini2.append(pygame.transform.scale(a, (480/2, 270/2)))
    return immagini2[::-1]

