import pygame
from template import *
from random import randint

class Grille:

    grid = [ 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0]
        ]

    def __init__(self,display,longueur=8,largeur=8):
        self.longueur=longueur
        self.largeur=largeur
        self.display=display
    
    def dessiner (self):
        for case in range(self.longueur):
            for cases in range(self.largeur):
                pygame.draw.rect(self.display,(0,0,220),(50+case*70,150+cases*70,60,60))

class En_Attente:
    def __init__(self,display,longueur=3,largeur=3):
        self.display=display
        self.longueur=longueur
        self.largeur=largeur

    def afficher(self):
        for case in range (self.longueur):
            for cases in range(self.largeur):
                pygame.draw.rect(self.display,(0,0,220),(85+case*40,750+cases*40,30,30))

        for case in range (self.longueur):
            for cases in range(self.largeur):
                pygame.draw.rect(self.display,(0,0,220),(275+case*40,750+cases*40,30,30))

        for case in range (self.longueur):
            for cases in range(self.largeur):
                pygame.draw.rect(self.display,(0,0,220),(465+case*40,750+cases*40,30,30))


class Pieces:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def choix_pieces(self):
        nb=randint(1,6)
        match nb:
            case 1:
                num=randint(1,3)
                return deux_pieces[num]
            case 2:
                num=randint(1,7)
                return trois_pieces[num]
            case 3:
                num=randint(1,19)
                return quatre_pieces[num]
            case 4:
                num=randint(1,7)
                return cinq_pieces[num]
            case 5:
                num=randint(1,2)
                return six_pieces[num]
            case 6:
                return neuf_pieces.values()
            
    def attente(self):
        if piece_en_attente<=0:
            for i in range (2):
                self.choix_pieces()

    def ajout (self):
        piece=self.choix_pieces()
        