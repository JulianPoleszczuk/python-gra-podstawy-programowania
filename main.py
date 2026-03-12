import pygame
pygame.init()
width, height = 1500, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pingwin Runner")
clock = pygame.time.Clock()
FPS = 60
pingwiny = pygame.image.load("assets/tux.png").convert_alpha()
szerokosc = 32
wysokosc = 32
run_frames = []
duck_frames = []
for i in range(8):
    frame = pingwiny.subsurface((i*szerokosc, 0, szerokosc, wysokosc))
    frame = pygame.transform.scale(frame, (60, 60))
    run_frames.append(frame)
for i in range(3):
    frame = pingwiny.subsurface((i*szerokosc, 3*wysokosc, szerokosc, wysokosc))
    frame = pygame.transform.scale(frame, (60, 60))
    duck_frames.append(frame)
class Postac:
    def __init__(self):
        self.x = 200
        self.y = 400
        self.ziemia = 400
        self.pred_y = 0
        self.skacze = False
        self.kuca = False
        self.frame = 0
        self.poprzedni_stan = False
    def ruch(self):
        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_LSHIFT]:
            self.kuca = True
        else:
            self.kuca = False
        if klawisze[pygame.K_SPACE] and not self.skacze:
            self.pred_y = -15
            self.skacze = True
        self.pred_y += 0.8
        self.y += self.pred_y
        if self.y >= self.ziemia:
            self.y = self.ziemia
            self.pred_y = 0
            self.skacze = False
gracz = Postac()
dziala = True
while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala = False
    gracz.ruch()
    if gracz.kuca != gracz.poprzedni_stan:
        gracz.frame = 0
    gracz.poprzedni_stan = gracz.kuca
    screen.fill((0,0,0))
    if gracz.kuca:
        if gracz.frame < len(duck_frames)-1:
            gracz.frame += 0.2
        sprite = duck_frames[int(gracz.frame)]
    else:
        gracz.frame += 0.2
        if gracz.frame >= len(run_frames):
            gracz.frame = 0
        sprite = run_frames[int(gracz.frame)]
    screen.blit(sprite, (gracz.x, gracz.y))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()