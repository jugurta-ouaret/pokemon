import pygame
from pygame.locals import *
from game_logic import *


# Def methodes pour afficher les textes
def affiche_message(message):
    #Dessin du rectangle box blanc et bordure noir
    pygame.draw.rect(game, blanc, (20, 556, Largeur - 30, 160), 3)
    
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    text = font.render(message, True, noir)
    text_rect = text.get_rect()
    text_rect.x = 50
    text_rect.y = 610
    game.blit(text, text_rect)
    
    pygame.display.update()