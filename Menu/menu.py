import pygame, sys
from Menu.bouton import Bouton
from Pokemon.pokemons import afficher_liste_pokemons

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("../pokemon/Assets/images/menu/bg.png")

def get_font(size): 
    return pygame.font.Font("../pokemon/Assets/images/menu/font.ttf", size)

def JOUER():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
         
        afficher_liste_pokemons()

        PLAY_RETOUR = Bouton(image=None, pos=(100, 650), 
                            text_input="RETOUR", font=get_font(40), base_color="Black", hovering_color="#c047c0")

        PLAY_RETOUR.changeColor(PLAY_MOUSE_POS)
        PLAY_RETOUR.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_RETOUR.checkForInput(PLAY_MOUSE_POS):
                    menu()

        pygame.display.update()
    
def REPRENDRE():
    while True:
        REPRENDRE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        REPRENDRE_TEXT = get_font(45).render("POKEDEX!!!!!!", True, "Black")
        REPRENDRE_RECT = REPRENDRE_TEXT.get_rect(center=(640, 70))
        SCREEN.blit(REPRENDRE_TEXT, REPRENDRE_RECT)

        REPRENDRE_RETOUR = Bouton(image=None, pos=(100, 650), 
                            text_input="RETOUR", font=get_font(40), base_color="Black", hovering_color="#c047c0")

        REPRENDRE_RETOUR.changeColor(REPRENDRE_MOUSE_POS)
        REPRENDRE_RETOUR.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if REPRENDRE_RETOUR.checkForInput(REPRENDRE_MOUSE_POS):
                    menu()
                    
        pygame.display.update()

def menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_Bouton = Bouton(image=pygame.image.load("../pokemon/Assets/images/menu/Play_Rect.png"), pos=(640, 250), 
                            text_input="NOUVELLE PARTIE", font=get_font(60), base_color="White", hovering_color="#c047c0")
        REPRENDRE_Bouton = Bouton(image=pygame.image.load("../pokemon/Assets/images/menu/Reprendre_Rect.png"), pos=(640, 400), 
                            text_input="REPRENDRE", font=get_font(60), base_color="White", hovering_color="#c047c0")
        QUIT_Bouton = Bouton(image=pygame.image.load("../pokemon/Assets/images/menu/Quitter_Rect.png"), pos=(640, 550), 
                            text_input="QUITTER", font=get_font(60), base_color="White", hovering_color="#c047c0")

        for bouton in [PLAY_Bouton, REPRENDRE_Bouton, QUIT_Bouton]:
            bouton.changeColor(MENU_MOUSE_POS)
            bouton.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_Bouton.checkForInput(MENU_MOUSE_POS):
                    JOUER()
                if REPRENDRE_Bouton.checkForInput(MENU_MOUSE_POS):
                    REPRENDRE()
                if QUIT_Bouton.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
menu()