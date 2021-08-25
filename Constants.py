import math
from enum import Enum
import numpy as np
from Item import Shirt, Pants, Shoes
from Action import Action
import State

THRESHOLD = 1
SHIRT = "shirt"
PANTS = "pants"
SHOES = "shoes"

CSP_AND_QLEARNING = 1
CSP_ONLY_BEST_MATCH = 2
CSP_ONLY_RANDOM_CHOICE = 3

HOME = 1
SPORT = 2
CASUAL = 3
CASUAL_ELEGANT = 4
FORMAL = 5

COLD = 0
WARM = 1
HOT = 2


class Color():
    """
    a class for the colors the solver deals with
    """
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


COLORS_LIST = [Color.BLUE, Color.RED, Color.YELLOW, Color.GREEN, Color.BROWN,
               Color.ORANGE, Color.PINK, Color.PURPLE,
               Color.GRAY, Color.BLACK, Color.WHITE]

HOME_LIST = [State.CelebState(Shirt("White Hoodie", 1, (0, 15), Color.WHITE),
                              Pants("Red Long Pants", 1, (0, 15), Color.RED),
                              Shoes("White Nike Air", 1, (0, 15), Color.WHITE),
                              "Justin Bieber"),
             State.CelebState(
                 Shirt("White Long Sleeve Shirt", 1, (0, 15), Color.WHITE),
                 Pants("White Long Sleeve Pants", 1, (0, 15), Color.RED),
                 Shoes("White Slippers", 1, (0, 15), Color.WHITE),
                 "Eliana Tidhar"),
             State.CelebState(
                 Shirt("Gray hoodie", 1, (0, 15), Color.GRAY),
                 Pants("Gray Long tights", 1, (0, 15), Color.GRAY),
                 Shoes("Slippers", 1, (0, 15), Color.GRAY),
                 "Coral Simanovich"),
             State.CelebState(
                 Shirt("Brown PJ Tank Top", 1, (16, 25), Color.BROWN),
                 Pants("Brown Long Sleeve Pants", 1, (16, 25), Color.BROWN),
                 Shoes("Slippers", 1, (16, 25), Color.WHITE),
                 "Eliana Tidhar"), State.CelebState(
        Shirt("White T Shirt", 1, (16, 25), Color.WHITE),
        Pants("Black Long Sweat Pants", 1, (16, 25), Color.BLACK),
        Shoes("Black Slippers", 1, (16, 25), Color.BLACK),
        "Delta Model Male"),
             State.CelebState(
                 Shirt("White T Shirt", 1, (16, 25), Color.WHITE),
                 Pants("Black Long Tights", 1, (16, 25), Color.BLACK),
                 Shoes("White Slippers", 1, (16, 25), Color.WHITE),
                 "Roni Sheinkman"),
             State.CelebState(
                 Shirt("Yellow T Shirt", 1, (26, 35), Color.YELLOW),
                 Pants("Yellow Short PJ Pants", 1, (26, 35), Color.YELLOW),
                 Shoes("White Slippers", 1, (26, 35), Color.WHITE),
                 "Eliana Tidhar"), State.CelebState(
        Shirt("Gray PJ Tank Top", 1, (26, 35), Color.GRAY),
        Pants("Gray Short PJ Pants", 1, (26, 35), Color.GRAY),
        Shoes("Pink Slippers", 1, (26, 35), Color.PINK),
        "Delta Model Male"), State.CelebState(
        Shirt("White T shirt", 1, (26, 35), Color.WHITE),
        Pants("White Short PJ Pants", 1, (26, 35), Color.WHITE),
        Shoes("Brown Slippers", 1, (26, 35), Color.BROWN),
        "Danit Greenberg")]

