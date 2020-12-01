import math
import os
import pygame
import pygame.gfxdraw
import sys
import time
from pygame.locals import *
from Text_Box_Class import *


player1_name = ''
player2_name = ''

def name_input():
    global player1_name
    global player2_name

    # Inicializálás
    pygame.init()

    # Ablak:
        # ablak igazítás középre
    os.environ['SDL_VIDEO_CENTERED'] = '1'
        # ablak megjelenítés

    window = pygame.display.set_mode((600, 800))
    pygame.display.set_caption('2048 Duel Arena')

    # betűtípus
    menu_font = pygame.font.SysFont("monospace", 30, bold=True)
    font = pygame.font.SysFont("monospace", 25)

    # háttérszín
    hatter = pygame.Color(130, 230, 140)

    menu_clock = pygame.time.Clock()

    click = False

    #text box objektumok
    text_box_player1_input = []
    text_box_player1_input.append(Text_Box(150, 250, 300, 50, border=6))

    player1_name = ''

    text_box_player2_input = []
    text_box_player2_input.append(Text_Box(150, 450, 300, 50, border=6))

    player2_name = ''

    while True:

        # -------- Ablak kialakítása / szövegek elhelyezése
        window.fill(hatter)

        label_name_changer = menu_font.render("Name Changer", 1, (0, 0, 0))
        label_name_changer_rect = label_name_changer.get_rect(
            center=(int(600 / 2), int(800 / 20)))
        window.blit(label_name_changer, label_name_changer_rect)

        label_player1 = menu_font.render("Player 1: " + str(player1_name) , 1, (0, 0, 0))
        label_player1_rect = label_player1.get_rect(
            center=(int(600 / 2), 150))
        window.blit(label_player1, label_player1_rect)

        label_player1_inst = menu_font.render("Keys: \u2191, \u2190, \u2193, \u2192, Right-CTRL", 1, (0, 0, 0))
        label_player1_inst_rect = label_player1_inst.get_rect(
            center=(int(600 / 2), 200))
        window.blit(label_player1_inst, label_player1_inst_rect)

        label_player1_name = menu_font.render("Name:", 1, (0, 0, 0))
        label_player1_name_rect = label_player1_name.get_rect(
            center=(int(600 / 6), 275))
        window.blit(label_player1_name, label_player1_name_rect)


        label_player2 = menu_font.render("Player 2: " + str(player2_name), 1, (0, 0, 0))
        label_player2_rect = label_player2.get_rect(
            center=(int(600 / 2), 350))
        window.blit(label_player2, label_player2_rect)

        label_player2_inst = menu_font.render("Keys: W, A, S, D, Left-CTRL", 1, (0, 0, 0))
        label_player2_inst_rect = label_player2_inst.get_rect(
            center=(int(600 / 2), 400))
        window.blit(label_player2_inst, label_player2_inst_rect)

        label_player2_name = menu_font.render("Name:", 1, (0, 0, 0))
        label_player2_name_rect = label_player2_name.get_rect(
            center=(int(600 / 6), 475))
        window.blit(label_player2_name, label_player2_name_rect)


        mouse_x, mouse_y = pygame.mouse.get_pos()       # egér jelenlegi pozíciója


        # --------- Gombok elhelyezése

        # --- Vissza gomb

        button_back = pygame.Rect(50, 650, 200, 100)
        label_button_back = menu_font.render('Back', 1, (0, 0, 0))
        label_button_back_rect = label_button_back.get_rect(center=(150, 700))
        pygame.draw.rect(window, (120, 30, 70), button_back)
        window.blit(label_button_back, label_button_back_rect)

        if button_back.collidepoint((mouse_x, mouse_y)):
            button_back = pygame.Rect(40, 640, 220, 120)
            pygame.draw.rect(window, (160, 70, 20), button_back)
            window.blit(label_button_back, label_button_back_rect)
            if click:

                from Main_Menu import main_menu
                main_menu()

        # ---  Game Start gomb

        button_play = pygame.Rect(350, 650, 200, 100)
        label_button_play = menu_font.render('Play', 1, (0, 0, 0))
        label_button_play_rect = label_button_play.get_rect(center=(450, 700))
        pygame.draw.rect(window, (120, 30, 70), button_play)
        window.blit(label_button_play, label_button_play_rect)

        if button_play.collidepoint((mouse_x, mouse_y)):
            button_play = pygame.Rect(340, 640, 220, 120)
            pygame.draw.rect(window, (160, 70, 20), button_play)
            window.blit(label_button_play, label_button_play_rect)
            if click:
                from Coop_2k48 import main
                main()



        click = False

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                for box in text_box_player1_input:
                    box.check_click(pygame.mouse.get_pos())
                for box in text_box_player2_input:
                    box.check_click(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                for box in text_box_player1_input:
                    if box.active:
                        box.add_text(event.key)

                        player1_name = ''.join(repr(box))
                for box in text_box_player2_input:
                    if box.active:
                        box.add_text(event.key)

                        player2_name = ''.join(repr(box))

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    from Main_Menu import main_menu
                    main_menu()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        for box in text_box_player1_input:
            box.draw(window)

        for box in text_box_player2_input:
            box.draw(window)


        pygame.display.update()
        menu_clock.tick(60)  # 60 FPS



def name_output():
    names = []
    names.append(player1_name)
    names.append(player2_name)
    return (names)



name_input()