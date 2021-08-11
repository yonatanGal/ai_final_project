import math
from enum import Enum
import numpy as np
from Item import Shirt,Pants
from Action import Action
from Good_Outfit import Good_Outfit
import State

THRESHOLD = 1
SHIRT = "shirt"
PANTS = "pants"

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

CELEBS = {'Justin Bieber': State.State(Shirt("Kind of long shirt", 4, (5, 24), Color.WHITE),
                                       Pants("Long loose pants", 4, (-5, 25), Color.RED)),
          'Noa Kirel': State.State(Shirt("Fila sports shirt", 3, (15, 35), Color.BLACK),
                                   Pants("Short sports pants", 3, (20, 35), Color.BLACK)),
          'Yuval Kaspit': State.State(Shirt("Loose long sleeves", 6, (15, 30), Color.YELLOW),
                                      Pants("Loose long pants", 6, (20, 30), Color.WHITE)),
          'Barack Obama': State.State(Shirt("formal suite", 10, (8, 25), Color.BLUE),
                                      Pants("formal suite pants", 10, (8, 25), Color.BLUE)),
          'Ofer Shechter': State.State(Shirt("casual T shirt", 5, (12, 30), Color.BLUE),
                                       Pants("casual jeans", 6, (13, 28), Color.GRAY)),
          'Gal Gadot': State.State(Shirt("Jeans Tank top", 7, (15, 30), Color.BLUE),
                                   Pants("Short jeans", 6, (13, 32), Color.BLUE)),
          'Morgan Freeman': State.State(Shirt("Buttoned shirt", 9, (9, 27), Color.GRAY),
                                        Pants("Tailored pants", 9, (9, 27), Color.BLACK)),
          'Arthur Read': State.State(Shirt("Sweater", 9, (9, 27), Color.YELLOW),
                                     Pants("Jeans", 9, (9, 27), Color.BLUE)),
          'Or Shpitz': State.State(Shirt("T shirt", 5, (12, 30), Color.PINK),
                                   Pants("Loose Pants", 7, (9, 27), Color.WHITE)),
          'Assi Azar': State.State(Shirt("Sweater", 5, (8, 25), Color.PURPLE),
                                   Pants("Jeans", 7, (9, 29), Color.BLUE)),

          }

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


db_shirts = [Shirt("Black T Shirt", 3, (18, 30), Color.BLACK),
             Shirt("Buttoned Long Shirt", 5, (5, 20), Color.GREEN),
             Shirt("Blouse", 7, (15, 35), Color.WHITE),
             Shirt("Sport T Shirt", 2, (15, 36), Color.BLUE),
             Shirt("Pyjama", 1, (12, 22), Color.PINK),
             Shirt("Thermal Shirt", 3, (-5, 12), Color.BLACK),
             Shirt("Casual T Shirt", 5, (12, 30), Color.BLUE),
             Shirt("Jeans Tank Top", 7, (15, 30), Color.BLUE),
             Shirt("American T Shirt", 4, (5, 28), Color.PURPLE),
             Shirt("Buttoned Short Shirt", 6, (21, 35), Color.ORANGE),
             Shirt("Sweater", 3, (-5,15), Color.YELLOW),
             Shirt("Formal Suite Shirt", 10, (8,25), Color.BLUE)
             ]


db_pants = [Pants("Long Jeans", 5, (-5, 25), Color.BLACK),
            Pants("Tailored Pants", 9, (-5, 25), Color.BROWN),
            Pants("Tights", 2, (2, 27), Color.GRAY),
            Pants("Short Skirt", 7, (18, 35), Color.WHITE),
            Pants("Business Casual Pants", 6, (10, 30), Color.YELLOW),
            Pants("Thermal Pants", 3, (-5, 13), Color.ORANGE),
            Pants("Formal Suite Shirt", 10, (8,25), Color.BLUE),
            Pants("Long loose pants", 4, (-5, 25), Color.RED),
            Pants("Casual Jeans", 6, (13, 28), Color.GRAY),
            Pants("Short Jeans", 6, (13, 32), Color.BLUE),
            Pants("Short sports pants", 3, (20, 35), Color.BLACK)
            ]

# db_shirts = [Shirt("my_black_T_shirt", 3, (18, 30), Color.BLACK),
#              Shirt("button long shirt", 5, (5, 20), Color.GREEN),
#              Shirt("blouse", 7, (15, 35), Color.WHITE)]
#
# db_pants = [Pants("jeans_long", 5, (-5, 25), Color.BLACK),
#             Pants("tailored pants", 9, (-5, 25), Color.BROWN),
#             Pants("tights", 2, (2, 27), Color.GRAY)]

db_good_outfit = [Good_Outfit(Shirt("cool button shirt", formality=6, temperature_range=(5, 25), color=Color.BLACK),
                              Pants("tights black pants", formality=5, temperature_range= (8, 28), color= Color.BLACK)),
                  Good_Outfit(Shirt("pyjama shirt", formality=0, temperature_range=(15, 28), color=Color.BLACK),
                              Pants("pyjama pants", formality=0, temperature_range=(15, 28), color=Color.BLACK)),
                  Good_Outfit(Shirt("black sport hoodie", formality=2, temperature_range=(2, 20), color=Color.BLACK),
                              Pants("black sport training", formality=2, temperature_range=(2, 20), color=Color.BLACK)),
                  Good_Outfit(Shirt("silk shirt", formality=9, temperature_range=(10, 28), color=Color.BLACK),
                              Pants("silk tailored pants", formality=9, temperature_range=(10, 28), color=Color.BLACK)),
                  Good_Outfit(Shirt("cotton black shirt", formality=3, temperature_range=(5, 18), color=Color.BLACK),
                              Pants("black jeans pants", formality=4, temperature_range=(5, 18), color=Color.BLACK))
                  ]
