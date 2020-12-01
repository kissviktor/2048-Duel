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
text_font = pygame.font.Font('PressStart2P.ttf', 20)

# háttérszín
hatter = pygame.Color(130, 230, 140)

menu_clock = pygame.time.Clock()

click = False


def instructions_1():

    click = False

    while True:

        window.fill(hatter)


        label_main_menu = menu_font.render("Instructions", True, (0, 0, 0))  # szöveg
        label_main_menu_rect = label_main_menu.get_rect(
            center=(int(600 / 2), int(800 / 12)))               # szövegdoboz az igazításhoz
        window.blit(label_main_menu, label_main_menu_rect)

        #   Első tipp
        inst_1_1 = "1, Your main goal is to"
        inst_1_2 = "earn more points, than"
        inst_1_3 = "your opponent."

        label_text1_1 = text_font.render(inst_1_1, True, (0, 0, 0))
        label_text1_1_rect = label_text1_1.get_rect(
            center=(int(600 / 2), 200))
        window.blit(label_text1_1, label_text1_1_rect)

        label_text1_2 = text_font.render(inst_1_2, True, (0, 0, 0))
        label_text1_2_rect = label_text1_2.get_rect(
            center=(int(600 / 2), 250))
        window.blit(label_text1_2, label_text1_2_rect)

        label_text1_3 = text_font.render(inst_1_3, True, (0, 0, 0))
        label_text1_3_rect = label_text1_3.get_rect(
            center=(int(600 / 2), 300))
        window.blit(label_text1_3, label_text1_3_rect)

        #   Második tipp
        inst_2_1 = "2, You get points by "
        inst_2_2 = "merging the tiles together. "

        label_text2_1 = text_font.render(inst_2_1, True, (0, 0, 0))
        label_text2_1_rect = label_text2_1.get_rect(
            center=(int(600 / 2), 400))
        window.blit(label_text2_1, label_text2_1_rect)

        label_text2_2 = text_font.render(inst_2_2, True, (0, 0, 0))
        label_text2_2_rect = label_text2_2.get_rect(
            center=(int(600 / 2), 450))
        window.blit(label_text2_2, label_text2_2_rect)



        mouse_x, mouse_y = pygame.mouse.get_pos()


        button_menu = pygame.Rect(50, 600, 150, 100)
        label_button_menu = button_font.render('Menu', 1, (0, 0, 0))
        label_button_menu_rect = label_button_menu.get_rect(center=(125, 650))

        pygame.draw.rect(window, (120, 30, 70), button_menu)
        window.blit(label_button_menu, label_button_menu_rect)


        button_next = pygame.Rect(400, 600, 150, 100)
        label_button_next = button_font.render('Next', 1, (0, 0, 0))
        label_button_next_rect = label_button_next.get_rect(center=(475, 650))

        pygame.draw.rect(window, (120, 30, 70), button_next)
        window.blit(label_button_next, label_button_next_rect)


        if button_menu.collidepoint((mouse_x, mouse_y)):
            button_menu = pygame.Rect(40, 590, 170, 120)
            pygame.draw.rect(window, (160, 70, 20), button_menu)
            window.blit(label_button_menu, label_button_menu_rect)
            if click:
                from Main_Menu import main_menu
                main_menu()


        if button_next.collidepoint((mouse_x, mouse_y)):
            button_next = pygame.Rect(390, 590, 170, 120)
            pygame.draw.rect(window, (160, 70, 20), button_next)
            window.blit(label_button_next, label_button_next_rect)
            if click:

                from Instructions_2 import instructions_2
                instructions_2()



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


instructions_1()
