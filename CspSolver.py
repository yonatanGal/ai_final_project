from constraint import *
from Constants import *
import Clothes


def areColorsMatch(cloth1, cloth2):
    return not ((cloth1.color, cloth2.color) in UNMATCHINGCOLORS or (
    cloth2.color, cloth1.color) in UNMATCHINGCOLORS)

def createCspSolver(problem,db_shirts,db_pants):
    problem.addVariable("top", db_shirts)
    problem.addVariable("bottom", db_pants)

    # colors constraints
    problem.addConstraint(areColorsMatch, ("top", "bottom"))
    for top in db_shirts:
        for bottom in db_pants:
            problem.addConstraint(areColorsMatch, ("top", "bottom"))



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
