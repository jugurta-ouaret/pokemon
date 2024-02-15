import pygame
import json
from Combat.game_logic import *

moves_json="../pokemon/dict_Json/moves.json"
pokemon_json = "../pokemon/dict_Json/pokemon.json"

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
            
        # Taille du sprite    
        self.size = 150
            
        # Charge l'image du pokemon de droite lors du choix de pokemon
        self.set_sprite('droite')
    
    
    def set_sprite(self, direction):
        # Le path des sprites / importation des sprites
        self.sprite = pygame.image.load(f'../Pokemon/Assets/images/sprites/{self.name}/{direction}.png')
        # Redimensionne le sprite
        self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))

     
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
       


    # Dessine le sprite du pokémon
    def draw(self, alpha = 255):
        sprite = self.sprite.copy()
        transparence = (255, 255, 255, alpha)
        sprite.fill(transparence, None, pygame.BLEND_RGBA_MULT)
        game.blit(sprite, (self.x, self.y))
     
     

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
        

         
# Charger les données du dictionnaire
with open("../pokemon/dict_Json/pokemon.json", "r") as f:
    pokemon_data = json.load(f)

# Extraire les informations sur les Pokémon
pokemon_noms = [pokemon['nom'] for pokemon in pokemon_data['Niveau1']]
pokemon_moves=[pokemon['moves'] for  pokemon in pokemon_data['Niveau1']]

pokemons_list=[]
# Instancier les pokemons
for i in  range (len(pokemon_noms)):
    pokemons_list.append(Pokemon(pokemon_noms[i],10,0,0))

for i in  range (len(pokemon_noms)):
    pokemons_list[i].set_moves(pokemon_moves[i]) 
    
