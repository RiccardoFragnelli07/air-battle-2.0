import pygame
import sys

pygame.init()

# Dimensioni della finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doppio Salto con Pavimento e Soglia")

# Colori
black = (0, 0, 0)
white = (255, 255, 255)

# Proprietà del rettangolo
rect_width, rect_height = 50, 50
rect_x, rect_y = width // 2, height - rect_height
rect_color = white

# Coordinata y del pavimento e della soglia di salto
floor_y = height - rect_height
jump_stop_y = height - 2 * rect_height

# Velocità e gravità
gravity = 1
jump_strength = -15
double_jump_strength = -12
velocity_y = 0
jumps = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jumps < 2:
                    if jumps == 0:
                        velocity_y = jump_strength
                    else:
                        velocity_y = double_jump_strength
                    jumps += 1

    # Applicare la gravità
    velocity_y += gravity
    rect_y += velocity_y

    # Controllare collisioni con il pavimento
    if rect_y >= floor_y:
        rect_y = floor_y
        velocity_y = 0
        jumps = 0

    # Fermarsi alla coordinata y specifica durante il salto
    if rect_y <= jump_stop_y:
        rect_y = jump_stop_y
        velocity_y = 0

    # Disegnare tutto
    screen.fill(black)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    clock.tick(60)