SPORTS_LIST = [
    State.CelebState(
        Shirt("Blue Long Sleeve Sweat Shirt Cropped Top", 2, (0, 15),
              Color.BLUE),
        Pants("Blue Long Sweat Pants", 2, (0, 15), Color.BLUE),
        Shoes("White Nike Sports Shoes", 2, (0, 15), Color.WHITE),
        "Liel Eli"), State.CelebState(
        Shirt("Yellow Long Sleeve Sweat Shirt", 2, (0, 15), Color.BLUE),
        Pants("Black Tights", 2, (0, 15), Color.BLACK),
        Shoes("Black Sport Shoes", 2, (0, 15), Color.BLACK),
        "Dana Frider"),

    State.CelebState(
        Shirt("Black long sleeve shirt", 1, (0, 15), Color.BLACK),
        Pants("Black Long tights", 1, (0, 15), Color.BLACK),
        Shoes("White nike shoes", 1, (0, 15), Color.WHITE),
        "Coral Simanovich"),

    State.CelebState(
        Shirt("Pink hoodie", 1, (0, 15), Color.PINK),
        Pants("Pink Long tights", 1, (0, 15), Color.PINK),
        Shoes("White nike shoes", 1, (0, 15), Color.WHITE),
        "Coral Simanovich"),

    State.CelebState(
        Shirt("White Adidas SeeThrough Tank Top", 2, (16, 25), Color.WHITE),
        Pants("Red Wide Training Pants", 2, (16, 25), Color.RED),
        Shoes("Red Sport Shoes", 2, (16, 25), Color.RED),
        "Maya Wertheimer"), State.CelebState(
        Shirt("Brown Training Top", 2, (16, 25), Color.BROWN),
        Pants("Brown Tights", 2, (16, 25), Color.BROWN),
        Shoes("White Sport Shoes", 2, (16, 25), Color.WHITE),
        "Yarden Visel"),

    State.CelebState(
        Shirt("Black Training Top", 2, (16, 25), Color.BLACK),
        Pants("Black Tights", 2, (16, 25), Color.BLACK),
        Shoes("Black Sport Shoes", 2, (16, 25), Color.BLACK),
        "Danit Greenberg"),

    State.CelebState(
        Shirt("Pink Training Top", 2, (16, 25), Color.PINK),
        Pants("Pink Tights", 2, (16, 25), Color.PINK),
        Shoes("White Sport Shoes", 2, (16, 25), Color.WHITE),
        "Coral Simanovich"),

    State.CelebState(
        Shirt("Black Training Tank Top", 2, (26, 35), Color.BLACK),
        Pants("Black Short Training Pants", 2, (26, 35), Color.BLACK),
        Shoes("Pink Sport Shoes", 2, (26, 35), Color.PINK),
        "Yarden Jerbi"), State.CelebState(
        Shirt("Pink Training Top", 2, (26, 35), Color.PINK),
        Pants("White Short Training Pants", 2, (26, 35), Color.WHITE),
        Shoes("White Sport Shoes", 2, (26, 35), Color.WHITE),
        "Yarden Visel"), State.CelebState(
        Shirt("White wide T shirt", 2, (26, 35), Color.WHITE),
        Pants("Black Short Training Pants", 2, (26, 35), Color.BLACK),
        Shoes("White Sport Shoes", 2, (26, 35), Color.WHITE),
        "Liel Eli")]

