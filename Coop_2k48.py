import math
import os
import pygame
import pygame.gfxdraw
import sys
import time
from pygame.locals import *
from colors import *
import random


Total_Points_player1 = 0
Total_Points_player2 = 0
Total_Points_winner = 0
Game_Over_Draw = False
Default_Score = 2
Board_Size = 4

# pygame inicializálás
pygame.init()

# ablak létrehozás:
# ablak igazítás középre
os.environ['SDL_VIDEO_CENTERED'] = '1'
# ablak megjelenítés
window = pygame.display.set_mode((600, 800))
pygame.display.set_caption('2048 Duel Arena')

# betűtípus
myfont = pygame.font.SysFont("monospace", 16, bold=True)
end_font = pygame.font.SysFont("monospace", 30, bold=True)
scorefont = pygame.font.Font('PressStart2P.ttf', 14)

#scorefont = pygame.font.SysFont("monospace", 22)
# háttérszín
hatter = pygame.Color(130, 230, 140)

# a későbbiekben tile-nak nevezem a "kockákat", mivel magyar megfelelő nem jutott az eszembe
tileMatrix_player1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tempMatrix_player1 = []

tileMatrix_player2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
tempMatrix_player2 = []

# az Action-höz szükséges változók

#   Az akció költségei
shoot_Cost_player1 = 100
shoot_Cost_player2 = 100

#   Az eddigi összes akció száma
shoot_Total_Counter_player1 = 0
shoot_Total_Counter_player2 = 0

#   Aktuálisan elérhető akciók száma

shoot_Actual_Counter_player1 = 0
shoot_Actual_Counter_player2 = 0




def randomTile_player1():
    # üres lista létrehozása, ahol a későbbiekben az üres mezők indexeit tárolom
    free_tile_indexes_player1 = []

    for rowindex in range(len(tileMatrix_player1)):
        for colindex in range(len(tileMatrix_player1)):
            if tileMatrix_player1[rowindex][colindex] == 0:
                free_tile_indexes_player1.append([rowindex, colindex])
                # itt tárolom el az üres mezők indexét [x,y] koordinátákként

    # most kell ellenőrizni, hogy ez a lista üres-e

    if not free_tile_indexes_player1:
        pass
        # ha üres, akkor mit csináljon

    else:
        free_coords_player1 = random.choice(free_tile_indexes_player1)
        # és végül beleírja a kettest
        tileMatrix_player1[free_coords_player1[0]][free_coords_player1[1]] = 2


def randomTile_player2():
    # üres lista létrehozása, ahol a későbbiekben az üres mezők indexeit tárolom
    free_tile_indexes_player2 = []

    for rowindex in range(len(tileMatrix_player2)):
        for colindex in range(len(tileMatrix_player2)):
            if tileMatrix_player2[rowindex][colindex] == 0:
                free_tile_indexes_player2.append([rowindex, colindex])
                # itt tárolom el az üres mezők indexét [x,y] koordinátákként

    # most kell ellenőrizni, hogy ez a lista üres-e

    if not free_tile_indexes_player2:
        pass
        # ha üres, akkor mit csináljon

    else:
        free_coords_player2 = random.choice(free_tile_indexes_player2)
        # és végül beleírja a kettest
        tileMatrix_player2[free_coords_player2[0]][free_coords_player2[1]] = 2


def CheckIfMovable_player1():  # mozgathatók-e a Tile-ok
    for i in range(0, Board_Size ** 2):
        if tileMatrix_player1[math.floor(i / Board_Size)][i % Board_Size] == 0:  # Van-e nulla
            return True
    for i in range(0, Board_Size):  # megvizsgálja, hogy a szomszédos mezőkön van-e egyező Tile
        for j in range(0, Board_Size - 1):
            if tileMatrix_player1[i][j] == tileMatrix_player1[i][j + 1]:
                return True
            elif tileMatrix_player1[j][i] == tileMatrix_player1[j + 1][i]:
                return True
    return False


def CheckIfMovable_player2():
    for i in range(0, Board_Size ** 2):
        if tileMatrix_player2[math.floor(i / Board_Size)][i % Board_Size] == 0:
            return True
    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            if tileMatrix_player2[i][j] == tileMatrix_player2[i][j + 1]:
                return True
            elif tileMatrix_player2[j][i] == tileMatrix_player2[j + 1][i]:
                return True
    return False


