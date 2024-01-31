import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre principale
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fenêtre Principale")

# Chargement de l'image du bouton
button_image = pygame.image.load('../pokemon/Assets/images/Niveau1/Gauche/1_Salameche.png')

# Position du bouton
button_x, button_y = 100, 100

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si les coordonnées du clic sont à l'intérieur du bouton
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if button_x < mouse_x < button_x + button_image.get_width() and button_y < mouse_y < button_y + button_image.get_height():
                # Ouvrir une autre fenêtre lorsque le bouton est cliqué
                other_window = pygame.display.set_mode((400, 300))
                pygame.display.set_caption("Autre Fenêtre")

    # Afficher le bouton sur la fenêtre principale
    screen.blit(button_image, (button_x, button_y))

    # Rafraîchir l'écran principal
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