CASUAL_LIST = [State.CelebState(
    Shirt("White Long Hoodie", 3, (0, 15),
          Color.WHITE),
    Pants("Blue Long Jeans", 3, (0, 15), Color.BLUE),
    Shoes("Black Sneaker", 3, (0, 15), Color.BLACK),
    "Anne Zivi"), State.CelebState(
    Shirt("Gray Long Knit", 3, (0, 15),
          Color.GRAY),
    Pants("Black Mom Jeans", 3, (0, 15), Color.BLACK),
    Shoes("Black Short Boots", 3, (0, 15), Color.BLACK),
    "Roni Sheinkman"),
    State.CelebState(
        Shirt("Black Long Hoodie", 3, (0, 15), Color.BLACK),
        Pants("Blue Long Jeans", 3, (0, 15), Color.BLUE),
        Shoes("White allstar", 3, (0, 15), Color.WHITE),
        "Liel Eli"),
    State.CelebState(
        Shirt("White Long shirt", 3, (0, 15), Color.WHITE),
        Pants("Black Long Jeans", 3, (0, 15), Color.BLACK),
        Shoes("Black short boots", 3, (0, 15), Color.BLACK),
        "Danit Greenberg"),
    State.CelebState(
        Shirt("White Long sweeter", 3, (0, 15), Color.WHITE),
        Pants("Blue Long Jeans", 3, (0, 15), Color.BLUE),
        Shoes("White jordens", 3, (0, 15), Color.WHITE),
        "Coral Simanovich"),
    State.CelebState(
        Shirt("Pink Polo", 3, (16, 25),
              Color.PINK),
        Pants("Black Short Jeans", 3, (16, 25), Color.BLACK),
        Shoes("White Sandals", 3, (16, 25), Color.WHITE),
        "Maya Wertheimer"), State.CelebState(
        Shirt("Black Strapless Shirt", 3, (16, 25),
              Color.BLACK),
        Pants("Pink Paddlephone Pants", 3, (16, 25), Color.PINK),
        Shoes("Black Sandals", 3, (16, 25), Color.BLACK),
        "Anne Zivi"),
    State.CelebState(
        Shirt("Brown strapless", 3, (16, 25), Color.BROWN),
        Pants("Blue Long Jeans", 3, (16, 25), Color.BLUE),
        Shoes("White adidas sneakers", 3, (16, 25), Color.WHITE),
        "Liel Eli"),
    State.CelebState(
        Shirt("White T shirt", 3, (16, 25), Color.WHITE),
        Pants("Blue Long Jeans", 3, (16, 25), Color.BLUE),
        Shoes("Black allstar", 3, (16, 25), Color.BLACK),
        "Danit Greenberg"),

    State.CelebState(
        Shirt("White tank top", 3, (16, 25), Color.WHITE),
        Pants("Blue Long Jeans", 3, (16, 25), Color.BLUE),
        Shoes("Pink flip flops", 3, (16, 25), Color.PINK),
        "Danit Greenberg"),

    State.CelebState(
        Shirt("Black Fila T Shirt", 3, (26, 35),
              Color.BLACK),
        Pants("Blue Short Jeans", 3, (26, 35), Color.BLUE),
        Shoes("White Sneakers", 3, (26, 35), Color.WHITE),
        "Noa Kirel"), State.CelebState(
        Shirt("Purple Tank Top", 3, (26, 35),
              Color.PURPLE),
        Pants("Blue Short Jeans", 3, (26, 35), Color.BLUE),
        Shoes("Brown Sandals", 3, (26, 35), Color.BROWN),
        "Avishag Samberg"),
    State.CelebState(
        Shirt("Pink T shirt", 3, (26, 35), Color.PINK),
        Pants("Pink Short tights", 3, (26, 35), Color.PINK),
        Shoes("White fila sneakers", 3, (26, 35), Color.WHITE),
        "Danit Greenberg")]

CASUAL_ELEGANT_LIST = [State.CelebState(
    Shirt("Black Long Elegant Hoodie", 4, (0, 15),
          Color.BLACK),
    Pants("Black Leather Skirt", 4, (0, 15), Color.BLACK),
    Shoes("Black Short Boots", 4, (0, 15), Color.BLACK),
    "Roni Sheinkman"), State.CelebState(
    Shirt("White CK Long Sleeve Shirt", 4, (0, 15),
          Color.WHITE),
    Pants("Red Paddlephone Pants", 4, (0, 15), Color.RED),
    Shoes("White Nike Air", 4, (0, 15), Color.WHITE),
    "Bar Refaeli"),
    State.CelebState(
        Shirt("White long sleeve shirt", 4, (0, 15), Color.WHITE),
        Pants("Brown Paddlephone Pants", 1, (0, 15), Color.BROWN),
        Shoes("Black short boots", 1, (0, 15), Color.BLACK),
        "Coral Simanovich"),

    State.CelebState(
        Shirt("Yellow strapless", 4, (16, 25),
              Color.YELLOW),
        Pants("Brown tailored pants", 4, (16, 25), Color.BROWN),
        Shoes("Brown elegant flip flops", 4, (16, 25), Color.BROWN),
        "Danit Greenberg"),

    State.CelebState(
        Shirt("White long sleeve shirt", 4, (16, 25),
              Color.WHITE),
        Pants("Black short jeans", 4, (16, 25), Color.BLACK),
        Shoes("Black short boots", 4, (16, 25), Color.BLACK),
        "Danit Greenberg"),

    State.CelebState(
        Shirt("White T shirt", 4, (16, 25),
              Color.WHITE),
        Pants("Black Paddlephone Pants", 4, (16, 25), Color.BLACK),
        Shoes("Black short boots", 4, (16, 25), Color.BLACK),
        "Danit Greenberg"),

    State.CelebState(
        Shirt("White T Shirt", 4, (16, 25),
              Color.WHITE),
        Pants("Midi Black Skirt", 4, (16, 25), Color.BLACK),
        Shoes("Black Short Boots", 4, (16, 25), Color.BLACK),
        "Adi Himelbloy"), State.CelebState(
        Shirt("Blue One Sleeve Shirt", 4, (16, 25),
              Color.BLUE),
        Pants("Blue Jeans", 4, (16, 25), Color.BLUE),
        Shoes("Brown Sandals", 4, (16, 25), Color.BROWN),
        "Maya Wertheimer"), State.CelebState(
        Shirt("White Cropped Tank Top", 4, (26, 35),
              Color.WHITE),
        Pants("White Short Skirt", 4, (26, 35), Color.WHITE),
        Shoes("Yellow Sandals", 4, (26, 35), Color.YELLOW),
        "Neta Alchimister"), State.CelebState(
        Shirt("Purple Puffy Sleeves Shirt", 4, (26, 35),
              Color.PURPLE),
        Pants("Gray Short Skirt", 4, (26, 35), Color.GRAY),
        Shoes("White Sandals", 4, (26, 35), Color.WHITE),
        "Anna Aronov"),

    State.CelebState(
        Shirt("White strapless", 4, (26, 35),
              Color.WHITE),
        Pants("Brown Paddlephone pants", 4, (16, 25), Color.BROWN),
        Shoes("Brown elegant flip flops", 4, (16, 25), Color.BROWN),
        "Coral Simanovich"),

    State.CelebState(
        Shirt("Red crop t shirt", 4, (26, 35),
              Color.RED),
        Pants("Red skirt", 4, (16, 25), Color.RED),
        Shoes("White elegant flip flops", 4, (16, 25), Color.WHITE),
        "Danit Greenberg")
]

