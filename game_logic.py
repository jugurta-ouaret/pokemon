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