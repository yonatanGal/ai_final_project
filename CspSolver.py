from constraint import *
from Constants import *
import Item
from util import *


def areColorsMatch(cloth1, cloth2):
    """
    this function is used in the csp "addConstraint" method. it checks if
    the pair of clothes are in a constraint
    :param cloth1:
    :param cloth2:
    :return:
    """
    for color in  color_lst:
        if colors_distance_for_cspSolver(cloth1.color, color) <= THRESHOLD:
            for forbidden_color in UNMATCHINGCOLORS[color]:
                if  colors_distance_for_cspSolver(cloth2.color, forbidden_color) <= THRESHOLD:
                    return False
    return True

def createCspSolver(problem, db_shirts, db_pants):

    problem.addVariable("shirt", db_shirts)
    problem.addVariable("pants", db_pants)
    # colors constraints
    problem.addConstraint(areColorsMatch, ("shirt", "pants"))


## example
# problem = Problem()
# problem.addVariable("top", [1,2,3])
# problem.addVariable("bottom", [4,5,6])
# print(problem.getSolutions())

# problem = Problem()
# all_shirts = []
# all_bottoms = []
# for shirt in db_shirts:
#     all_shirts.append(shirt)
#
# for bottom in db_pants:
#     all_bottoms.append(bottom)
#
# problem.addVariable("top", all_shirts)
# problem.addVariable("bottom", all_bottoms)
#
# # colors constraints
# for top in db_shirts:
#     for bottom in db_pants:
#         problem.addConstraint(areColorsMatch, ("top", "bottom"))
#
# print(problem.getSolutions())
