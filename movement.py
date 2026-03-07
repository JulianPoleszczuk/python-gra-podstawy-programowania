import pygame
def ruszanie(gracz):
    klawisz = pygame.key.get_pressed()
    if klawisz[pygame.K_LEFT]:
        gracz.x -= gracz.pred
    if klawisz[pygame.K_RIGHT]:
        gracz.x += gracz.pred
    if klawisz[pygame.K_UP]:
        gracz.y -= gracz.pred
    if klawisz[pygame.K_DOWN]:
        gracz.y += gracz.pred   