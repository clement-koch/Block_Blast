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
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                if self.grid[y][x]==0:
                    pygame.draw.rect(self.display,(0,0,220),(50+x*70,150+y*70,60,60))
                else:
                    pygame.draw.rect(self.display,(255,0,0),(50+x*70,150+y*70,60,60))

    def clear_full_lines(self):
        full_rows = [i for i, row in enumerate(self.grid) if all(cell != 0 for cell in row)]
        full_cols = []
        for x in range(len(self.grid[0])):
            if all(self.grid[y][x] != 0 for y in range(len(self.grid))):
                full_cols.append(x)

        # vider les lignes et colonnes complètes
        for y in full_rows:
            for x in range(len(self.grid[y])):
                self.grid[y][x] = 0

        for x in full_cols:
            for y in range(len(self.grid)):
                self.grid[y][x] = 0

        points = len(full_rows) * 100 + len(full_cols) * 100
        return points


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

    grid_attente=[
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]

    def __init__(self, x, y, display,piece_en_attente=False):
        self.x = x
        self.y = y
        self.display = display
        self.piece_en_attente = piece_en_attente
        self.pieces_attente = []

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
                return neuf_pieces[1]

    def _normalize_piece(self, piece):
        xs = [p[0] for p in piece]
        ys = [p[1] for p in piece]
        min_x, min_y = min(xs), min(ys)
        return [(px - min_x, py - min_y) for px, py in piece]

    def dessiner_attente(self):
        # ne remplit pas automatiquement : user veut que non direct
        # positions des trois emplacements bas
        slots = [(85, 750), (275, 750), (465, 750)]
        block_size = 25
        for idx, piece in enumerate(self.pieces_attente):
            base_x, base_y = slots[idx]
            normalized = self._normalize_piece(piece)
            # dessiner chaque bloc de la pièce
            for (px, py) in normalized:
                pygame.draw.rect(self.display, (255, 255, 0),
                                 (base_x + px * block_size, base_y + py * block_size, block_size - 2, block_size - 2))
            # cadre du slot
            pygame.draw.rect(self.display, (255, 255, 255), (base_x - 5, base_y - 5, 3 * block_size + 10, 3 * block_size + 10), 2)

    def attente(self):
        if not self.piece_en_attente:
            self.piece_en_attente = True
            while len(self.pieces_attente) < 3:
                self.pieces_attente.append(self.choix_pieces())

    def ajout(self):
        if len(self.pieces_attente) < 3:
            piece = self.choix_pieces()
            self.pieces_attente.append(piece)

    def refill_all(self):
        while len(self.pieces_attente) < 3:
            self.pieces_attente.append(self.choix_pieces())

    def can_place(self, grille, grid_x, grid_y, piece):
        normalized = self._normalize_piece(piece)
        for px, py in normalized:
            gx = grid_x + px
            gy = grid_y + py
            if gx < 0 or gx >= len(grille[0]) or gy < 0 or gy >= len(grille):
                return False
            if grille[gy][gx] != 0:
                return False
        return True

    def place_piece(self, grille, grid_x, grid_y, piece):
        normalized = self._normalize_piece(piece)
        for px, py in normalized:
            gx = grid_x + px
            gy = grid_y + py
            grille[gy][gx] = 1

    def return_piece(self, piece):
        self.pieces_attente.insert(0, piece)
        if len(self.pieces_attente) > 3:
            self.pieces_attente = self.pieces_attente[-3:]

    def can_place_any(self, grille):
        if not self.pieces_attente:
            return False

        rows = len(grille)
        cols = len(grille[0]) if rows > 0 else 0
        for piece in self.pieces_attente:
            for gx in range(cols):
                for gy in range(rows):
                    if self.can_place(grille, gx, gy, piece):
                        return True
        return False