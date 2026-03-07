import pygame
class Przycisk:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def wyswietlanie_przyciskow(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))