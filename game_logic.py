import pygame
from pygame.locals import *
import random
import json

pygame.init()

#Taille de la fenêtre
Hauteur = 720
Largeur = 1280
Taille = (Largeur, Hauteur)
game = pygame.display.set_mode(Taille)
pygame.display.set_caption("PokeWorld - Battle by J.A.R")

#Les couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
gold = (255, 215, 0)
vert = (0, 255, 0)
rouge = (255, 0, 0)
gris = (128, 128, 128)

# Path to the json files
moves_json = "json/moves.json"
pokemon_json = "json/pokemon.json"

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
        
# Classe Pokemon
class Pokemon(pygame.sprite.Sprite):
    
    # Def des attributs
    def __init__(self, name, niveau, x, y):
        with open(pokemon_json, "r") as file:
            data = json.load(file)
        
        # Accédez au premier élément de la liste "Niveau1"
        pokemon_data = data["Niveau1"][0]

        # Trouvez le Pokémon spécifique par son nom dans la liste
        for pokemon in data["Niveau1"]:
            if pokemon["nom"] == name:
                pokemon_data = pokemon
                break

        self.json = pokemon_data
        self.name = name
        self.niveau = niveau
        self.x = x
        self.y = y
        self.num_potions = 3
        
        self.type = self.json['type']
        self.PV = self.json['PV'] + self.niveau
        self.MAX_PV = self.json['PV'] + self.niveau
        self.Attaque = self.json['Attaque']
        self.AttaqueSp = self.json['AttaqueSp']
        self.Defense = self.json['Defense']
        self.Vitesse = self.json['Vitesse']
        
        self.types = []
        for i in range(len(self.type)):
            type = self.json['type'][i]
            self.types.append(type)
         
        #    
        self.size = 150
            
        # Charge l'image du pokemon de droite lors du choix de pokemon
        self.set_sprite('droite')