FORMAL_LIST = [State.CelebState(
    Shirt("Green Blazer", 5, (0, 15),
          Color.GREEN),
    Pants("Green Tailored Pants", 5, (0, 15), Color.GREEN),
    Shoes("Black Short Boots", 5, (0, 15), Color.BLACK),
    "Roni Sheinkman"), State.CelebState(
    Shirt("Red Blazer", 5, (0, 15),
          Color.RED),
    Pants("Red Tailored Pants", 5, (0, 15), Color.RED),
    Shoes("Black Pointy High Heels", 5, (0, 15), Color.BLACK),
    "Gal Gadot"),
    State.CelebState(
        Shirt("Gray Blazer", 5, (0, 15),
              Color.GRAY),
        Pants("Blue jeans", 5, (0, 15), Color.BLUE),
        Shoes("Black Pointy High Heels", 5, (0, 15), Color.BLACK),
        "Coral Simanovich"),

    State.CelebState(
        Shirt("Pink Blazer", 5, (16, 25),
              Color.PINK),
        Pants("Pink Skirt", 5, (16, 25), Color.PINK),
        Shoes("White High Heels", 5, (16, 25), Color.WHITE),
        "Yarden Jerbi"), State.CelebState(
        Shirt("White Strapless Cropped Long Crochet", 5, (16, 25),
              Color.WHITE),
        Pants("White Long Paddlephone Crochet", 5, (16, 25), Color.WHITE),
        Shoes("Red High Heels", 5, (16, 25), Color.RED),
        "Neta Alchimister"),

    State.CelebState(
        Shirt("White one shoulder shirt", 5, (16, 25),
              Color.WHITE),
        Pants("White Long Paddlephone with drawings", 5, (16, 25), Color.WHITE),
        Shoes("Brown crochet platform", 5, (16, 25), Color.BROWN),
        "Coral Simanovich"),
    State.CelebState(
        Shirt("Black One Sleeve Tank Top", 5, (26, 35),
              Color.BLACK),
        Pants("Black Tailored Pants", 5, (26, 35), Color.BLACK),
        Shoes("Yellow High Heels", 5, (26, 35), Color.YELLOW),
        "Agam Rudberg"), State.CelebState(
        Shirt("Pink Puffy Sleeves Shirt", 5, (26, 35),
              Color.PINK),
        Pants("White Skirt", 5, (26, 35), Color.WHITE),
        Shoes("White Low Heels", 5, (26, 35), Color.WHITE),
        "Anna Aronov"),
    State.CelebState(
        Shirt("Black elegant tank top", 5, (26, 35),
              Color.BLACK),
        Pants("Black Skirt", 5, (26, 35), Color.BLACK),
        Shoes("Black high Heels", 5, (26, 35), Color.BLACK),
        "Liel Eli")
]

