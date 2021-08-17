# from constraint import *
from Constants import *
import Item
from util import *


def areColorsMatch(cloth1, cloth2):
    """
    This function is used in the csp "addConstraint" method. it checks if
    the pair of clothes are in a constraint.
    :param cloth1: Item object representing the first cloth.
    :param cloth2: Item object representing the second cloth.
    :return: True if the colors matches, False otherwise.
    """
    for color in  COLORS_LIST:
        if colors_distance_for_cspSolver(cloth1.color, color) <= THRESHOLD:
            for forbidden_color in UNMATCHINGCOLORS[color]:
                if  colors_distance_for_cspSolver(cloth2.color, forbidden_color) <= THRESHOLD:
                    return False
    return True

def createCspSolver(problem, db_shirts, db_pants,db_shoes):
    """
    Creates the CSP solver, sets the variables and adds the color constraints.
    :param problem: a CSP problem object.
    :param db_shirts: list of Shirts in the data base.
    :param db_pants: list of pants in the data base.
    :param db_shoes: list of shoes in the data base.
    """
    problem.addVariable("shirt", db_shirts)
    problem.addVariable("pants", db_pants)
    problem.addVariable("shoes", db_shoes)
    # colors constraints
    problem.addConstraint(areColorsMatch, ("shirt", "pants"))
    problem.addConstraint(areColorsMatch, ("shirt", "shoes"))
    problem.addConstraint(areColorsMatch, ("pants", "shoes"))


