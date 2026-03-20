import pygame 
from affichage import *

# Initialisation de Pygame
pygame.init()

LARGEUR = 650
HAUTEUR = 950

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
aff = Grille(fenetre)
att = En_Attente(fenetre)
piec = Pieces(0, 0, fenetre)
piec.attente()  # initialise la file d'attente au démarrage
pygame.display.set_caption("blok blast")


# boucle de jeu
running = True
clock = pygame.time.Clock()

slots = [(85, 750), (275, 750), (465, 750)]
slot_size = 3 * 25
selected_piece = None
dragging = False
drag_x = 0
drag_y = 0
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                piec.ajout()
            elif event.key == pygame.K_SPACE:
                piec.refill_all()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            for idx, (sx, sy) in enumerate(slots):
                if sx <= mx <= sx + slot_size and sy <= my <= sy + slot_size:
                    if idx < len(piec.pieces_attente):
                        selected_piece = piec.pieces_attente.pop(idx)
                        dragging = True
                        drag_x, drag_y = mx, my
                    break

        elif event.type == pygame.MOUSEMOTION and dragging:
            drag_x, drag_y = event.pos

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and dragging:
            mx, my = event.pos
            grid_x = (mx - 50) // 70
            grid_y = (my - 150) // 70
            placed = False
            if 0 <= grid_x < 8 and 0 <= grid_y < 8 and selected_piece is not None:
                if piec.can_place(aff.grid, grid_x, grid_y, selected_piece):
                    piec.place_piece(aff.grid, grid_x, grid_y, selected_piece)
                    placed = True
                    gained = aff.clear_full_lines()
                    score += gained
            if not placed and selected_piece is not None:
                piec.return_piece(selected_piece)

            selected_piece = None
            dragging = False

    # fond
    fenetre.fill((0, 0, 240))
    pygame.draw.rect(fenetre, (0, 0, 150), (40, 140, 570, 570))

    # grille
    aff.dessiner()

    # attente
    att.afficher()
    piec.dessiner_attente()

    if dragging and selected_piece is not None:
        normalized = piec._normalize_piece(selected_piece)
        for px, py in normalized:
            pygame.draw.rect(fenetre, (0, 255, 0), (drag_x + px * 25 - 12, drag_y + py * 25 - 12, 23, 23))

    # respawn automatique quand il n'y a plus de pièces
    if len(piec.pieces_attente) == 0:
        piec.refill_all()

    # condition de défaite : aucune pièce ne peut être posée (et on n'est pas en train de drag)
    if not dragging and not piec.can_place_any(aff.grid):
        font_go = pygame.font.Font(None, 72)
        text_go = font_go.render("Game Over", True, (255, 50, 50))
        fenetre.blit(text_go, (150, 420))

        font_retry = pygame.font.Font(None, 30)
        text_retry = font_retry.render("Appuyez sur R pour recommencer", True, (255, 255, 255))
        fenetre.blit(text_retry, (150, 500))
        pygame.display.flip()

        # attendre le re-start ou quitter
        waiting = True
        while waiting:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                    waiting = False
                elif e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                    # réinitialiser état
                    aff.grid = [[0] * 8 for _ in range(8)]
                    piec.pieces_attente.clear()
                    piec.refill_all()
                    score = 0
                    waiting = False
        continue

    # score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    fenetre.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()