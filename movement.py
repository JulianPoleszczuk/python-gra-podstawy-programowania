import pygame
import time
def ruszanie(gracz):
        klawisz = pygame.key.get_pressed()
        if klawisz[pygame.K_LEFT]:
            gracz.x -= gracz.pred
            if gracz.pred > 8:
                gracz.pred += 0.2
        if klawisz[pygame.K_RIGHT]:
            gracz.x += gracz.pred
            if gracz.pred > 8:
                gracz.pred += 0.2
        if klawisz[pygame.K_UP]:
                if gracz.pred > 8:
                    gracz.pred += 0.2
        gracz.y -= gracz.pred
        if klawisz[pygame.K_DOWN]:
                if gracz.pred > 8:
                    gracz.pred += 0.2
        gracz.y += gracz.pred