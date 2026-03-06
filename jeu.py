import pygame 
from affichage import *

# Initialisation de Pygame
pygame.init()

LARGEUR = 650
HAUTEUR = 950

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
aff=Grille(fenetre)
att=En_Attente(fenetre)
piec=Pieces(x,y)
pygame.display.set_caption("blok blast")


BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0,0,240)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                x = event.pos[0]
                y = event.pos[1]
                piec.x = (x-50)//70
                piec.y = (y-150)//70
                piec.ajout()
                
    
    
    fenetre.fill(BLEU)
    pygame.draw.rect(fenetre,(0,0,150),(40,140,570,570))
    aff.dessiner()
    att.afficher()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()