STYLES = {HOME: HOME_LIST, SPORT: SPORTS_LIST, CASUAL: CASUAL_LIST,
          CASUAL_ELEGANT: CASUAL_ELEGANT_LIST, FORMAL: FORMAL_LIST}

UNMATCHINGCOLORS = {Color.BLUE: {Color.RED,
                                 Color.YELLOW,
                                 Color.GREEN,
                                 Color.BROWN,
                                 Color.ORANGE,
                                 Color.PINK,
                                 Color.PURPLE},

                    Color.RED: {Color.YELLOW,
                                Color.GREEN,
                                Color.BROWN,
                                Color.ORANGE,
                                Color.PINK,
                                Color.PURPLE,
                                Color.BLUE},

                    Color.YELLOW: {Color.GREEN,
                                   Color.ORANGE,
                                   Color.BROWN,
                                   Color.PINK,
                                   Color.PURPLE,
                                   Color.RED,
                                   Color.BLUE},

                    Color.GREEN: {Color.BROWN,
                                  Color.ORANGE,
                                  Color.PINK,
                                  Color.PURPLE,
                                  Color.YELLOW,
                                  Color.RED,
                                  Color.BLUE},

                    Color.BROWN: {Color.ORANGE,
                                  Color.PINK,
                                  Color.PURPLE,
                                  Color.BLACK,
                                  Color.GREEN,
                                  Color.YELLOW,
                                  Color.RED,
                                  Color.BLUE},

                    Color.ORANGE: {Color.PINK,
                                   Color.PURPLE,
                                   Color.BROWN,
                                   Color.GREEN,
                                   Color.YELLOW,
                                   Color.RED,
                                   Color.BLUE},

                    Color.PINK: {
                        Color.PURPLE,
                        Color.ORANGE,
                        Color.BROWN,
                        Color.GREEN,
                        Color.YELLOW,
                        Color.RED,
                        Color.BLUE},

                    Color.PURPLE: {Color.PINK,
                                   Color.ORANGE,
                                   Color.BROWN,
                                   Color.GREEN,
                                   Color.YELLOW,
                                   Color.RED,
                                   Color.BLUE},

                    Color.GRAY: {},

                    Color.BLACK: {Color.BROWN},

                    Color.WHITE: {}
                    }

DB_SHOES = [Shoes("Black Sneakers", 3, (0, 35), Color.BLACK),
            Shoes("Black Winter Boots", 4, (0, 12), Color.BLACK),
            Shoes("White Nike Sports Shoes", 2, (0, 35), Color.WHITE),
            Shoes("White Slippers", 1, (0, 35), Color.WHITE),
            Shoes("Black Slippers", 1, (0, 35), Color.BLACK),
            Shoes("Pink Slippers", 1, (0, 35), Color.PINK),
            Shoes("Yellow Slippers", 1, (0, 35), Color.YELLOW),
            Shoes("Brown Oxford Shoes", 4, (0, 35), Color.BROWN),
            Shoes("Red High Heels", 5, (0, 35), Color.RED),
            Shoes("Black High Heels", 5, (0, 35), Color.BLACK),
            Shoes("White High Heels", 5, (0, 35), Color.WHITE),
            Shoes("Brown Blundstone", 3, (0, 35), Color.BROWN),
            Shoes("Shoresh Sandals", 3, (25, 35), Color.PURPLE),
            Shoes("Black Elegant Sandals", 4, (22, 35), Color.BLACK),
            Shoes("White Elegant Sandals", 4, (22, 35), Color.WHITE),
            Shoes("Brown Elegant Sandals", 4, (22, 35), Color.BROWN),
            Shoes("Blue Sneakers", 3, (0, 35), Color.BLUE),
            Shoes("White Nike Air", 3, (0, 35), Color.WHITE)
            ]

