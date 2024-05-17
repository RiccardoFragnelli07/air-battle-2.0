import pygame

def carica_texture_jet(immagini = []):
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
    
def carica_texture_nemici(immagini = []):
    immagini.append([pygame.image.load("immagini\\NFighter.png"), pygame.image.load("immagini\\KFighter.png")])
    immagini.append([pygame.image.load("immagini\\NBomber.png"), pygame.image.load("immagini\\KBomber.png")])
    immagini.append([pygame.image.load("immagini\\NTorpedo.png"), pygame.image.load("immagini\\KTorpedo.png")])
    immagini.append([pygame.image.load("immagini\\NFrigate.png"), pygame.image.load("immagini\\KFrigate.png")])
    immagini.append([pygame.image.load("immagini\\NBattlecruiser.png"), pygame.image.load("immagini\\KBattlecruiser.png")])
    immagini.append([pygame.image.load("immagini\\NDreadnought.png"), pygame.image.load("immagini\\KDreadnought.png")])