def Movable_player1():  # megvizsgálja, hogy bármilyen mozgásra van-e lehetőség
    for i in range(0, Board_Size):
        for j in range(1, Board_Size):
            if tileMatrix_player1[i][j - 1] == 0 and tileMatrix_player1[i][j] > 0:  # Van-e nulla ÉS mellette van-e
                return True
            elif (tileMatrix_player1[i][j - 1] == tileMatrix_player1[i][j] and tileMatrix_player1[i][
                j - 1] != 0):  # ha két szomszédos Tile értéke egyezik és nem nem nulla
                return True
    return False


def Movable_player2():
    for i in range(0, Board_Size):
        for j in range(1, Board_Size):
            if tileMatrix_player2[i][j - 1] == 0 and tileMatrix_player2[i][j] > 0:
                return True
            elif (tileMatrix_player2[i][j - 1] == tileMatrix_player2[i][j] and tileMatrix_player2[i][j - 1] != 0):
                return True
    return False


def Keyboard_Input_player1(k):  # megvizsgála, hogy a használt billentyűk a nyilak-e
    return (k == pygame.K_UP or k == pygame.K_DOWN or k == pygame.K_LEFT or k == pygame.K_RIGHT)


def Keyboard_Input_player2(k):  # megvizsgála, hogy a használt billentyűk a WASD-e
    return (k == pygame.K_w or k == pygame.K_s or k == pygame.K_a or k == pygame.K_d)


def RotationDirection_player1(k):  # forgatási irány a lenyomott billentyű alapján (nyilak kiosztás)
    if k == pygame.K_UP:
        return 1
    elif k == pygame.K_DOWN:
        return 3
    elif k == pygame.K_LEFT:
        return 0
    elif k == pygame.K_RIGHT:
        return 2


def RotationDirection_player2(k):  # forgatási irány a lenyomott billentyű alapján (WASD kiosztás)
    if k == pygame.K_w:
        return 5
    elif k == pygame.K_s:
        return 7
    elif k == pygame.K_a:
        return 4
    elif k == pygame.K_d:
        return 6


def LinearMatrixConverter_player1():  # a 2D-s mátrixból egy listát készít
    matrix_player1 = []

    for i in range(0, Board_Size ** 2):
        matrix_player1.append(tileMatrix_player1[math.floor(i / Board_Size)][i % Board_Size])

    matrix_player1.append(Total_Points_player1)  # hozzáfűzi az elért összpontszámot

    return matrix_player1


def LinearMatrixConverter_player2():  # a 2D-s mátrixból egy listát készít
    matrix_player2 = []

    for i in range(0, Board_Size ** 2):
        matrix_player2.append(tileMatrix_player2[math.floor(i / Board_Size)][i % Board_Size])

    matrix_player2.append(Total_Points_player2)  # hozzáfűzi az elért összpontszámot

    return matrix_player2


def UndoListAppend():  # temporary (átmeneti) lista
    tempMatrix_player1.append(LinearMatrixConverter_player1())
    tempMatrix_player2.append(LinearMatrixConverter_player2())


def ListToMatrixConvert_player1():  # visszaépíti a 2D-s mátrixot a listából
    if len(tempMatrix_player1) > 0:
        matrix_player1 = tempMatrix_player1.pop()

        for i in range(0, Board_Size ** 2):
            tileMatrix_player1[math.floor(i / Board_Size)][i % Board_Size] = matrix_player1[i]

        global Total_Points_player1
        Total_Points_player1 = matrix_player1[Board_Size ** 2]

        kiirMatrix()


def ListToMatrixConvert_player2():  # visszaépíti a 2D-s mátrixot a listából
    if len(tempMatrix_player2) > 0:
        matrix_player2 = tempMatrix_player2.pop()

        for i in range(0, Board_Size ** 2):
            tileMatrix_player2[math.floor(i / Board_Size)][i % Board_Size] = matrix_player2[i]

        global Total_Points_player2
        Total_Points_player2 = matrix_player2[Board_Size ** 2]

        kiirMatrix()


def MatrixRotation_player1():
    for i in range(0, int(Board_Size / 2)):
        for k in range(i, Board_Size - i - 1):
            replace_1_player1 = tileMatrix_player1[i][k]
            replace_2_player1 = tileMatrix_player1[Board_Size - 1 - k][i]
            replace_3_player1 = tileMatrix_player1[Board_Size - 1 - i][Board_Size - 1 - k]
            replace_4_player1 = tileMatrix_player1[k][Board_Size - 1 - i]

            tileMatrix_player1[Board_Size - 1 - k][i] = replace_1_player1
            tileMatrix_player1[Board_Size - 1 - i][Board_Size - 1 - k] = replace_2_player1
            tileMatrix_player1[k][Board_Size - 1 - i] = replace_3_player1
            tileMatrix_player1[i][k] = replace_4_player1


