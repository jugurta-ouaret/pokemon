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
            
        #Si on clique sur un bouton
        elif game_status == "tour joueur":
            if fight_button.collidepoint(mouse_click):
                game_status = "joueur attaque"
                
            if potion_button.collidepoint(mouse_click):
               if player_pokemon.use_potion() == 0:
                    display_text = "Vous n'avez plus de potions"
                    affiche_message(display_text)
                    time.sleep(2)
                    game_status = "joueur attaque"
               else:
                   player_pokemon.use_potion()
                   display_text = f"{player_pokemon.name} a utilisé une potion"
                   affiche_message(display_text)                    
            
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
      
       
    if game_status == "precombat":
        game.fill(blanc)
        player_pokemon.draw()
        pygame.display.update()
        
        moves_names = [move.name for move in player_pokemon.moves]
        
        player_pokemon.set_moves(moves_names)
        enemy_pokemon.set_moves(moves_names)
        
        #Positionnement des pokemons
        player_pokemon.x = 80
        player_pokemon.y = 200
        
        enemy_pokemon.x = 980
        enemy_pokemon.y = 200
        
        #Redimensionnement des sprites
        player_pokemon.size = 300
        enemy_pokemon.size = 300
        player_pokemon.set_sprite('gauche')
        enemy_pokemon.set_sprite('droite')
        
        game_status = "debut combat"
     
     #Début du combat   
    if game_status == "debut combat":
        #L'ennemi envoie son pokemon
        alpha = 0
        while alpha < 255:
            game.blit(battle_bg, (0, 0))
            enemy_pokemon.draw(alpha)
            display_text = f"L'ennemi a envoyé {enemy_pokemon.name} !"
            affiche_message(display_text)
            alpha += 6
            
            pygame.display.update()
        
        time.sleep(1.5)
        
        #Le joueur envoie son pokemon
        alpha = 0
        while alpha < 255:
            game.blit(battle_bg, (0, 0))
            player_pokemon.draw(alpha)
            display_text = f"À l'attaque {player_pokemon.name} !"
            affiche_message(display_text)
            alpha += 6
            
            pygame.display.update()
        
        player_pokemon.draw_pv()
        enemy_pokemon.draw_pv()
        enemy_pokemon.draw()
        
        
        if enemy_pokemon.Vitesse > player_pokemon.Vitesse:
            game_status = "tour ennemi"
        else:
            game_status = "tour joueur"
            
        pygame.display.update()
        
        time.sleep(2)
        
    if game_status == "tour joueur":
        game.blit(battle_bg, (0, 0))
        player_pokemon.draw()
        enemy_pokemon.draw()
        player_pokemon.draw_pv()
        enemy_pokemon.draw_pv()
        
        fight_button = create_button(200, 50, 540, 600, 640, 625, "Attaquer")
        potion_button = create_button(200, 50, 540, 660, 640, 685, f"Potion({player_pokemon.num_potions})")
        # leave_button = create_button(200, 50, 540, 720, 640, 745, "Fuir")
           
        pygame.draw.rect(game, noir, (20, 556, Largeur - 30, 160), 3)
        pygame.display.update()
        
    if game_status == "joueur attaque":
        print("Entering joueur attaque condition") # Vérifier si on est bien dans la conditioon d'attaque
        game.blit(battle_bg, (0, 0))
        player_pokemon.draw()
        enemy_pokemon.draw()
        player_pokemon.draw_pv()
        enemy_pokemon.draw_pv()
        
        #Affichage des attaques
        move_buttons = []
        for i in range(len(player_pokemon.moves)):
            move = player_pokemon.moves[i]
            button_width = 520
            button_height = 78
            left = 25 + i % 2 * button_width
            top = 560 + i // 2 * button_height
            text_center_x = left + 250
            text_center_y = top + 35

            button = create_button(button_width, button_height, left, top, text_center_x, text_center_y, move.name.capitalize())
            move_buttons.append(button)

        pygame.draw.rect(game, noir, (20, 556, Largeur - 30, 160), 3)
        pygame.display.update()
         
pygame.quit()