# funzioni utili
import pygame
from random import randint
import math

WIDTH, HEIGHT = 500, 700

def carica_texture_spaceships():
    immagini = []
    immagini.append([])
    immagini.append([])

    for i in range(4):
        immagini[0].append(pygame.image.load(f"immagini\\white_spaceship_images\\SF0{i+1}.png"))
    for i in range(4):
        immagini[1].append(pygame.image.load(f"immagini\\white_spaceship_images\\SF0{i+1}a_strip60.png"))
    
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


def genera_navicella(tipo):
    if tipo == 0:
        percentuale = randint(0, 100)
        if percentuale < 0:
            ris = randint(0, 1)
        else:
            ris = 2
    elif tipo == 1:
        percentuale = randint(0, 100)
        if percentuale < 45:
            ris = 3
        elif percentuale < 80:
            ris = 4
        else:
            ris = 5
    elif tipo == 2:
        ris = 6 
    
    return ris

def collisione_pn(l1, l2):
    lista_colpiti = []
    proiettili_colpiti = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i].rect.colliderect(l2[j]) and l1[i].vel[1] < 0:
                proiettili_colpiti.append(l1[i])   
                lista_colpiti.append(l2[j])
                break
            
    return [proiettili_colpiti, lista_colpiti]


def distanza_punti(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(0.5)


def genera_proiettili(n, distanza, aereo_rect, proiettile_rect):
    x1, y1 = aereo_rect.left, aereo_rect.top  
    center_x = x1 + aereo_rect.width / 2  
    width_tot = (n - 1) * distanza
    var = center_x - width_tot / 2

    punti = []
    for i in range(n):
        x = var + i * distanza - proiettile_rect.width / 2
        y = y1 - proiettile_rect.height  
        punti.append([x, y])  

    return punti



def calcola_direzione(rect, arrivo):
    dx = arrivo[0] - rect.x
    dy = arrivo[1] - rect.y
    distanza = math.hypot(dx, dy)
    if distanza == 0:
        return [0, 0]
    direction_x = dx / distanza
    direction_y = dy / distanza
    return [direction_x, direction_y]


def frequenze_lista(lista):
    frequenze = {}
    for elemento in lista:
        if elemento in frequenze:
            frequenze[elemento] += 1
        else:
            frequenze[elemento] = 1
    return frequenze

def crea_posizioni(n, dim, start, end):
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    distanza_x = delta_x / (n - 1)
    distanza_y = delta_y / (n - 1)

    posizione_rettangoli = []
    for i in range(n):
        pos_x = start[0] + distanza_x * i
        pos_y = start[1] + distanza_y * i
        posizione_rettangoli.append([pos_x, pos_y])

    lista_rettangoli = []
    for i in range(n):
        lista_rettangoli.append(pygame.Rect(posizione_rettangoli[i][0], posizione_rettangoli[i][1], dim[0], dim[1]))
        
    return lista_rettangoli


def calculate_speeds(velocity, rectangles, destination_point):
    speeds = []

    for rect in rectangles:
        rect_center = rect.center
        dx = destination_point[0] - rect_center[0]
        dy = destination_point[1] - rect_center[1]

        # Calcola la distanza totale dal rettangolo al punto di destinazione
        distance = max(abs(dx), abs(dy))

        # Calcola le velocità x e y necessarie per raggiungere il punto
        if distance != 0:
            speed_x = velocity * dx / distance
            speed_y = velocity * dy / distance
        else:
            speed_x, speed_y = 0, 0

        speeds.append([speed_x, speed_y])

    return speeds


def genera_rettangoli_casuali(n_rettangoli, rect):
    rettangoli = []
    tentativi_max = 10000
    for _ in range(n_rettangoli):
        tentativi = 0
        while tentativi < tentativi_max:
            x_position = randint(0, WIDTH - rect.width)
            y_position = 0 

            new_rect = pygame.Rect(x_position, y_position, rect.width, rect.height)
            overlap = any(new_rect.colliderect(rect) for rect in rettangoli)

            if not overlap:
                rettangoli.append(new_rect)
                break
            
            tentativi += 1
        if tentativi < tentativi_max == False:
            return rettangoli

    return rettangoli



def generate_rectangles_on_edges(num_rectangles, rectangle_width, rectangle_height, min_height, max_height):
    rectangles = []
    max_attempts = 10000

    # Assicurare che ci sia almeno un rettangolo su ogni bordo
    remaining_rectangles = num_rectangles - 3
    top_count = randint(1, remaining_rectangles + 1)
    remaining = remaining_rectangles - (top_count - 1)
    left_count = randint(1, remaining + 1)
    right_count = remaining - (left_count - 1) + 1

    def create_rectangle(x_position, y_position):
        return pygame.Rect(x_position, y_position, rectangle_width, rectangle_height)

    def is_overlapping(new_rect, rectangles):
        return any(new_rect.colliderect(rect) for rect in rectangles)

    def generate_rectangles_on_side(x_func, count):
        generated = 0
        while generated < count:
            attempts = 0
            while attempts < max_attempts:
                x_position = x_func()
                y_position = randint(min_height, max_height - rectangle_height)
                new_rect = create_rectangle(x_position, y_position)

                if not is_overlapping(new_rect, rectangles):
                    rectangles.append(new_rect)
                    generated += 1
                    break

                attempts += 1
            if attempts == max_attempts:
                print(f"Non è stato possibile generare un rettangolo non sovrapposto dopo {max_attempts} tentativi.")
                break

    # Genera rettangoli sulla cima
    for _ in range(top_count):
        attempts = 0
        while attempts < max_attempts:
            x_position = randint(0, WIDTH - rectangle_width)
            y_position = 0
            new_rect = create_rectangle(x_position, y_position)

            if not is_overlapping(new_rect, rectangles):
                rectangles.append(new_rect)
                break

            attempts += 1
        if attempts == max_attempts:
            print(f"Non è stato possibile generare un rettangolo non sovrapposto dopo {max_attempts} tentativi.")
            break

    # Genera rettangoli sul bordo sinistro
    generate_rectangles_on_side(lambda: 0, left_count)

    # Genera rettangoli sul bordo destro
    generate_rectangles_on_side(lambda: WIDTH - rectangle_width, right_count)

    return rectangles


def generate_pentagon_rectangles(rectangle_width, rectangle_height, distance):
    rectangles = []

    pentagon_height = distance / (2 * math.sin(math.radians(180 / 5)))

    y = 0
    while y < pentagon_height:
        x = randint(rectangle_width // 2, 800 - rectangle_width // 2)
        rectangles.append(pygame.Rect(x - rectangle_width // 2, y, rectangle_width, rectangle_height))
        y += rectangle_height

    return rectangles


def mothership_nello_schermo(lista):
    for el in lista:
        if el.tipo == 6:
            return True
    return False