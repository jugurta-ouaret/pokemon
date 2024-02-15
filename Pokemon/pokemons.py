import pygame
import json
from Menu import menu
from Combat.combat import run_combat


# Initialisation de Pygame
pygame.init()

#Fonction pour afficher le profil du Pokémon
def afficher_profil_pokemon(nom):
    pygame.init()
    
    # Dimensions de la fenêtre
    WIDTH = 1280
    HEIGHT = 720

    # Couleurs
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    BLACK=(0,0,0)

    # Création de la fenêtre
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"{nom}")

    # Fond de la fenêtre
    background = pygame.Surface(screen.get_size())
    background.fill(WHITE)
    screen.blit(background, (0, 0))

    # Charger les données du dictionnaire
    with open("../pokemon/dict_Json/pokemon.json", "r") as f:
        pokemon_data = json.load(f)

    # Extraire les informations sur les Pokémon
    pokemon_images = [pokemon['image']for pokemon in pokemon_data['Niveau1']]
    pokemon_noms = [pokemon['nom'] for pokemon in pokemon_data['Niveau1']]
    pokemon_types = [pokemon['type'] for pokemon in pokemon_data['Niveau1']]
    pokemon_PVs = [pokemon['PV'] for pokemon in pokemon_data['Niveau1']]
    pokemon_attaques = [pokemon['Attaque'] for pokemon in pokemon_data['Niveau1']]
    pokemon_defenses = [pokemon['Defense'] for pokemon in pokemon_data['Niveau1']]
    pokemon_vitesses = [pokemon['Vitesse'] for pokemon in pokemon_data['Niveau1']]
    pokemon_attaques_sups = [pokemon['AttaqueSp'] for pokemon in pokemon_data['Niveau1']]
    #récupérer l'index  de nom de  pokemon
    index=pokemon_noms.index(nom)

    #récupérer le reste des infos 
    type_pokemon = pokemon_types[index]
    PV=pokemon_PVs[index]
    attaque=pokemon_attaques[index]
    defense=pokemon_defenses[index]
    vitesse=pokemon_vitesses[index]
    attaque_sup=pokemon_attaques_sups[index]
    image_path=pokemon_images[index]
    
    # Titre "Profil"
    font_titre = pygame.font.Font(None, 70)
    texte_titre = font_titre.render(f"{nom}", True, (0, 0, 0))
    titre_rect = texte_titre.get_rect(center=(WIDTH // 2, 100))
    screen.blit(texte_titre, titre_rect)

    # Afficher l'image du Pokémon
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (300, 300))
    image_rect = image.get_rect(center=(WIDTH // 2, 250))
    screen.blit(image, image_rect)

    # Afficher les informations du Pokémon
    font = pygame.font.Font(None, 30)
    y_position = 450

    
    texte_type = font.render(f"Type: {type_pokemon}", True, BLACK)
    texte_PV = font.render(f"PV: {PV}", True, BLACK)
    texte_attaque = font.render(f"Attaque: {attaque}", True, BLACK)
    texte_defense = font.render(f"Défense: {defense}", True, BLACK)
    texte_vitesse = font.render(f"Vitesse: {vitesse}", True, BLACK)
    texte_attaque_sup = font.render(f"Attaque Spéciale: {attaque_sup}", True, BLACK)

    for texte in [texte_type, texte_PV, texte_attaque, texte_defense, texte_vitesse, texte_attaque_sup]:
        texte_rect = texte.get_rect(center=(WIDTH // 2, y_position))
        screen.blit(texte, texte_rect)
        y_position += 30

    pygame.display.flip()

   
    # Bouton "Choisir"
    choisir_button_rect = pygame.Rect(WIDTH - 160, HEIGHT - 60, 120, 40)
    pygame.draw.rect(screen, (0, 128, 255), choisir_button_rect)
    font_choisir = pygame.font.Font(None, 28)
    texte_choisir = font_choisir.render("Choisir", True, WHITE)
    choisir_rect = texte_choisir.get_rect(center=choisir_button_rect.center)
    screen.blit(texte_choisir, choisir_rect)

    # Bouton "Retour"
    retour_button_rect = pygame.Rect(40, HEIGHT - 50, 120, 40)
    pygame.draw.rect(screen, (255, 0, 0), retour_button_rect)
    font_retour = pygame.font.Font(None, 28)
    texte_retour = font_retour.render("Retour", True, WHITE)
    retour_rect = texte_retour.get_rect(center=retour_button_rect.center)
    screen.blit(texte_retour, retour_rect)


    pygame.display.flip()

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Vérifier si le clic est sur le bouton "Choisir"
                if choisir_button_rect.collidepoint(event.pos):
                    run_combat(index)


                # Vérifier si le clic est sur le bouton "Retour"
                elif retour_button_rect.collidepoint(event.pos):
                    afficher_liste_pokemons()
                   






#fonction de l'affichage de pokémone 
def afficher_liste_pokemons():
    
    # Dimensions de la fenêtre
    WIDTH = 1280
    HEIGHT = 720

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
    pokemon_list = [pokemon['image']for pokemon in pokemon_data['Niveau1']]

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


