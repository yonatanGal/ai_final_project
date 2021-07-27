from enum import Enum


class color(Enum):
    BLUE = 'blue'
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    BROWN = 'brown'
    ORANGE = 'orange'
    PINK = 'pink'
    PURPLE = 'purple'
    GRAY = 'gray'


UNMATCHINGCOLORS = {{color.BLUE, color.RED},
                    {color.BLUE, color.YELLOW},
                    {color.BLUE, color.GREEN},
                    {color.BLUE, color.BROWN},
                    {color.BLUE, color.ORANGE},
                    {color.BLUE, color.PINK},
                    {color.BLUE, color.PURPLE},

                    {color.RED, color.YELLOW},
                    {color.RED, color.GREEN},
                    {color.RED, color.BROWN},
                    {color.RED, color.ORANGE},
                    {color.RED, color.PINK},
                    {color.RED, color.PURPLE},

                    {color.YELLOW, color.GREEN},
                    {color.YELLOW, color.ORANGE},
                    {color.YELLOW, color.BROWN},
                    {color.YELLOW, color.PINK},
                    {color.YELLOW, color.PURPLE},

                    {color.GREEN, color.BROWN},
                    {color.GREEN, color.ORANGE},
                    {color.GREEN, color.PINK},
                    {color.GREEN, color.PURPLE},

                    {color.BROWN, color.ORANGE},
                    {color.BROWN, color.PINK},
                    {color.BROWN, color.PURPLE},

                    {color.ORANGE, color.PINK},
                    {color.ORANGE, color.PURPLE},
                    {color.PINK, color.PURPLE},

                    {color.BLUE, color.BLUE},
                    {color.ORANGE, color.ORANGE},
                    {color.RED, color.RED},
                    {color.YELLOW, color.YELLOW},
                    {color.GREEN, color.GREEN},
                    {color.BROWN, color.BROWN},
                    {color.PINK, color.PINK},
                    {color.PURPLE, color.PURPLE},
                    {color.GRAY,color.GRAY}
                    }
