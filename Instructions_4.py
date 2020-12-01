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


def instructions_4():

    click = False

    while True:

        window.fill(hatter)

        label_main_menu = menu_font.render("Instructions", True, (0, 0, 0))  # szöveg
        label_main_menu_rect = label_main_menu.get_rect(
            center=(int(600 / 2), int(800 / 12)))  # szövegdoboz az igazításhoz
        window.blit(label_main_menu, label_main_menu_rect)

        #   TIPPEK (start)

        #   Hatodik tipp
        inst_6_1 = "6, You will earn shots by"
        inst_6_2 = "collecting points and via"
        inst_6_3 = "shots you can destroy an "
        inst_6_4 = "enemy Tile."
        inst_6_5 = "Use it wisely!"

        label_text_6_1 = text_font.render(inst_6_1, True, (0, 0, 0))
        label_text_6_1_rect = label_text_6_1.get_rect(
            center=(int(600 / 2), 200))
        window.blit(label_text_6_1, label_text_6_1_rect)

        label_text_6_2 = text_font.render(inst_6_2, True, (0, 0, 0))
        label_text_6_2_rect = label_text_6_2.get_rect(
            center=(int(600 / 2), 250))
        window.blit(label_text_6_2, label_text_6_2_rect)

        label_text_6_3 = text_font.render(inst_6_3, True, (0, 0, 0))
        label_text_6_3_rect = label_text_6_3.get_rect(
            center=(int(600 / 2), 300))
        window.blit(label_text_6_3, label_text_6_3_rect)

        label_text_6_4 = text_font.render(inst_6_4, True, (0, 0, 0))
        label_text_6_4_rect = label_text_6_4.get_rect(
            center=(int(600 / 2), 350))
        window.blit(label_text_6_4, label_text_6_4_rect)

        label_text_6_5 = text_font.render(inst_6_5, True, (0, 0, 0))
        label_text_6_5_rect = label_text_6_5.get_rect(
            center=(int(600 / 2), 400))
        window.blit(label_text_6_5, label_text_6_5_rect)

        #   TIPPEK (end)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_menu = pygame.Rect(50, 600, 150, 100)
        label_button_menu = button_font.render('Menu', 1, (0, 0, 0))
        label_button_menu_rect = label_button_menu.get_rect(center=(125, 650))

        pygame.draw.rect(window, (120, 30, 70), button_menu)
        window.blit(label_button_menu, label_button_menu_rect)


        button_back = pygame.Rect(225, 600, 150, 100)
        label_button_back = button_font.render('Back', 1, (0, 0, 0))
        label_button_back_rect = label_button_back.get_rect(center=(300, 650))

        pygame.draw.rect(window, (120, 30, 70), button_back)
        window.blit(label_button_back, label_button_back_rect)

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

        if button_back.collidepoint((mouse_x, mouse_y)):
            button_back = pygame.Rect(215, 590, 170, 120)
            pygame.draw.rect(window, (160, 70, 20), button_back)
            window.blit(label_button_back, label_button_back_rect)
            if click:
                #egyet vissza
                from Instructions_3 import instructions_3
                instructions_3()

        if button_next.collidepoint((mouse_x, mouse_y)):
            button_next = pygame.Rect(390, 590, 170, 120)
            pygame.draw.rect(window, (160, 70, 20), button_next)
            window.blit(label_button_next, label_button_next_rect)
            if click:
                #egyet előre
                from Instructions_5 import instructions_5
                instructions_5()



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


instructions_4()
