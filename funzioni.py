# funzioni utili
import pygame
from random import randint
import math

def carica_texture_spaceships():
    immagini = []
    immagini.append([])
    immagini.append([])

    immagini[0].append(pygame.image.load("immagini\\white_spaceship_images\\SF01.png"))
    immagini[0].append(pygame.image.load("immagini\\white_spaceship_images\\SF02.png"))
    immagini[0].append(pygame.image.load("immagini\\white_spaceship_images\\SF03.png"))
    immagini[0].append(pygame.image.load("immagini\\white_spaceship_images\\SF04.png"))

    immagini[1].append(pygame.image.load("immagini\\white_spaceship_images\\SF01a_strip60.png"))
    immagini[1].append(pygame.image.load("immagini\\white_spaceship_images\\SF02a_strip60.png"))
    immagini[1].append(pygame.image.load("immagini\\white_spaceship_images\\SF03a_strip60.png"))
    immagini[1].append(pygame.image.load("immagini\\white_spaceship_images\\SF04a_strip60.png"))
    
    return immagini


    
def carica_texture_nemici(immagini = []):
    immagini = []
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Scout.png"))
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Bomber.png"))
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Frigate.png"))
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Cruiser.png"))
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Heavycruiser.png"))
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Battleship.png"))
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Mothership.png"))
    immagini.append(pygame.image.load("immagini\\nemici_images\\Alien-Spacestation.png"))
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

def collisione_pn(l1, l2, punteggio, temp, nemici_texture):
    lista_colpiti = []
    proiettili_colpiti = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i].rect.colliderect(l2[j]):
                proiettili_colpiti.append(l1[i])  
                lista_colpiti.append(l2[j])
                if l2[j].tipo_img == 0:
                    punteggio[0] += temp+50
                elif l2[j].tipo_img == 1:
                    punteggio[0] += temp+100
                elif l2[j].tipo_img == 2:
                    punteggio[0] += temp+150
                elif l2[j].tipo_img == 3:
                    punteggio[0] += temp+200
                elif l2[j].tipo_img == 4:
                    punteggio[0] += temp+250
                elif l2[j].tipo_img == 5:
                    punteggio[0] += temp+300
                elif l2[j].tipo_img == 6:
                    punteggio[0] += temp+350
                elif l2[j].tipo_img == 7:
                    punteggio[0] += temp+400
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



def genera_proiettili(n, distanza, aereo_rect, proiettile_width, proiettile_height):
    x1, y1 = aereo_rect.left, aereo_rect.top  
    center_x = x1 + aereo_rect.width / 2  

    width_tot = (n - 1) * distanza
    var = center_x - width_tot / 2

    punti = []

    for i in range(n):
        x = var + i * distanza - proiettile_width / 2
        y = y1 - proiettile_height  
        punti.append([x, y])  

    return punti

def frequenze_lista(lista):
    frequenze = {}
    for elemento in lista:
        if elemento in frequenze:
            frequenze[elemento] += 1
        else:
            frequenze[elemento] = 1
    return frequenze