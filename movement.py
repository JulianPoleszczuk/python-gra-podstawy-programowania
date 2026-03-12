import pygame

grawitacja = 1

def ruszanie(gracz):

    klawisz = pygame.key.get_pressed()

    # skok
    if klawisz[pygame.K_SPACE] and not gracz.skacze:
        gracz.pred_y = -15
        gracz.skacze = True

    # kucanie
    if klawisz[pygame.K_LSHIFT]:
        gracz.kuca = True
    else:
        gracz.kuca = False

    # grawitacja
    gracz.pred_y += grawitacja
    gracz.y += gracz.pred_y

    # podłoga
    if gracz.y >= gracz.ziemia:
        gracz.y = gracz.ziemia
        gracz.pred_y = 0
        gracz.skacze = False