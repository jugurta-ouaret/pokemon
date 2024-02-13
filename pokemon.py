import pygame
from pygame.locals import *
from game_logic import *


# Instancier les pokemons
niveau = 10
bullbizarre = Pokemon("Bullbizarre", niveau, 25, 100)
salameche = Pokemon("Salameche", niveau, 175, 100)
carapuce = Pokemon("Carapuce", niveau, 325, 100)
galekid = Pokemon("Galekid", niveau, 480, 100)
abra = Pokemon("Abra", niveau, 650, 100)


#Initialisation des attaques 
moves_bullbizarre = ["fouet lianes", "tranche", "laser glace", "seisme"]
bullbizarre.set_moves(moves_bullbizarre)

moves_salameche = ["flammeche", "griffe", "tranche", "feu d'enfer"]
salameche.set_moves(moves_salameche)

moves_carapuce = ["pistolet a o", "ecume", "hydrocanon", "laser glace"]
carapuce.set_moves(moves_carapuce)

moves_galekid = ["charge", "griffe", "tranche", "morsure"]
galekid.set_moves(moves_galekid)

moves_abra = ["psyko", "choc mental"]
abra.set_moves(moves_abra)

pokemons = [salameche, carapuce, bullbizarre, abra, galekid]