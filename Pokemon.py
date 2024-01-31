import pygame
import json


# Initialiser Pygame
pygame.init()

# Charger les données du dictionnaire
with open("../pokemon/dict_Json/pokemon.json", "r") as f:
    pokemon_data = json.load(f)

# Extraire les informations sur les Pokémon
pokemon_images = [pokemon['image'][1]['Gauche'] for pokemon in pokemon_data['Niveau1']]
pokemon_noms = [pokemon['nom'] for pokemon in pokemon_data['Niveau1']]
pokemon_types = [pokemon['type'] for pokemon in pokemon_data['Niveau1']]
pokemon_PVs = [pokemon['PV'] for pokemon in pokemon_data['Niveau1']]
pokemon_attaques = [pokemon['Attaque'] for pokemon in pokemon_data['Niveau1']]
pokemon_defenses = [pokemon['Defense'] for pokemon in pokemon_data['Niveau1']]
pokemon_vitesses = [pokemon['Vitesse'] for pokemon in pokemon_data['Niveau1']]
pokemon_attaques_sups = [pokemon['AttaqueSp'] for pokemon in pokemon_data['Niveau1']]

# Fonction pour afficher le profil du Pokémon
def afficher_profil_pokemon(nom):
    pygame.init()
    
    # Dimensions de la fenêtre
    WIDTH = 700
    HEIGHT = 800

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
    pokemon_images = [pokemon['image'][1]['Gauche'] for pokemon in pokemon_data['Niveau1']]
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
                    print("Bouton Choisir cliqué!")

                # Vérifier si le clic est sur le bouton "Retour"
                elif retour_button_rect.collidepoint(event.pos):
                    running = False
                   


    pygame.quit()

