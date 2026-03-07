import pygame
import sys
import subprocess
pygame.init()
szerokosc = 1500
wysokosc = 640
screen = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("test")
tlo = pygame.image.load("assets/tlo.png")
tlo = pygame.transform.scale(tlo, (szerokosc, wysokosc))
dziala = True
while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala = False
    screen.blit(tlo, (0,0))
    pygame.display.update()
pygame.quit()
class Przycisk:
    def __init__(self,tekst,srodek,akcja):
        self.tekst = tekst
        self.srodek = srodek
        self.akcja = akcja
        self.szerokosc,self.wysokosc = 320,70
    def