DB_SHIRTS = [Shirt("Black T Shirt", 3, (15, 35), Color.BLACK),
             Shirt("White T Shirt", 3, (15, 35), Color.WHITE),
             Shirt("Green Buttoned Long Shirt", 4, (5, 25), Color.GREEN),
             Shirt("White Blouse", 4, (15, 35), Color.WHITE),
             Shirt("Black Sport T Shirt", 2, (15, 35), Color.BLACK),
             Shirt("White Sport T Shirt", 2, (15, 35), Color.WHITE),
             Shirt("Black Sport Top", 2, (15, 35), Color.BLACK),
             Shirt("White Sport Top", 2, (15, 35), Color.WHITE),
             Shirt("Black Tank Top", 2, (20, 35), Color.BLACK),
             Shirt("Blue Long Sleeve Sweat Shirt Cropped Top", 2, (0, 15),
                   Color.BLUE),
             Shirt("White Tank Top", 2, (20, 35), Color.WHITE),
             Shirt("White Short Pyjama", 1, (20, 35), Color.WHITE),
             Shirt("Black Short Pyjama", 1, (20, 35), Color.BLACK),
             Shirt("White Long Pyjama", 1, (0, 19), Color.WHITE),
             Shirt("Black Long Pyjama", 1, (0, 19), Color.BLACK),
             Shirt("Black Thermal Shirt", 1, (0, 12), Color.BLACK),
             Shirt("Black Nightdress Shirt", 1, (20, 35), Color.BLACK),
             Shirt("Blue Nightdress Shirt", 1, (20, 35), Color.BLUE),
             Shirt("Blue Casual T Shirt", 3, (12, 35), Color.BLUE),
             Shirt("Blue Jeans Tank Top", 3, (15, 35), Color.BLUE),
             Shirt("Orange Buttoned Short Shirt", 6, (20, 35), Color.ORANGE),
             Shirt("Yellow Sweater", 2, (0, 15), Color.YELLOW),
             Shirt("White Sweater", 2, (0, 15), Color.WHITE),
             Shirt("Black Sweater", 2, (0, 15), Color.BLACK),
             Shirt("White Hoodie", 2, (0, 20), Color.WHITE),
             Shirt("Black Hoodie", 2, (0, 20), Color.BLACK),
             Shirt("White Strapless", 2, (20, 35), Color.WHITE),
             Shirt("Black Strapless", 2, (20, 35), Color.BLACK),
             Shirt("Red Blazer", 5, (0, 20), Color.RED),
             Shirt("White Blazer", 5, (0, 20), Color.WHITE),
             Shirt("Pink Puffy Sleeve", 4, (20, 35), Color.PINK)]

DB_PANTS = [Pants("Black Long Jeans", 4, (0, 35), Color.BLACK),
            Pants("Blue Long Jeans", 4, (0, 35), Color.BLUE),
            Pants("Brown Tailored Pants", 5, (0, 25), Color.BROWN),
            Pants("White Tailored Pants", 5, (0, 25), Color.WHITE),
            Pants("Black Tailored Pants", 5, (0, 25), Color.BLACK),
            Pants("Gray Tights", 2, (0, 30), Color.GRAY),
            Pants("Black Tights", 2, (0, 30), Color.BLACK),
            Pants("White Short Skirt", 4, (18, 35), Color.WHITE),
            Pants("Black Short Skirt", 4, (18, 35), Color.BLACK),
            Pants("Yellow Business Casual Pants", 4, (0, 25), Color.YELLOW),
            Pants("Red Long PJ Pants", 1, (0, 13), Color.RED),
            Pants("Gray Long PJ Pants", 1, (0, 13), Color.GRAY),
            Pants("Black Nightdress Pants", 1, (20, 35), Color.BLACK),
            Pants("Blue Nightdress Pants", 1, (20, 35), Color.BLUE),
            Pants("Black Short PJ Pants", 1, (0, 13), Color.BLACK),
            Pants("Gray Short PJ Pants", 1, (0, 13), Color.GRAY),
            Pants("Red Tailored Pants", 4, (0, 30), Color.RED),
            Pants("Black Tailored Pants", 4, (0, 30), Color.BLACK),
            Pants("White Tailored Pants", 4, (0, 30), Color.WHITE),
            Pants("Blue Long loose pants", 2, (0, 20), Color.BLUE),
            Pants("Pink Paddlephone Pants", 3, (15, 30), Color.PINK),
            Pants("Blue Short Jeans", 4, (25, 35), Color.BLUE),
            Pants("Black Short sports pants", 2, (25, 35), Color.BLACK),
            Pants("White Short sports pants", 2, (25, 35), Color.WHITE)
            ]
