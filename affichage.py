import pygame


class Grille:
    def __init__(self,display,longueur=8,largeur=8):
        self.longueur=longueur
        self.largeur=largeur
        self.display=display
    
    def dessiner (self):
        for case in range(self.longueur):
            for cases in range(self.largeur):
                pygame.draw.rect(self.display,(0,0,220),(50+case*70,150+cases*70,60,60))