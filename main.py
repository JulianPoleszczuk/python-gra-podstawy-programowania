import pygame
pygame.init()
width, height = 640,640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("testa")
czcionka = pygame.font.SysFont("JetBrains Mono", 24)

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

    klawisz = pygame.key.get_pressed()
    if klawisz[pygame.K_LEFT]:
        gracz.x -= gracz.pred
    if klawisz[pygame.K_RIGHT]:
        gracz.x += gracz.pred
    if klawisz[pygame.K_UP]:
        gracz.y -= gracz.pred
    if klawisz[pygame.K_DOWN]:
        gracz.y += gracz.pred    

    sekundy = pygame.time.get_ticks() // 1000
    napis_czasu = czcionka.render(f"Czas: {sekundy}s", True, (255,255,255))
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), (gracz.x, gracz.y, gracz.szer, gracz.wys))
    screen.blit(napis_czasu, (10, 10))


    pygame.display.update()
    clock.tick(60) # Limit fps - warto dodac do ustawien wybor. Na razie jest 60 i powinno tyle wystarczyc
pygame.quit()