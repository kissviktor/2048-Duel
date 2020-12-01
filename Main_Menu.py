import math
import os
import pygame
import pygame.gfxdraw
import sys
import time
from pygame.locals import *


# inicializálás
pygame.init()

# ablak létrehozás:
# ablak igazítás középre
os.environ['SDL_VIDEO_CENTERED'] = '1'
# ablak megjelenítés
window = pygame.display.set_mode((600, 800))
pygame.display.set_caption('2048 Duel Arena')

# betűtípus
menu_font = pygame.font.Font('PressStart2P.ttf', 50, bold=True)
button_font = pygame.font.Font('PressStart2P.ttf', 24, bold=True)

# háttérszín
hatter = pygame.Color(130, 230, 140)

menu_clock = pygame.time.Clock()

click = False


def main_menu():

    click = False

    while True:

        window.fill(hatter)

        label_main_menu = menu_font.render("Main Menu", True, (0, 0, 0))  # szöveg
        label_main_menu_rect = label_main_menu.get_rect(
            center=(int(600 / 2), int(800 / 12)))  # szövegdoboz az igazításhoz
        window.blit(label_main_menu, label_main_menu_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_Instructions = pygame.Rect(150, 150, 300, 100)
        label_button_Instructions = button_font.render('Instructions', 1, (0, 0, 0))
        label_button_Instructions_rect = label_button_Instructions.get_rect(center=(300, 200))


        button_pvp = pygame.Rect(150, 300, 300, 100)
        label_button_pvp = button_font.render('Play', 1, (0, 0, 0))
        label_button_pvp_rect = label_button_pvp.get_rect(center=(300, 350))


        button_highscore = pygame.Rect(150, 450, 300, 100)
        label_button_highscore = button_font.render('Highscores', 1, (0, 0, 0))
        label_button_highscore_rect = label_button_highscore.get_rect(center=(300, 500))

        button_exit = pygame.Rect(150, 600, 300, 100)
        label_button_exit = button_font.render('Exit', 1, (0, 0, 0))
        label_button_exit_rect = label_button_exit.get_rect(center=(300, 650))


        pygame.draw.rect(window, (120, 30, 70), button_Instructions)
        window.blit(label_button_Instructions, label_button_Instructions_rect)

        pygame.draw.rect(window, (120, 30, 70), button_pvp)
        window.blit(label_button_pvp, label_button_pvp_rect)

        pygame.draw.rect(window, (120, 30, 70), button_highscore)
        window.blit(label_button_highscore, label_button_highscore_rect)

        pygame.draw.rect(window, (120, 30, 70), button_exit)
        window.blit(label_button_exit, label_button_exit_rect)

        if button_Instructions.collidepoint((mouse_x, mouse_y)):
            button_Instructions = pygame.Rect(140, 140, 320, 120)
            pygame.draw.rect(window, (160, 70, 20), button_Instructions)
            window.blit(label_button_Instructions, label_button_Instructions_rect)
            if click:
                from Instructions_1 import instructions_1
                instructions_1()


        if button_pvp.collidepoint((mouse_x, mouse_y)):
            button_pvp = pygame.Rect(140, 290, 320, 120)
            pygame.draw.rect(window, (160, 70, 20), button_pvp)
            window.blit(label_button_pvp, label_button_pvp_rect)
            if click:

                from Coop_Names_Input import name_input
                name_input()

        if button_highscore.collidepoint((mouse_x, mouse_y)):
            button_highscore = pygame.Rect(140, 440, 320, 120)
            pygame.draw.rect(window, (160, 70, 20), button_highscore)
            window.blit(label_button_highscore, label_button_highscore_rect)
            if click:

                from Highscores import highscores
                highscores()

        if button_exit.collidepoint((mouse_x, mouse_y)):
            button_exit = pygame.Rect(140, 590, 320, 120)
            pygame.draw.rect(window, (160, 70, 20), button_exit)
            window.blit(label_button_exit, label_button_exit_rect)
            if click:
                pygame.quit()
                sys.exit()



        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        menu_clock.tick(60)  # 60 FPS


main_menu()
