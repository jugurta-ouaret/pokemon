import json 
import pygame

pygame.init()

# Création de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokedex")

#récupérer les données de dictionnaire 
with open("../pokemon/dict_Json/pokemon.json", "r") as f:
    data=json.load(f)
    
# Boucle pour récupérer les images de chaque ligne de niveau "1"
images=[]
for level in data.values(): 
   for pokemon in level[0]["Niveau"]: 
      for image_url in pokemon["1"]: 
        image=image_url["image"]
        image1 = pygame.image.load(image)
        image_1 = pygame.transform.scale(image1, (100, 100))
        # Liste des images
        images.append(image_1)


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


