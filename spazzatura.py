import pygame
from moviepy.editor import VideoFileClip

# Inizializza Pygame
pygame.init()

# Dimensioni della finestra
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Riproduzione video in Pygame")

# Carica il video usando MoviePy
video_path = "Clip 4.mp4"
clip = VideoFileClip(video_path)

# Funzione per convertire il frame di MoviePy in superficie di Pygame
def to_pygame_surface(moviepy_frame):
    # MoviePy restituisce frame in formato RGB, convertiamoli a superficie Pygame
    frame = pygame.surfarray.make_surface(moviepy_frame.swapaxes(0, 1))
    return frame

# Loop principale del gioco
running = True
clock = pygame.time.Clock()
video_fps = clip.fps

# Riproduzione video
for frame in clip.iter_frames(fps=video_fps, dtype="uint8"):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    frame_surface = to_pygame_surface(frame)
    screen.blit(frame_surface, (0, 0))
    pygame.display.flip()
    clock.tick(video_fps)

# Pulisce Pygame e MoviePy
clip.close()
pygame.quit()