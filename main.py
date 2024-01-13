import pygame, sys
from Game.Class.bouton import Bouton


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("../pokemon/Assets/menu/bg.png")

def get_font(size): 
    return pygame.font.Font("../pokemon/Assets/menu/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("CHOIX DU POKEMON", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_RETOUR = Bouton(image=None, pos=(640, 460), 
                            text_input="RETOUR", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_RETOUR.changeColor(PLAY_MOUSE_POS)
        PLAY_RETOUR.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_RETOUR.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def REPRENDRE():
    while True:
        REPRENDRE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        REPRENDRE_TEXT = get_font(45).render("POKEDEX!!!!!!", True, "Black")
        REPRENDRE_RECT = REPRENDRE_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(REPRENDRE_TEXT, REPRENDRE_RECT)

        REPRENDRE_RETOUR = Bouton(image=None, pos=(640, 460), 
                            text_input="RETOUR", font=get_font(75), base_color="Black", hovering_color="Green")

        REPRENDRE_RETOUR.changeColor(REPRENDRE_MOUSE_POS)
        REPRENDRE_RETOUR.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if REPRENDRE_RETOUR.checkForInput(REPRENDRE_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("", True, "#f9cc36")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_Bouton = Bouton(image=pygame.image.load("../pokemon/Assets/menu/Play_Rect.png"), pos=(640, 250), 
                            text_input="NOUVELLE PARTIE", font=get_font(60), base_color="White", hovering_color="#c047c0")
        REPRENDRE_Bouton = Bouton(image=pygame.image.load("../pokemon/Assets/menu/Reprendre_Rect.png"), pos=(640, 400), 
                            text_input="REPRENDRE", font=get_font(60), base_color="White", hovering_color="#c047c0")
        QUIT_Bouton = Bouton(image=pygame.image.load("../pokemon/Assets/menu/Quitter_Rect.png"), pos=(640, 550), 
                            text_input="QUITTER", font=get_font(60), base_color="White", hovering_color="#c047c0")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for bouton in [PLAY_Bouton, REPRENDRE_Bouton, QUIT_Bouton]:
            bouton.changeColor(MENU_MOUSE_POS)
            bouton.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_Bouton.checkForInput(MENU_MOUSE_POS):
                    play()
                if REPRENDRE_Bouton.checkForInput(MENU_MOUSE_POS):
                    REPRENDRE()
                if QUIT_Bouton.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()