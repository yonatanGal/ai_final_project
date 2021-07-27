from enum import Enum
from Clothes import *


class Color(Enum):
    BLUE = 'blue'
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    BROWN = 'brown'
    ORANGE = 'orange'
    PINK = 'pink'
    PURPLE = 'purple'
    GRAY = 'gray'
    BLACK = 'black'
    WHITE = 'white'


UNMATCHINGCOLORS = {(Color.BLUE, Color.RED),
                    (Color.BLUE, Color.YELLOW),
                    (Color.BLUE, Color.GREEN),
                    (Color.BLUE, Color.BROWN),
                    (Color.BLUE, Color.ORANGE),
                    (Color.BLUE, Color.PINK),
                    (Color.BLUE, Color.PURPLE),

                    (Color.RED, Color.YELLOW),
                    (Color.RED, Color.GREEN),
                    (Color.RED, Color.BROWN),
                    (Color.RED, Color.ORANGE),
                    (Color.RED, Color.PINK),
                    (Color.RED, Color.PURPLE),

                    (Color.YELLOW, Color.GREEN),
                    (Color.YELLOW, Color.ORANGE),
                    (Color.YELLOW, Color.BROWN),
                    (Color.YELLOW, Color.PINK),
                    (Color.YELLOW, Color.PURPLE),

                    (Color.GREEN, Color.BROWN),
                    (Color.GREEN, Color.ORANGE),
                    (Color.GREEN, Color.PINK),
                    (Color.GREEN, Color.PURPLE),

                    (Color.BROWN, Color.ORANGE),
                    (Color.BROWN, Color.PINK),
                    (Color.BROWN, Color.PURPLE),
                    (Color.BROWN, Color.BLACK),

                    (Color.ORANGE, Color.PINK),
                    (Color.ORANGE, Color.PURPLE),
                    (Color.PINK, Color.PURPLE),

                    (Color.BLUE, Color.BLUE),
                    (Color.ORANGE, Color.ORANGE),
                    (Color.RED, Color.RED),
                    (Color.YELLOW, Color.YELLOW),
                    (Color.GREEN, Color.GREEN),
                    (Color.BROWN, Color.BROWN),
                    (Color.PINK, Color.PINK),
                    (Color.PURPLE, Color.PURPLE),
                    (Color.GRAY, Color.GRAY)
                    }

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
