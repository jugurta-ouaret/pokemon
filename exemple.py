import json 
import pygame

pygame.init()

# Création de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokedex")

#récupérer les données de dictionnaire 
with open("../pokemon/dict_Json/pokedex.json", "r") as f:
    data=json.load(f)
    
    # Récupérer le nom du pokemon1 de niveau1
    image1 = data["pokemon1"][1]["Niveau1"]["image"]
    image2 = data["pokemon1"][1]["Niveau2"]["image"]
    image3 = data["pokemon1"][1]["Niveau3"]["image"]
    image4 = data["pokemon1"][1]["Niveau4"]["image"]


# Chargement des images
image_1 = pygame.image.load(image1)
image_1 = pygame.transform.scale(image_1, (100, 100))


image_2 = pygame.image.load(image2)
image_2 = pygame.transform.scale(image_2, (100, 100))

image_3 = pygame.image.load(image3)
image_3 = pygame.transform.scale(image_3, (100, 100))

image_4 = pygame.image.load(image4)
image_4 = pygame.transform.scale(image_4, (100, 100))

# Liste des images
images = [image_1, image_2 , image_3 , image_4] 

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Affichage des images
    screen.fill((255, 255, 255))
    x = 50
    y = 50
    spacing = 20
    for image in images:
        screen.blit(image, (x, y))
        x += image.get_width() + spacing

    pygame.display.flip()

pygame.quit()