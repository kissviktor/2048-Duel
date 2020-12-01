#2048 játék színei

BLACK = (0, 0, 0)
RED = (251, 65, 55)
PINK = (236, 40, 100)
PURPLE = (154, 40, 175)
DEEP_PURPLE = (104, 60, 180)
BLUE = (35, 152, 242)
TEAL = (0, 152, 138)
L_GREEN = (140, 192, 75)
GREEN = (62, 173, 82)
ORANGE = (255, 151, 0)
DEEP_ORANGE = (255, 85, 35)
BROWN = (120, 85, 73)

color_szotar = { 0:BLACK, 2:RED, 4:PINK, 8:PURPLE, 16:DEEP_PURPLE, 32:BLUE, 64:TEAL, 128:L_GREEN, 256:GREEN, 512:ORANGE, 1024: DEEP_ORANGE, 2048:BROWN}

def getColor(i):
    return color_szotar[i]