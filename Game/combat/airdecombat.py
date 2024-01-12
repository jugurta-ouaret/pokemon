import pygame
import sys


pygame.init()


largeur, hauteur = 1280, 720
taille_fenetre = (largeur, hauteur)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Fenêtre Pygame")


image_fond = pygame.image.load("../pokemon/Assets/images/Fond.png")  
image_fond = pygame.transform.scale(image_fond, (largeur, hauteur))  


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    fenetre.blit(image_fond, (0, 0))

   
    pygame.display.flip()
