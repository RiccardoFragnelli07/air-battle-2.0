import pygame

HEIGHT = 690
WIDTH = 500
VEL = 7

class Proiettile:
    def __init__(self, rect, img, screen) -> None:
        self.rect = rect
        self.img = img
        self.screen = screen
        self.proiettile = []
        self.check = False
        proiettile_width = self.img.get_width() // 5
        proiettile_height = self.img.get_height()
        for i in range(5):
            startx = i * proiettile_width
            img_part = self.img.subsurface((startx, 0, proiettile_width, proiettile_height))
            img_part = pygame.transform.scale(img_part, (50, 50))
            self.proiettile.append(img_part)

    def move(self, aereo, dimx):
        self.rect.y = aereo.rect.y - VEL
        if self.check == False:
            self.rect.x = aereo.rect.x + dimx//2
            self.check = True

    def draw(self, screen, ind):
        screen.blit(self.proiettile[0], (self.rect.x, self.rect.y))