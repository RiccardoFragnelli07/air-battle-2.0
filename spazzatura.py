import pygame
import math
import random

def generate_pentagon_rectangles(rectangle_width, rectangle_height, distance):
    rectangles = []

    # Genera il centro del pentagono in modo casuale sull'asse x
    pentagon_center_x = random.randint(rectangle_width // 2, 800 - rectangle_width // 2)

    # Calcola la distanza dal centro del pentagono al vertice
    radius = distance / (2 * math.sin(math.radians(180 / 5)))

    # Calcola l'angolo per ogni vertice del pentagono
    angles = [math.radians(angle) for angle in range(90, 450, 72)]

    # Genera i rettangoli per ciascun vertice del pentagono
    for angle in angles:
        x = pentagon_center_x + radius * math.cos(angle) - rectangle_width // 2
        y = radius * math.sin(angle)

        rectangles.append(pygame.Rect(x, y, rectangle_width, rectangle_height))

    # Trasla i rettangoli in modo che il rettangolo più basso abbia il suo fondo coincidente con y = 0
    min_y = min(rect.y for rect in rectangles)
    for rect in rectangles:
        rect.y -= min_y

    return rectangles

# Esempio di utilizzo
pygame.init()
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

distance_between_vertices = 100  # Distanza tra i vertici del pentagono
rectangles = generate_pentagon_rectangles(30, 30, distance_between_vertices)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Disegna i rettangoli
    for rect in rectangles:
        pygame.draw.rect(screen, (255, 0, 0), rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()