def MatrixRotation_player2():
    for i in range(0, int(Board_Size / 2)):
        for k in range(i, Board_Size - i - 1):
            replace_1_player2 = tileMatrix_player2[i][k]
            replace_2_player2 = tileMatrix_player2[Board_Size - 1 - k][i]
            replace_3_player2 = tileMatrix_player2[Board_Size - 1 - i][Board_Size - 1 - k]
            replace_4_player2 = tileMatrix_player2[k][Board_Size - 1 - i]

            tileMatrix_player2[Board_Size - 1 - k][i] = replace_1_player2
            tileMatrix_player2[Board_Size - 1 - i][Board_Size - 1 - k] = replace_2_player2
            tileMatrix_player2[k][Board_Size - 1 - i] = replace_3_player2
            tileMatrix_player2[i][k] = replace_4_player2


def Tile_Mover_player1():  # Tile mozgatása
    # oszloponként akarunk mozogni és mozgatni
    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            while tileMatrix_player1[i][j] == 0 and sum(tileMatrix_player1[i][
                                                        j:]) > 0:  # ha bármely elem 0 és van érték amit mozgatnánk, akkor az alatta lévő elemeket is fel kell mozgatni
                for k in range(j, Board_Size - 1):  # A lejjebb lévő elemek feljebb mozgatása
                    tileMatrix_player1[i][k] = tileMatrix_player1[i][k + 1]  # Minden elem feljebb mozgatása egyel
                tileMatrix_player1[i][Board_Size - 1] = 0


def Tile_Mover_player2():  # Tile mozgatása
    # oszloponként akarunk mozogni és mozgatni
    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            while tileMatrix_player2[i][j] == 0 and sum(tileMatrix_player2[i][
                                                        j:]) > 0:  # ha bármely elem 0 és van érték amit mozgatnánk, akkor az alatta lévő elemeket is fel kell mozgatni
                for k in range(j, Board_Size - 1):  # A lejjebb lévő elemek feljebb mozgatása
                    tileMatrix_player2[i][k] = tileMatrix_player2[i][k + 1]  # Minden elem feljebb mozgatása egyel
                tileMatrix_player2[i][Board_Size - 1] = 0


def Tile_Merger_player1():  # Tile-ok összeolvaszátása ("merge"-lése/fúziója)
    global Total_Points_player1

    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            if tileMatrix_player1[i][j] == tileMatrix_player1[i][j + 1] and tileMatrix_player1[i][
                j] != 0:  # ha nem nulla és egymás mellett lévő Tile-ok értéke megegyezik
                tileMatrix_player1[i][j] = tileMatrix_player1[i][j] * 2  # összeolvasztás során az érték duplázása
                tileMatrix_player1[i][j + 1] = 0
                Total_Points_player1 += tileMatrix_player1[i][j]
                Tile_Mover_player1()


def Tile_Merger_player2():  # Tile-ok összeolvaszátása ("merge"-lése/fúziója)
    global Total_Points_player2

    for i in range(0, Board_Size):
        for j in range(0, Board_Size - 1):
            if tileMatrix_player2[i][j] == tileMatrix_player2[i][j + 1] and tileMatrix_player2[i][
                j] != 0:  # ha nem nulla és egymás mellett lévő Tile-ok értéke megegyezik
                tileMatrix_player2[i][j] = tileMatrix_player2[i][j] * 2  # összeolvasztás során az érték duplázása
                tileMatrix_player2[i][j + 1] = 0
                Total_Points_player2 += tileMatrix_player2[i][j]
                Tile_Mover_player2()


