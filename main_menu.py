import pygame
import sys
import subprocess

pygame.init()
szerokosc = 1280
wysokosc = 720
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("test")

tlo = pygame.image.load("assets/tlo.png")
tlo = pygame.transform.scale(tlo, (szerokosc, wysokosc))

bialy = (255,255,255)
przezroczystosc_niebieska = (0,80,200,180)
niebieski_pods = (0,140,255,220)
CIEN = (0,0,0)
try:
    czcionka_tytulowa = pygame.font.Font("assets/czcionki/JupiteroidLight-R90XW.ttf", 72)
    czcionka_przycisk = pygame.font.Font("assets/czcionki/JupiteroidLight-R90XW.ttf", 36)
except:
    czcionka_tytulowa = pygame.font.Font(None, 72)
    czcionka_przycisk = pygame.font.Font(None, 36)
class Przycisk:
    def __init__(self,tekst,y,akcja):
        self.tekst = tekst
        self.y = y
        self.akcja = akcja
        self.szerokosc, self.wysokosc = 320,70
        self.rect = pygame.Rect(0,0,self.szerokosc,self.wysokosc)
        self.rect.center = (szerokosc//6,y)
    def draw(self,poz_mysz,win):
        is_hover = self.rect.collidepoint(poz_mysz)
        kolor = niebieski_pods if is_hover else przezroczystosc_niebieska
        button_tlo = pygame.Surface((self.szerokosc,self.wysokosc),pygame.SRCALPHA)
        pygame.draw.rect(button_tlo, kolor,(0,0,self.szerokosc,self.wysokosc),border_radius=16)
        win.blit(button_tlo,self.rect)

        tekst_surf = czcionka_przycisk.render(self.tekst,True,(255,255,255))
        tekst_rect = tekst_surf.get_rect(center=self.rect.center)
        cien = czcionka_przycisk.render(self.tekst,True,CIEN)
        win.blit(cien,(tekst_rect.x+2,tekst_rect.y+2))
        win.blit(tekst_surf,tekst_rect)
    def czy_klik(self,klik,poz_mysz):
        return self.rect.collidepoint(poz_mysz) and klik[0]




przyciski = [
    Przycisk("Start", 320-70,"new"),
    Przycisk("Settings",400-70,"settings"),
    Przycisk("Statistics",480-70,"statistics"),
    Przycisk("Quit Game",560-70,"quit"),
]

dziala = True
clock = pygame.time.Clock()
while dziala:
    clock.tick(60)
    ekran.blit(tlo,(0,0))
    poz_mysz = pygame.mouse.get_pos()
    klik = pygame.mouse.get_pressed()
    tytul = czcionka_tytulowa.render("******",True,(0,0,0))
    cien = czcionka_tytulowa.render("******", True, CIEN)
    ekran.blit(cien,(szerokosc//2 - tytul.get_width()//2 + 3, 103))
    ekran.blit(tytul,(szerokosc//2 - tytul.get_width()//2,100))
    for i in przyciski:
        i.draw(poz_mysz,ekran)
        if i.czy_klik(klik, poz_mysz):
            pygame.time.delay(200)
            if i.akcja == "new":
                print("test1")
                pygame.quit()
                subprocess.run(["python","main.py"])
                sys.exit()
            elif i.akcja == "settings":
                print("test2")
            elif i.akcja == "statistics":
                print("test3")
            elif i.akcja == "quit":
                dziala = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala= False
    pygame.display.flip()
pygame.quit()
print("test")


