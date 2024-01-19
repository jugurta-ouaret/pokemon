# main.py
import pygame
import sys
from Game.Menu import menu

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

menu(SCREEN)