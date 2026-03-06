import pygame
pygame.init()
width, height = 640,640
screen = pygame.display.set_mode((width, height))
dziala = True
while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala= False
pygame.quit()
print('test')