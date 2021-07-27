from constraint import *
from Constants import *
import Clothes

def colorConstraints(cloth1,cloth2):

    return ((cloth1,cloth2) in UNMATCHINGCOLORS)



if __name__ == '__main__':
    ## example
    # problem = Problem()
    # problem.addVariable("top", [1,2,3])
    # problem.addVariable("bottom", [4,5,6])
    # print(problem.getSolutions())




    problem = Problem()
    all_shirts = []
    all_bottoms = []
    for shirt in Clothes.db_shirts.values():
        all_shirts.append(shirt)

    for bottom in Clothes.db_pants.values():
        all_bottoms.append(bottom)

    problem.addVariable("top", [all_shirts])
    problem.addVariable("bottom",[all_bottoms])

    # colors constraints
    for top in :
        for bottom in :
            problem.addConstraint()

