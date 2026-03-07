import pygame
import time
while True:
    warunek = True
    def ruszanie(gracz):
        klawisz = pygame.key.get_pressed()
        if klawisz[pygame.K_LEFT]:
            gracz.x -= gracz.pred
            while warunek==True:
                time.sleep(0.2)
                gracz.pred += 0.2
                if gracz.pred > 8:
                    warunek = False
        if klawisz[pygame.K_RIGHT]:
            gracz.x += gracz.pred
            while warunek==True:
                time.sleep(0.2)
                gracz.pred += 0.2
                if gracz.pred > 8:
                    warunek = False
        if klawisz[pygame.K_UP]:
            while warunek==True:
                time.sleep(0.2)
                gracz.pred += 0.2
                if gracz.pred > 8:
                    warunek = False
            gracz.y -= gracz.pred
        if klawisz[pygame.K_DOWN]:
            while warunek==True:
                time.sleep(0.2)
                gracz.pred += 0.2
                if gracz.pred > 8:
                    warunek = False
            gracz.y += gracz.pred   