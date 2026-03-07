import pygame
import time
from movement import ruszanie
pygame.init()
width, height = 1500,640
FPS = 60
screen = pygame.display.set_mode((width, height,))
pygame.display.set_caption("testa")
czcionka = pygame.font.SysFont("JetBrains Mono", 24)
print('test')
class Postac:
        x = 50
        y = 50
        szer = 60
        wys = 60
        pred = 5

gracz=Postac()
dziala = True
clock = pygame.time.Clock() 

while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala= False
    ruszanie(gracz)

    sekundy = pygame.time.get_ticks() // 1000
    napis_czasu = czcionka.render(f"Czas: {sekundy}s", True, (255,255,255))
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), (gracz.x, gracz.y, gracz.szer, gracz.wys))
    screen.blit(napis_czasu, (10, 10))


    pygame.display.update()
    clock.tick(FPS) # Limit fps - warto dodac do ustawien wybor. Na razie jest 60 i powinno tyle wystarczyc
pygame.quit()