#ide megy majd az action cucc
def kiir_Action():      # kiírja az akcióhoz / "lövéshez" szükséges adatokat, textet

    # Pre-action calculations

    global shoot_Cost_player1
    global shoot_Cost_player2
    global shoot_Total_Counter_player1
    global shoot_Total_Counter_player2
    global shoot_Actual_Counter_player1
    global shoot_Actual_Counter_player2

    if ((Total_Points_player1 // shoot_Cost_player1) >= 1):
        shoot_Total_Counter_player1 = shoot_Total_Counter_player1 + 1                           # növeli az összes "lövés"/akció számát
        shoot_Actual_Counter_player1 = shoot_Actual_Counter_player1 + 1                         # növeli az aktuálisan elérhető akciók számát
        shoot_Cost_player1 = shoot_Cost_player1 + 100 * (shoot_Total_Counter_player1 + 1)       # növeli a következő "lövés"/akció költségét
    else:
        pass

    if ((Total_Points_player2 // shoot_Cost_player2) >= 1):
        shoot_Total_Counter_player2 = shoot_Total_Counter_player2 + 1
        shoot_Actual_Counter_player2 = shoot_Actual_Counter_player2 + 1                         # növeli az aktuálisan elérhető akciók számát
        shoot_Cost_player2 = shoot_Cost_player2 + 100 * (shoot_Total_Counter_player2 + 1)
    else:
        pass

    # Akció szöveg megjelenítése

    # írja ki hogy van elérhető akció

        # player 1      (alsó tér)
    label_Shoots_Text_player1 = scorefont.render("Shots:", 1, (0, 0, 0))
    label_Shoots_Text_player1_rect = label_Shoots_Text_player1.get_rect(center=(200, 565))
    window.blit(label_Shoots_Text_player1, label_Shoots_Text_player1_rect)

    label_Shoot_Total_Counter_player1 = scorefont.render(str(shoot_Actual_Counter_player1), 1, (0, 0, 0))
    label_Shoot_Total_Counter_player1_rect = label_Shoot_Total_Counter_player1.get_rect(center=(200, 590))
    window.blit(label_Shoot_Total_Counter_player1, label_Shoot_Total_Counter_player1_rect)

        # player 2      (felső tér)
    label_Shoots_Text_player2 = scorefont.render("Shots:", 1, (0, 0, 0))
    label_Shoots_Text_player2_rect = label_Shoots_Text_player2.get_rect(center=(200, 115))
    window.blit(label_Shoots_Text_player2, label_Shoots_Text_player2_rect)

    label_Points_player2 = scorefont.render(str(shoot_Actual_Counter_player2), 1, (0, 0, 0))
    label_Points_player2_rect = label_Points_player2.get_rect(center=(200, 140))
    window.blit(label_Points_player2, label_Points_player2_rect)


def do_Action_player1():            # az egyes játékos akciója a kettes játékos ellen

    global shoot_Actual_Counter_player1

    # lista létrehozása, ahol a későbbiekben a nem üres mezők indexeit tárolom
    shootable_tile_indexes_player2 = []

    if shoot_Actual_Counter_player1 > 0:

        for rowindex1 in range(len(tileMatrix_player2)):
            for colindex1 in range(len(tileMatrix_player2)):
                if tileMatrix_player2[rowindex1][colindex1] > 0:
                    shootable_tile_indexes_player2.append([rowindex1, colindex1])
                    # itt tárolom el a nem üres mezők indexét [x,y] koordinátákként

        # most kell ellenőrizni, hogy ez a lista üres-e

        if len(shootable_tile_indexes_player2) <= 1 :
            pass
            # ha üres vagy csak egy eleme van, akkor mit csináljon => semmit, hiszen a másik játékos ilyenkor mozgásképtelen elsz

        else:
            shootable_coords_player2 = random.choice(shootable_tile_indexes_player2)
            # és végül kitörli az értéket
            tileMatrix_player2[shootable_coords_player2[0]][shootable_coords_player2[1]] = 0

            shoot_Actual_Counter_player1 -= 1

    else:
        pass

def do_Action_player2():            # a kettes játékos akciója az egyes játékos ellen

    global shoot_Actual_Counter_player2

    # lista létrehozása, ahol a későbbiekben a nem üres mezők indexeit tárolom
    shootable_tile_indexes_player1 = []

    if shoot_Actual_Counter_player2 > 0:

        for rowindex2 in range(len(tileMatrix_player1)):
            for colindex2 in range(len(tileMatrix_player1)):
                if tileMatrix_player1[rowindex2][colindex2] > 0:
                    shootable_tile_indexes_player1.append([rowindex2, colindex2])
                    # itt tárolom el a nem üres mezők indexét [x,y] koordinátákként

        # most kell ellenőrizni, hogy ez a lista üres-e

        if len(shootable_tile_indexes_player1) <= 1:
            pass
            # ha üres vagy csak egy eleme van, akkor mit csináljon => semmit, hiszen a másik játékos ilyenkor mozgásképtelen elsz
        else:
            shootable_coords_player1 = random.choice(shootable_tile_indexes_player1)
            # és végül kitörli az értéket
            tileMatrix_player1[shootable_coords_player1[0]][shootable_coords_player1[1]] = 0

            shoot_Actual_Counter_player2 -= 1

    else:
        pass






def GameOver():  # Játék végi szöveg kiírása
    global Total_Points_player1
    global Total_Points_player2
    global Total_Points_winner
    global Game_Over_Draw

    from Coop_Names_Input import name_output
    names = name_output()
    player1_name = names[0]
    player2_name = names[1]

    window.fill(BLACK)

    # label_gameover = myfont.render("Játék vége!", 1, (255,255,255))
    # label_gameover_rect = label_gameover.get_rect(center=(600/2, 800/2))
    # window.blit(label_gameover, (label_gameover_rect))

    if Total_Points_player1 > Total_Points_player2:
        Total_Points_winner = Total_Points_player1
    elif Total_Points_player2 > Total_Points_player1:
        Total_Points_winner = Total_Points_player2
    elif Total_Points_player2 == Total_Points_player1:
        Game_Over_Draw = True

    if Game_Over_Draw == True:

            # MINDIG DÖNTETLENT MUTAT!!!

        label_gameover = end_font.render("Játék vége!", 1, (255, 255, 255))  # szöveg
        label_gameover_rect = label_gameover.get_rect(center=(int(600 / 2), int(800 / 4)))  # szövegdoboz az igazításhoz
        label_draw = scorefont.render("Döntetlen! Elért pontotok:" + str(Total_Points_player1), 1, (255, 255, 255))
        label_draw_rect = label_draw.get_rect(center=(int(600 / 2), int(800 / 2)))
        label_restart = myfont.render("Kérlek nyomd meg az R betűt az újrakezdéshez!", 1, (255, 255, 255))
        label_restart_rect = label_restart.get_rect(center=(int(600 / 2), int(800 / 2 + 60)))
        label_back_to_menu = myfont.render("A Főmenübe visszatéréshez nyomd meg az ESC billentyűt!", 1, (255, 255, 255))
        label_back_to_menu_rect = label_back_to_menu.get_rect(center=(int(600 / 2), int(800 / 2 + 120)))

        window.blit(label_gameover, label_gameover_rect)
        window.blit(label_draw, label_draw_rect)
        window.blit(label_restart, label_restart_rect)
        window.blit(label_back_to_menu, label_back_to_menu_rect)

    else:
        if Total_Points_winner == Total_Points_player1:
            label_gameover = end_font.render("Játék vége!", 1, (255, 255, 255))  # szöveg
            label_gameover_rect = label_gameover.get_rect(center=(int(600 / 2), int(800 / 4)))  # szövegdoboz az igazításhoz
            label_winner = scorefont.render("Első helyezett: " + player1_name , 1, (255, 255, 255))
            label_winner_rect = label_winner.get_rect(center=(int(600 / 2), int(800 / 2)))
            label_winner_score = scorefont.render(player1_name + " pontszáma:" + str(Total_Points_player1), 1, (255, 255, 255))
            label_winner_score_rect = label_winner_score.get_rect(center=(int(600 / 2), int(800 / 2 + 60)))
            label_loser_score = scorefont.render(player2_name + " pontszáma:" + str(Total_Points_player2), 1, (255, 255, 255))
            label_loser_score_rect = label_loser_score.get_rect(center=(int(600 / 2), int(800 / 2 + 120)))
            label_restart = myfont.render("Kérlek nyomd meg az R betűt az újrakezdéshez!", 1, (255, 255, 255))
            label_restart_rect = label_restart.get_rect(center=(int(600 / 2), int(800 / 2 + 180)))
            label_back_to_menu = myfont.render("A Főmenübe visszatéréshez nyomd meg az ESC billentyűt!", 1, (255, 255, 255))
            label_back_to_menu_rect = label_back_to_menu.get_rect(center=(int(600 / 2), int(800 / 2 + 240)))


            window.blit(label_gameover, label_gameover_rect)
            window.blit(label_winner, label_winner_rect)
            window.blit(label_winner_score, label_winner_score_rect)
            window.blit(label_loser_score, label_loser_score_rect)
            window.blit(label_restart, label_restart_rect)
            window.blit(label_back_to_menu, label_back_to_menu_rect)

        else:
            label_gameover = end_font.render("Játék vége!", 1, (255, 255, 255))  # szöveg
            label_gameover_rect = label_gameover.get_rect(center=(int(600 / 2), int(800 / 4)))  # szövegdoboz az igazításhoz
            label_winner = scorefont.render("Első helyezett: " + player2_name, 1, (255, 255, 255))
            label_winner_rect = label_winner.get_rect(center=(int(600 / 2), int(800 / 2 )))
            label_winner_score = scorefont.render(player2_name + " pontszáma:" + str(Total_Points_player2), 1, (255, 255, 255))
            label_winner_score_rect = label_winner_score.get_rect(center=(int(600 / 2), int(800 / 2 + 60)))
            label_loser_score = scorefont.render(player1_name + " pontszáma:" + str(Total_Points_player1), 1, (255, 255, 255))
            label_loser_score_rect = label_loser_score.get_rect(center=(int(600 / 2), int(800 / 2 + 120)))
            label_restart = myfont.render("Kérlek nyomd meg az R betűt az újrakezdéshez!", 1, (255, 255, 255))
            label_restart_rect = label_restart.get_rect(center=(int(600 / 2), int(800 / 2 + 180)))
            label_back_to_menu = myfont.render("A Főmenübe visszatéréshez nyomd meg az ESC billentyűt!", 1, (255, 255, 255))
            label_back_to_menu_rect = label_back_to_menu.get_rect(center=(int(600 / 2), int(800 / 2 + 240)))


            window.blit(label_gameover, label_gameover_rect)
            window.blit(label_winner, label_winner_rect)
            window.blit(label_winner_score, label_winner_score_rect)
            window.blit(label_loser_score, label_loser_score_rect)
            window.blit(label_restart, label_restart_rect)
            window.blit(label_back_to_menu, label_back_to_menu_rect)


def SaveScores():  # highscore mentése fájlba

    from Coop_Names_Input import name_output
    names = name_output()
    player1_name = names[0]
    player2_name = names[1]

    #   Fájlkezelés (arra az esetre, ha nincs elérhető adatbázis kezelő)
    file = open("SavedScores.txt", "a")

    if Total_Points_player1 > Total_Points_player2:
        line_winner = "Player1" + ";" + player1_name + ";" + str(Total_Points_player1) + ";" + "Winner" + ";"
        line_loser = "Player2" + ";" + player2_name + ";" + str(Total_Points_player2) + ";" + "Loser" + ";"
    elif Total_Points_player2 > Total_Points_player1:
        line_winner = "Player2" + ";" + player2_name + ";" + str(Total_Points_player2) + ";" + "Winner" + ";"
        line_loser = "Player1" + ";" + player1_name + ";" + str(Total_Points_player1) + ";" + "Loser" + ";"
    else:
        line_winner = "Player1" + ";" + player1_name + ";" + str(Total_Points_player1) + ";" + "Draw" + ";"
        line_loser = "Player2" + ";" + player2_name + ";" + str(Total_Points_player2) + ";" + "Draw" + ";"

    file.write(line_winner + "\n" + line_loser + "\n")
    file.close()



    #   Adatbázis kezelés

    import sqlite3

    #   Kapcsolat létrehozása és kapcsolódás hozzá
    conn = sqlite3.connect("Game_Database.db")

    #   Kurzor létrehozása, az adatbázis parancsok végrehajtására
    cursor = conn.cursor()

    #   Létrehozza a táblát, ha még nem létezik
    cursor.execute("CREATE TABLE IF NOT EXISTS user (username TEXT, points INTEGER, result TEXT)")


    sqlite_insert_parameters = """INSERT INTO user
                          (username, points, result) 
                          VALUES (?, ?, ?);"""

    #data_tuple_player1 = (player1_name, Total_Points_player1, "Win")
    #data_tuple_player2 = (player2_name, Total_Points_player2, "Lose")

    if Total_Points_player1 > Total_Points_player2:
        data_tuple_player1 = (player1_name, Total_Points_player1, "Win")
        data_tuple_player2 = (player2_name, Total_Points_player2, "Lose")

        cursor.execute(sqlite_insert_parameters, data_tuple_player1)
        cursor.execute(sqlite_insert_parameters, data_tuple_player2)

    elif Total_Points_player2 > Total_Points_player1:
        data_tuple_player2 = (player2_name, Total_Points_player2, "Win")
        data_tuple_player1 = (player1_name, Total_Points_player1, "Lose")

        cursor.execute(sqlite_insert_parameters, data_tuple_player2)
        cursor.execute(sqlite_insert_parameters, data_tuple_player1)

    else:
        data_tuple_player1 = (player1_name, Total_Points_player1, "Draw")
        data_tuple_player2 = (player2_name, Total_Points_player2, "Draw")

        cursor.execute(sqlite_insert_parameters, data_tuple_player1)
        cursor.execute(sqlite_insert_parameters, data_tuple_player2)


    #   Commit (mentés)
    conn.commit()
    #   Kapcsolat bontása
    conn.close()



def ResetGame():
    global Total_Points_player1
    global tileMatrix_player1
    global Total_Points_player2
    global tileMatrix_player2

    global shoot_Cost_player1
    global shoot_Cost_player2
    global shoot_Total_Counter_player1
    global shoot_Total_Counter_player2
    global shoot_Actual_Counter_player1
    global shoot_Actual_Counter_player2

    Total_Points_player1 = 0
    Total_Points_player2 = 0

    window.fill(BLACK)

    tileMatrix_player1 = [[0 for i in range(0, Board_Size)] for j in range(0, Board_Size)]
    tileMatrix_player2 = [[0 for i in range(0, Board_Size)] for j in range(0, Board_Size)]

    #   Az akció költségei
    shoot_Cost_player1 = 100
    shoot_Cost_player2 = 100

    #   Az eddigi összes akció száma
    shoot_Total_Counter_player1 = 0
    shoot_Total_Counter_player2 = 0

    #   Aktuálisan elérhető akciók száma

    shoot_Actual_Counter_player1 = 0
    shoot_Actual_Counter_player2 = 0

    #main()
    from Coop_Names_Input import name_input
    name_input()


def kiirMatrix():
    window.fill(hatter)

    # játéktér háttere (alsó és felső)
    pygame.draw.rect(window, pygame.Color(255, 255, 100), (300, 500, 250, 250))
    pygame.draw.rect(window, pygame.Color(255, 255, 100), (300, 50, 250, 250))

    # Név / Pont illetve torony háttere

    pygame.draw.rect(window, pygame.Color(255, 255, 100), (150, 15, 400, 25))  # felső név
    pygame.draw.rect(window, pygame.Color(255, 255, 100), (150, 50, 100, 100))  # felső pont
    #pygame.draw.rect(window, pygame.Color(255, 255, 100), (150, 200, 100, 100))  # felső torony

    pygame.draw.rect(window, pygame.Color(255, 255, 100), (150, 465, 400, 25))  # alsó név
    #pygame.draw.rect(window, pygame.Color(255, 255, 100), (150, 500, 100, 100))  # alsó torony
    pygame.draw.rect(window, pygame.Color(255, 255, 100), (150, 500, 100, 100))  # alsó pont

    global Board_Size
    global Total_Points_player1
    global Total_Points_player1

    from Coop_Names_Input import name_output
    names = name_output()
    player1_name = names[0]
    player2_name = names[1]

    # az alsó 4x4-es játékteren lévő Tile-ok kirajzolása
    for i in range(0, Board_Size):
        for j in range(0, Board_Size):
            pygame.draw.rect(window, getColor(tileMatrix_player1[i][j]), (j * 60 + 310, i * 60 + 510, 50, 50))

            label_Tile_player1 = myfont.render(str(tileMatrix_player1[i][j]), 1, (255, 255, 255))  # Tile-ok szövege

            label_Name_player1 = scorefont.render(player1_name, 1, (0, 0, 0))               # név kiírás, jó
            label_Name_player1_rect = label_Name_player1.get_rect(center=(350, 480))        # név koord, jó
            window.blit(label_Name_player1, label_Name_player1_rect)                        # név kiírása

            label_Score_player1 = scorefont.render("Points:", 1, (0, 0, 0))
            label_Score_player1_rect = label_Score_player1.get_rect(center=(200, 515))
            window.blit(label_Score_player1, label_Score_player1_rect)                      # pontok szöveg kiírása

            label_Points_player1 = scorefont.render(str(Total_Points_player1), 1, (0, 0, 0))
            label_Points_player1_rect = label_Points_player1.get_rect(center=(200, 540))
            window.blit(label_Points_player1, label_Points_player1_rect)                    # aktuális pont kiírása


            window.blit(label_Tile_player1, (j * 60 + 310 + 10, i * 60 + 510 + 20))  # Tile-ok kiírása


    # a felső 4x4-es játékteren lévő Tile-ok kirajzolása
    for i in range(0, Board_Size):
        for j in range(0, Board_Size):
            pygame.draw.rect(window, getColor(tileMatrix_player2[i][j]), (j * 60 + 310, i * 60 + 60, 50, 50))

            label_Tile_player2 = myfont.render(str(tileMatrix_player2[i][j]), 1, (255, 255, 255))  # Tile-ok szövege


            label_Name_player2 = scorefont.render(player2_name, 1, (0, 0, 0))  # név kiírás, jó
            label_Name_player2_rect = label_Name_player2.get_rect(center=(350, 30))  # név koord, jó
            window.blit(label_Name_player2, label_Name_player2_rect)  # név kiírása

            label_Score_player2 = scorefont.render("Points:", 1, (0, 0, 0))
            label_Score_player2_rect = label_Score_player2.get_rect(center=(200, 65))
            window.blit(label_Score_player2, label_Score_player2_rect)  # pontok szöveg kiírása

            label_Points_player2 = scorefont.render(str(Total_Points_player2), 1, (0, 0, 0))
            label_Points_player2_rect = label_Points_player2.get_rect(center=(200, 90))
            window.blit(label_Points_player2, label_Points_player2_rect)  # aktuális pont kiírása


            window.blit(label_Tile_player2, (j * 60 + 310 + 10, i * 60 + 60 + 20))  # Tile-ok kiírása


def main(fromLoaded=False):



    if not fromLoaded:
        global Total_Points_player1
        global tileMatrix_player1
        global Total_Points_player2
        global tileMatrix_player2

        Total_Points_player1 = 0
        Total_Points_player2 = 0

        window.fill(BLACK)

        tileMatrix_player1 = [[0 for i in range(0, Board_Size)] for j in range(0, Board_Size)]
        tileMatrix_player2 = [[0 for i in range(0, Board_Size)] for j in range(0, Board_Size)]

        randomTile_player1()
        randomTile_player1()
        randomTile_player2()
        randomTile_player2()

    kiirMatrix()
    kiir_Action()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # kilépés a jobb felső X-el
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if Total_Points_player1 != 0 or Total_Points_player2 != 0:
                        SaveScores()
                    GameOver()

            if CheckIfMovable_player1() == True and CheckIfMovable_player2() == True:  # meghívja az összemozgatást ellenőrző fgv-t
                if event.type == KEYDOWN:

                    if Keyboard_Input_player1(event.key):
                        rotate_player1 = RotationDirection_player1(event.key)  # forgatási irány függvény meghívása

                        UndoListAppend()

                        for i in range(0, rotate_player1):
                            MatrixRotation_player1()

                        if Movable_player1():
                            Tile_Mover_player1()
                            Tile_Merger_player1()
                            randomTile_player1()

                        for j in range(0, (4 - rotate_player1) % 4):
                            MatrixRotation_player1()

                        kiirMatrix()
                        kiir_Action()


                    if Keyboard_Input_player2(event.key):
                        rotate_player2 = RotationDirection_player2(event.key)

                        UndoListAppend()

                        for k in range(0, rotate_player2):
                            MatrixRotation_player2()

                        if Movable_player2():
                            Tile_Mover_player2()
                            Tile_Merger_player2()
                            randomTile_player2()

                        for l in range(0, (4 - rotate_player2) % 4):
                            MatrixRotation_player2()

                        kiirMatrix()
                        kiir_Action()


            else:
                if Total_Points_player1 != 0 or Total_Points_player2 != 0:
                    SaveScores()
                GameOver()

            # Ide jön az Action
            if event.type == KEYDOWN:
                if event.key == pygame.K_RCTRL:

                    do_Action_player1()
                    kiirMatrix()
                    kiir_Action()

            #if event.type == KEYDOWN:
                elif event.key == pygame.K_LCTRL:

                    do_Action_player2()
                    kiirMatrix()
                    kiir_Action()

            if event.type == KEYDOWN:

                if event.key == pygame.K_r:
                    ResetGame()


                if event.key == pygame.K_ESCAPE:
                    from Main_Menu import main_menu
                    main_menu()


        pygame.display.update()     # Update!!



main()
