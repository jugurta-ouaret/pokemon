import pygame
from game_logic import *
from pokemon import *
from ui import *
import time 
import math 
import random

pygame.init()

player_pokemon = None
enemy_pokemon = None

clock = pygame.time.Clock()
FPS = 60

game_status = "choix pokemon"
while game_status != "quit":
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = "quit"
         
        #Si on clique sur un pokemon
        if event.type == MOUSEBUTTONDOWN:
            
            #Si on clique sur un pokemon
                mouse_click = event.pos

                #Si on est en train de choisir un pokemon
                if game_status == "choix pokemon":
                    chosen_pokemon = None # variable pour stocker le pokemon choisi
                    for i in range(len(pokemons)):
                        if pokemons[i].get_rect().collidepoint(mouse_click):
                            chosen_pokemon = pokemons[i] # assigner le pokemon choisi à la variable
                            break # sortir de la boucle
                    if chosen_pokemon is not None: # si un pokemon a été choisi
                        player_pokemon = chosen_pokemon # assigner le pokemon choisi au joueur
                        pokemons.remove(chosen_pokemon) # supprimer le pokemon choisi de la liste
                        enemy_pokemon = random.choice(pokemons) # choisir un pokemon ennemi au hasard
                        
                        player_pokemon.PV_x = 150
                        player_pokemon.PV_y = 80
                        player_pokemon.PV_width = 350
                        player_pokemon.PV_height = 100
                        
                        enemy_pokemon.PV_x = 950
                        enemy_pokemon.PV_y = 80
                        enemy_pokemon.PV_width = 350
                        enemy_pokemon.PV_height = 100
                        
                        game_status = "precombat"
                        
        if game_status == "choix pokemon":
            
            game.fill(blanc)
            
            #Affichage des pokemons
            for i in range(len(pokemons)):
                pokemons[i].draw()
            
            #Affichage des noms des pokemons
            font = pygame.font.Font(None, 50)
            text = font.render("Choisissez votre Pokemon", True, noir)
            game.blit(text, (Largeur//2 - text.get_width()//2, 40))
            
            
            mouse_cursor = pygame.mouse.get_pos()
            for pokemon in pokemons:
                if pokemon.get_rect().collidepoint(mouse_cursor):
                    pygame.draw.rect(game, noir, pokemon.get_rect(), 3)
                    
            pygame.display.update()

pygame.quit()