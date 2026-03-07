import pygame
from przyciski import Przycisk
def menu(screen):
    szerokosc = 1500
    wysokosc = 640
    tlo = pygame.image.load("assets/tlo.png")
    tlo = pygame.transform.scale(tlo, (szerokosc, wysokosc))
    start_img = pygame.image.load("assets/Start_Game.png").convert_alpha()
    ustawienia_img = pygame.image.load("assets/Settings.png").convert_alpha()
    wyjscie_img = pygame.image.load("assets/Exit_Game.png").convert_alpha()
    przycisk_start = Przycisk(100,200,start_img)
    przycisk_wyjscie = Przycisk(450,200,wyjscie_img)
    przycisk_ustawienia = Przycisk(900,200,ustawienia_img)
    dziala = True
    while dziala:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(tlo,(0,0))
        przycisk_start.wyswietlanie_przyciskow(screen)
        przycisk_wyjscie.wyswietlanie_przyciskow(screen)
        przycisk_ustawienia.wyswietlanie_przyciskow(screen)
        pygame.display.update()