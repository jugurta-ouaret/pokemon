import json 

import pygame

# Initialisation de Pygame
pygame.init()

# Dimension de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

#récupérer les données de dictionnaire 
with open("../pokemon/dict_Json/pokedex.json", "r") as f:
    data=json.load(f)
    
    # Récupérer le nom du pokemon1 de niveau1
    nom_pokemon = data["pokemon1"][1]["Niveau1"]["nom"]
    type_pokemon = data["pokemon1"][1]["Niveau1"]["type"][0]
    image_pokemon=data["pokemon1"][1]["Niveau1"]["image"]

#chargement de l'image 
pokemon_image = pygame.image.load(image_pokemon)

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Affichage Pokémon")

# Boucle principale du jeu
continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    # Effacer la fenêtre
    fenetre.fill(BLANC)

    # Afficher l'image du Pokémon
    fenetre.blit(pokemon_image, (0, 0))

    # Création de l'objet de texte pour le nom du Pokémon
    font = pygame.font.Font(None, 25)
    pokemon_texte_nom = font.render(nom_pokemon, True, NOIR)

    # Afficher le nom du Pokémon
    fenetre.blit(pokemon_texte_nom, (0, pokemon_image.get_height()))

    # Création de l'objet de texte pour le type du Pokémon
    pokemon_texte_type = font.render(type_pokemon, True, NOIR)

    # Afficher le type du Pokémon
    fenetre.blit(pokemon_texte_type, (0, pokemon_image.get_height() + pokemon_texte_nom.get_height()))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()

