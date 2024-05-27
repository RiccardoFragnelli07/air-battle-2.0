import pygame
import math

# Inizializzazione di Pygame
pygame.init()

# Definizione delle dimensioni della finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Proiettili da un rettangolo")

# Colori
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Definizione del rettangolo (dimensioni fisse)
rect_x, rect_y = 300, 200
rect_width, rect_height = 200, 150
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Parametri dei proiettili
num_projectiles = 12  # Cambia questo valore per testare diverse configurazioni
distance_between_projectiles = 20  # Distanza fissa tra i proiettili
projectile_width, projectile_height = 5, 10  # Dimensioni del proiettile

# Funzione per generare proiettili dal bordo superiore del rettangolo
def generate_projectiles(n, fixed_distance, rect):
    x1, y1 = rect.left, rect.top  # Coordinate del vertice superiore sinistro
    center_x = x1 + rect.width / 2  # Centro del bordo superiore del rettangolo

    # Calcolare l'offset per mantenere i proiettili simmetrici rispetto al centro
    total_width = (n - 1) * fixed_distance
    offset = center_x - total_width / 2

    points = []

    for i in range(n):
        x = offset + i * fixed_distance  # Calcolo della posizione x
        y = y1 - projectile_height  # La posizione y è il bordo superiore meno l'altezza del proiettile
        points.append((x, y))  # Aggiungi solo le coordinate x e y

    return points

# Generare i proiettili
projectiles = generate_projectiles(num_projectiles, distance_between_projectiles, rect)
print(projectiles)
# Loop principale del gioco
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect = pygame.Rect(1/3, 13/12, 40, 80)

pygame.quit()