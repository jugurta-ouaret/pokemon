import pygame
import json
from Pokemon import afficher_profil_pokemon

# Initialisation de Pygame
pygame.init()

#fonction de l'affichage de pokémone 
def afficher_liste_pokemons():
    
    # Dimensions de la fenêtre
    WIDTH = 1300
    HEIGHT = 780

    # Couleurs
    WHITE = (255, 255, 255)

    # Création de la fenêtre principale
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Liste pokemons")

    # Charger l'arrière-plan
    background = pygame.image.load("../pokemon/Assets/images/Pokemons.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Charger les données du dictionnaire
    with open("../pokemon/dict_Json/pokemon.json", "r") as f:
        pokemon_data = json.load(f)

    # Créer une liste de tous les Pokémon de niveau 1
    pokemon_list = [pokemon['image'][1]['Gauche'] for pokemon in pokemon_data['Niveau1']]

    # Charger les images
    images = []
    for image_path in pokemon_list:
        image = pygame.transform.scale(pygame.image.load(image_path), (150, 150))
        images.append(image)

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Vérifier si le clic est sur l'une des images
                    for i, image in enumerate(images):
                        if image.get_rect(topleft=(30 + i % 8 * 150, 150 + i // 8 * 150)).collidepoint(event.pos):
                            # Obtenir le nom du Pokémon correspondant à l'image
                            pokemon_name = pokemon_name = [pokemon['nom'] for pokemon in pokemon_data['Niveau1']] [i]
                            # Afficher les détails du Pokémon dans une nouvelle fenêtre
                            afficher_profil_pokemon(pokemon_name)

        # Affichage de l'arrière-plan
        screen.blit(background, (0, 0))

        # Dessiner les images sur l'écran
        x, y = 30, 150
        for i, image in enumerate(images):
            screen.blit(image, (x, y))
            x += image.get_width()
            if i % 8 == 7:  # Passer à la ligne suivante après avoir dessiné 8 images
                y += image.get_height()
                x = 30

        # Rafraîchissement de la fenêtre principale
        pygame.display.flip()

# Quitter Pygame
pygame.quit()

afficher_liste_pokemons()