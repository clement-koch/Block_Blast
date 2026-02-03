import pygame 
from affichage import Grille

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
LARGEUR = 650
HAUTEUR = 950

# Créer la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
aff=Grille(fenetre,8,8)
# Titre de la fenêtre
pygame.display.set_caption("Ma fenêtre Pygame")

# Couleurs (RGB)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0,0,240)

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    # Remplir l'écran avec une couleur
    fenetre.fill(BLEU)
    aff.dessiner()
    # Mettre à jour l'affichage
    pygame.display.flip()
    
    # Limiter à 60 FPS
    clock.tick(60)

# Quitter proprement
pygame.quit()