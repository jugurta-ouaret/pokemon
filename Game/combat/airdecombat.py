import json
import pygame

# Initialisation de Pygame
pygame.init()

# Dimension de la fenêtre
largeur_fenetre = 1280
hauteur_fenetre = 720

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
battle_bg = pygame.image.load("../pokemon/Assets/images/battle_bg.png")

with open("../pokemon/dict_Json/pokemon.json", "r") as f:
    data = json.load(f)
    
    niveau1_data = data["Niveau1"]
    i = 0
    for pokemon in niveau1_data:
        nom = pokemon["nom"]
        type = pokemon["type"]
        pv = pokemon["PV"]
        attack = pokemon["Attaque"]
        special_attack = pokemon["AttaqueSp"]
        defense = pokemon["Defense"]
        speed = pokemon["Vitesse"]
        
        # Access the image paths directly under the "image" key
        image_gauche = pokemon["image"][1]["Gauche"]
        image_droite = pokemon["image"][0]["droite"]

        # Récupérer les informations du premier Pokémon de niveau 1
        image_pokemon1 = image_gauche

        # Récupérer les informations du premier Pokémon de niveau 2
        image_pokemon2 = image_droite

# Chargement des images des Pokémon
pokemon_image1 = pygame.image.load(image_pokemon1)
pokemon_image2 = pygame.image.load(image_pokemon2)

# Redimensionnement des images des Pokémon
pokemon_image1 = pygame.transform.scale(pokemon_image1, (pokemon_image1.get_width() // 2, pokemon_image1.get_height() // 2))
pokemon_image2 = pygame.transform.scale(pokemon_image2, (pokemon_image2.get_width() // 2, pokemon_image2.get_height() // 2))

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("PokeWorld - Battle")

# Initialisation des barres de vie
barre_vie_pokemon1 = pygame.Surface((pokemon_image1.get_width(), 10))
barre_vie_pokemon2 = pygame.Surface((pokemon_image2.get_width(), 10))
barre_vie_pokemon1.fill((0,255, 0))
barre_vie_pokemon2.fill((0, 255, 0))

# Boucle principale du jeu
continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    # Effacer la fenêtre
    fenetre.blit(battle_bg, (0, 0))

    # Positionner le premier Pokémon
    x1 = (largeur_fenetre - pokemon_image1.get_width()) / 2 - 400
    y1 = (hauteur_fenetre - pokemon_image1.get_height()) // 2 + 80
    fenetre.blit(pokemon_image1, (x1, y1))

    # Positionner le deuxième Pokémon
    x2 = (largeur_fenetre - pokemon_image2.get_width()) / 2 + 400
    y2 = (hauteur_fenetre - pokemon_image2.get_height()) // 2 + 80
    fenetre.blit(pokemon_image2, (x2, y2))

    # Positionner les barres de vie
    fenetre.blit(barre_vie_pokemon1, (x1, y1 - 10))
    fenetre.blit(barre_vie_pokemon2, (x2, y2 - 10))
    
        # Récupérer le nom du Pokémon
    nom_pokemon = data["Niveau1"][1]["nom"]

    # Créer une police
    police = pygame.font.Font("freesansbold.ttf", 20)

    # Créer un texte
    texte_nom = police.render(nom_pokemon, True, BLANC)

    # Calculer la taille du texte
    taille_texte = texte_nom.get_size()

    # Positionner le texte
    x = x1 + (barre_vie_pokemon1.get_width() - taille_texte[0]) / 2
    y = y1 - 10 - taille_texte[1]
    
    x = x2 + (barre_vie_pokemon1.get_width() - taille_texte[0]) / 2
    y = y2 - 10 - taille_texte[1]
    
    # Afficher le texte
    fenetre.blit(texte_nom, (x, y))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
