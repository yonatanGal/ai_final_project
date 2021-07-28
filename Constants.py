import math
from enum import Enum
import numpy as np
from Clothes import *

THRESHOLD = 1


class Color():
    #     BLUE = 'blue'
    #     RED = 'red'
    #     YELLOW = 'yellow'
    #     GREEN = 'green'
    #     BROWN = 'brown'
    #     ORANGE = 'orange'
    #     PINK = 'pink'
    #     PURPLE = 'purple'
    #     GRAY = 'gray'
    #     BLACK = 'black'
    #     WHITE = 'white'
    #
    #

    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BROWN = (165, 42, 42)
    ORANGE = (255, 165, 0)
    PINK = (255, 192, 203)
    PURPLE = (128, 0, 128)
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


color_lst = [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN, Color.BROWN, Color.ORANGE, Color.PINK, Color.PURPLE,
             Color.GRAY, Color.BLACK, Color.WHITE]

UNMATCHINGCOLORS = {Color.BLUE: {Color.RED,
                                 Color.YELLOW,
                                 Color.GREEN,
                                 Color.BROWN,
                                 Color.ORANGE,
                                 Color.PINK,
                                 Color.PURPLE,
                                 Color.BLUE},

                    Color.RED: {Color.YELLOW,
                                Color.GREEN,
                                Color.BROWN,
                                Color.ORANGE,
                                Color.PINK,
                                Color.PURPLE,
                                Color.RED,
                                Color.BLUE},

                    Color.YELLOW: {Color.GREEN,
                                   Color.ORANGE,
                                   Color.BROWN,
                                   Color.PINK,
                                   Color.PURPLE,
                                   Color.YELLOW,
                                   Color.RED,
                                   Color.BLUE},

                    Color.GREEN: {Color.BROWN,
                                  Color.ORANGE,
                                  Color.PINK,
                                  Color.PURPLE,
                                  Color.GREEN,
                                  Color.YELLOW,
                                  Color.RED,
                                  Color.BLUE},

                    Color.BROWN: {Color.ORANGE,
                                  Color.PINK,
                                  Color.PURPLE,
                                  Color.BLACK,
                                  Color.BROWN,
                                  Color.GREEN,
                                  Color.YELLOW,
                                  Color.RED,
                                  Color.BLUE},

                    Color.ORANGE: {Color.PINK,
                                   Color.PURPLE,
                                   Color.ORANGE,
                                   Color.BROWN,
                                   Color.GREEN,
                                   Color.YELLOW,
                                   Color.RED,
                                   Color.BLUE},

                    Color.PINK: {Color.PINK,
                                 Color.PURPLE,
                                 Color.ORANGE,
                                 Color.BROWN,
                                 Color.GREEN,
                                 Color.YELLOW,
                                 Color.RED,
                                 Color.BLUE},

                    Color.PURPLE: {Color.PINK,
                                   Color.PURPLE,
                                   Color.ORANGE,
                                   Color.BROWN,
                                   Color.GREEN,
                                   Color.YELLOW,
                                   Color.RED,
                                   Color.BLUE},

                    Color.GRAY: {Color.GRAY},

                    Color.BLACK: {Color.BROWN},

                    Color.WHITE: {}
                    }


def colors_distance(color1, color2):
    (r1, g1, b1) = color1
    (r2, g2, b2) = color2
    return np.sqrt((r1 - r2) ^ 2 + (g1 - g2) ^ 2 + (b1 - b2) ^ 2)


db_shirts = [Shirt("my_black_T_shirt", 3, (18, 30), Color.BLACK),
             Shirt("button long shirt", 5, (5, 20), Color.GREEN),
             Shirt("blouse", 7, (15, 35), Color.WHITE),
             Shirt("sport_tshirt", 1, (15, 40), Color.BLUE),
             Shirt("pyjama", 0, (12, 22), Color.PINK),
             Shirt("thermal shirt", 3, (-5, 12), Color.BLACK)]

db_pants = [Pants("jeans_long", 5, (-5, 25), Color.BLACK),
            Pants("tailored pants", 9, (-5, 25), Color.BROWN),
            Pants("tights", 2, (2, 27), Color.GRAY),
            Pants("short skirt", 7, (18, 35), Color.WHITE),
            Pants("business casual pants", 6, (10, 30), Color.YELLOW),
            Pants("thermal pants", 3, (-5, 13), Color.ORANGE)]
