import pygame
from pygame.locals import *
from Combat.ui import *
import random
import json
import time
import math 

pygame.init()

# Path to the json files
moves_json = "../pokemon/dict_Json/moves.json"
pokemon_json = "../pokemon/dict_Json/pokemon.json"

# Charge le background du combat
battle_bg = pygame.image.load("../pokemon/Assets/images/battle_bg.png")


class Move():
    def __init__(self, name):
        # Ouvrir le fichier JSON
        with open(moves_json, 'r') as file:
            move_data = json.load(file)
            for i in move_data['moves']:
                if i['name'] == name:
                    self.json = i
                    break
        # Définir les attributs
        self.name = self.json['name']
        self.power = self.json['power']
        self.type = self.json['type']
    

    def effectue_attaque(self, autre, move):
        affiche_message(f"{self.name} utilise {move.name}")
        
        #pause de 2 secondes
        time.sleep(2)
        
        # Calcul des dégâts
        degats = (2 * self.niveau + 10) / 250 * (self.Attaque / autre.Defense) * move.power
        if move.type in autre.types:
            degats *= 2
            affiche_message("C'est super efficace !")
            
        random_num = random.randint(1, 10000)
        if random_num < 625:
            degats *= 2
            affiche_message("Coup critique !")
            
        degats = math.floor(degats)
        
        autre.subir_degats(degats)
        
    def subir_degats(self, degats):
        self.PV -= degats
        if self.PV < 0:
            self.PV = 0
        affiche_message(f"{self.name} a subi {degats} dégâts")
    
     
    # Def de la méthode pour se soigner   
    def use_potion(self):
        # verifier si le joueur a des potions restantes
        if self.num_potions > 0:
            # ajout de 10 PV mais pas plus que le MAX_PV
            self.PV += 10
            if self.PV > self.MAX_PV:
                self.PV = self.MAX_PV
            # -1 sur 3 utilisation de potion
            self.num_potions -= 1

        
    
     
    # Def de la méthode pour recup les attaque des pokemons
    def set_moves(self, moves_data):
        # moves_data est le nom du fichier JSON qui contient les données des attaques
        
        # self.moves est une liste qui contiendra les attaques du pokémon
        self.moves = []
        
        # importe les données des attaques depuis le fichier JSON
        with open(moves_json, 'r') as file:
           moves_data_all = json.load(file)
    
        # parcour les noms des attaques fournis
        for move_name in moves_data:
            
            # rechercher l'attaque dans les données de toutes les attaques
            for move_data in moves_data_all['moves']:
                
                # si le nom de l'attaque correspond à celui fourni
                if move_data['name'] == move_name:
                    # ajouter l'attaque à la liste des attaques du Pokémon
                    move = Move(move_name)
                    self.moves.append(move)
                    break  # sortir de la boucle interne
                
        # si le Pokémon a plus de 4 attaques, en choisir aléatoirement 4
        if len(self.moves) > 4:
            self.moves = random.sample(self.moves, 4)
            
    
    
    # Dessine la barre de PV
    def draw_pv(self):
        barre_scale = 300 // self.MAX_PV
        for i in range(self.MAX_PV):
            barre = (self.PV_x + barre_scale * i, self.PV_y, barre_scale, 20)
            pygame.draw.rect(game, rouge, barre)

        for i in range(self.PV):
            barre = (self.PV_x + barre_scale * i, self.PV_y, barre_scale, 20)
            pygame.draw.rect(game, vert, barre)

        # dessiner le texte des PV    
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        text = font.render(f"PV : {self.PV} / {self.MAX_PV}", True, noir)
        text_rect = text.get_rect()
        text_rect.x = self.PV_x
        text_rect.y = self.PV_y + 30
        game.blit(text, text_rect)
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)