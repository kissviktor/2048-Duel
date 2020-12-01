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
menu_font = pygame.font.Font('PressStart2P.ttf', 46, bold=True)
button_font = pygame.font.Font('PressStart2P.ttf', 24, bold=True)
text_font = pygame.font.Font('PressStart2P.ttf', 20)

# háttérszín
hatter = pygame.Color(130, 230, 140)

menu_clock = pygame.time.Clock()

click = False

def get_highscores():

    import sqlite3

    #   Kapcsolat létrehozása és kapcsolódás hozzá
    conn = sqlite3.connect("Game_Database.db")

    #   Kurzor létrehozása, az adatbázis parancsok végrehajtására
    cursor = conn.cursor()

    cursor.execute("SELECT username, points, result FROM user WHERE username IS NOT '' ORDER BY points DESC LIMIT 3")
    scores = cursor.fetchall()

    return scores

    conn.close()


def highscores():

    score_table = get_highscores()
    print(len(score_table))

    click = False

    while True:

        window.fill(hatter)


        label_main_menu = menu_font.render("Hall of Fame", True, (0, 0, 0))  # szöveg
        label_main_menu_rect = label_main_menu.get_rect(
            center=(int(600 / 2), int(800 / 12)))               # szövegdoboz az igazításhoz
        window.blit(label_main_menu, label_main_menu_rect)


        label_text1_1 = text_font.render("Top Players", True, (0, 0, 0))
        label_text1_1_rect = label_text1_1.get_rect(
            center=(int(600 / 2), 150))
        window.blit(label_text1_1, label_text1_1_rect)

        #       TOPLISTA

        if len(score_table) < 3:
            if len(score_table) < 2:
                if len(score_table) < 1:

                    label_top_1 = text_font.render("1." , True, (0, 0, 0))
                    label_top_1_rect = label_top_1.get_rect(
                        center=(int(600 / 2), 250))
                    window.blit(label_top_1, label_top_1_rect)

                    label_top_2 = text_font.render("2.", True, (0, 0, 0))
                    label_top_2_rect = label_top_2.get_rect(
                        center=(int(600 / 2), 350))
                    window.blit(label_top_2, label_top_2_rect)

                    label_top_3 = text_font.render("3.", True, (0, 0, 0))
                    label_top_3_rect = label_top_3.get_rect(
                        center=(int(600 / 2), 450))
                    window.blit(label_top_3, label_top_3_rect)

                else:
                    pass

                label_top_1 = text_font.render("1." + score_table[0][0] + " : " + str(score_table[0][1]) + " points" + " (" + score_table[0][2] + ")", True, (0, 0, 0))
                label_top_1_rect = label_top_1.get_rect(
                    center=(int(600 / 2), 250))
                window.blit(label_top_1, label_top_1_rect)

                label_top_2 = text_font.render("2.", True, (0, 0, 0))
                label_top_2_rect = label_top_2.get_rect(
                    center=(int(600 / 2), 350))
                window.blit(label_top_2, label_top_2_rect)

                label_top_3 = text_font.render("3.", True, (0, 0, 0))
                label_top_3_rect = label_top_3.get_rect(
                    center=(int(600 / 2), 450))
                window.blit(label_top_3, label_top_3_rect)

            else:
                pass
            label_top_1 = text_font.render(
                "1." + score_table[0][0] + " : " + str(score_table[0][1]) + " points" + " (" + score_table[0][2] + ")", True, (0, 0, 0))
            label_top_1_rect = label_top_1.get_rect(
                center=(int(600 / 2), 250))
            window.blit(label_top_1, label_top_1_rect)

            label_top_2 = text_font.render("2." + score_table[1][0] + " : " + str(score_table[1][1]) + " points" +  " (" + score_table[1][2] + ")", True, (0, 0, 0))
            label_top_2_rect = label_top_2.get_rect(
                center=(int(600 / 2), 350))
            window.blit(label_top_2, label_top_2_rect)

            label_top_3 = text_font.render("3.", True, (0, 0, 0))
            label_top_3_rect = label_top_3.get_rect(
                center=(int(600 / 2), 450))
            window.blit(label_top_3, label_top_3_rect)
        else:
            pass


        #       #1 player
        label_top_1 = text_font.render("1." + score_table[0][0] + " : " + str(score_table[0][1]) + " points" + " (" + score_table[0][2] + ")", True, (0, 0, 0))
        label_top_1_rect = label_top_1.get_rect(
            center=(int(600 / 2), 250))
        window.blit(label_top_1, label_top_1_rect)

        #       #2 player
        label_top_2 = text_font.render("2." + score_table[1][0] + " : " + str(score_table[1][1]) + " points" +  " (" + score_table[1][2] + ")", True, (0, 0, 0))
        label_top_2_rect = label_top_2.get_rect(
            center=(int(600 / 2), 350))
        window.blit(label_top_2, label_top_2_rect)

        #       #3 player
        label_top_3 = text_font.render("3." + score_table[2][0] + " : " + str(score_table[2][1]) + " points" +  " (" + score_table[2][2] + ")", True, (0, 0, 0))
        label_top_3_rect = label_top_3.get_rect(
            center=(int(600 / 2), 450))
        window.blit(label_top_3, label_top_3_rect)


        mouse_x, mouse_y = pygame.mouse.get_pos()


        button_menu = pygame.Rect(50, 600, 150, 100)
        label_button_menu = button_font.render('Menu', 1, (0, 0, 0))
        label_button_menu_rect = label_button_menu.get_rect(center=(125, 650))

        pygame.draw.rect(window, (120, 30, 70), button_menu)
        window.blit(label_button_menu, label_button_menu_rect)



        if button_menu.collidepoint((mouse_x, mouse_y)):
            button_menu = pygame.Rect(40, 590, 170, 120)
            pygame.draw.rect(window, (160, 70, 20), button_menu)
            window.blit(label_button_menu, label_button_menu_rect)
            if click:
                from Main_Menu import main_menu
                main_menu()





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


highscores()
