import pygame
pygame.init()
postacie =pygame.image.load("assets/tux.png").convert_alpha()
wysokosc_1 = 32
szerokosc_1 = 32
pingwin_biegajacy = postacie.subsurface((0,0, szerokosc_1, wysokosc_1))
def ruszanie(gracz):
        klawisz = pygame.key.get_pressed()
        if klawisz[pygame.K_LSHIFT]:
            pass

