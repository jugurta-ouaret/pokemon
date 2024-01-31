import pygame
import json 

# Initialisation de Pygame
pygame.init()
# Dimensions de la fenêtre
WIDTH = 1300
HEIGHT = 780

# Couleurs
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Button Effect")

#changer le fond de la console 
background = pygame.image.load ("../pokemon/Assets/images/ListePokémone.png")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))


#récupérer les données de dictionnaire 
with open("../pokemon/dict_Json/pokemon.json", "r") as f:
    pokemon_data=json.load(f)
    

# Créer une liste de tous les Pokémon de niveau 1
pokemon_list = [pokemon['image'][1]['Gauche'] for pokemon in pokemon_data['Niveau1']]

images=[]
for image in pokemon_list:
    image_load=pygame.transform.scale((pygame.image.load(image)),(150,150))
    images.append(image_load)




# Rafraîchir l'écran
pygame.display.flip()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Affichage de l'arrière plan 
    screen.blit(background,(0,0))

    # Dessiner les images sur l'écran
    x, y = 30, 150
    for i, image in enumerate(images):
        screen.blit(image, (x, y))
        x += image.get_width()
        if i % 8 == 7:  # Passer à la ligne suivante après avoir dessiné 4 images
            y += image.get_height()
            x = 30
    
    # Rafraîchissement de la fenêtre
    pygame.display.flip()

# Quitter Pygame
pygame.quit()



