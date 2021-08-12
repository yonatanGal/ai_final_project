# from Item import *
from constraint import *
from Constants import *
from CspSolver import *
import argparse
from Action import Action
import State
import Good_Outfit
import qLearningAgent


def learnAndPredict(db_shirts, db_pants, db_shoes, possibleSolutions,
                    goodOutfit):
    """
    create and train a qLearning agent to suggest an outfit that is:
    1. in the possibleSolutions extracted from the CSP solver
    2. as close as it can to the celeb outfit (goodOutfit)

    :param db_shirts:
    :param db_pants:
    :param possibleSolutions:
    :param goodOutfit:
    :return:
    """
    qLearner = qLearningAgent.QLearningAgent(db_shirts, db_pants, db_shoes,
                                             possibleSolutions, goodOutfit)
    qLearner.learn()
    s = State.State(None, None, None)
    while not qLearner.isTerminalState(s):
        action1 = qLearner.getPolicy(s)
        if (not action1 is None):
            s = qLearner.apply_action(s, action1)
    return s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--style",
                        help=f"choose a style: 1 - Home\n2 - Sport\n3 - Casual\n4 - Casual Elegant\n5 - Formal",
                        default=5, type=int, choices=range(1, 6))
    parser.add_argument("--temperature", help="what is the temperature today?",
                        default=18, type=int, choices=range(0, 36))
    # parser.add_argument("--dressLike",
    #                     help=f"Like who would like to dress today? {CELEBS.keys()}",
    #                     default="Noa Kirel", type=str, choices=CELEBS.keys())

    args = parser.parse_args()
    temperature = args.temperature
    style = args.style
    # style = 2 # todo: delete after debug
    # dressLike = args.dressLike

    # filter the outfits that meet the temperature and the stle the user has chosen

    res_db_shirts = Item.filter_db(int(temperature), style, db_shirts)
    res_db_pants = Item.filter_db(int(temperature), style, db_pants)
    res_db_shoes = Item.filter_db(int(temperature), style, db_shoes)
    # solve the csp problem to get all possible solutions that fulfill the constraints and the user needs
    problem = Problem()
    try:
        createCspSolver(problem, res_db_shirts, res_db_pants, res_db_shoes)
    except ValueError as e:
        print("Error! \n" + str(e))
        return
    if (problem.getSolutions() is None):
        print("you haven't got any outfit that fits the current constraints")
        return
    solutions_list = findSolutions(problem)

    # goodOutfit  = CELEBS[dressLike]

    goodOutfits = State.filter_from_temperature(temperature,STYLES[style])
    # train the qLearner and suggest a solution meeting all constraints and as close as it can to the "good" outfit
    finalState = learnAndPredict(res_db_shirts, res_db_pants, res_db_shoes,
                                 solutions_list,
                                 goodOutfits)
    print(finalState)


def findSolutions(problem):
    solutions_dictionary_list = problem.getSolutions()
    shirtAndPantsTuples = []
    shirtAndShoesTuples = []
    pantsAndShoesTuples = []
    for sol in solutions_dictionary_list:
        # solutions_list.append((sol['shirt'], sol['pants']))
        shirtAndPantsTuples.append({sol['shirt'], sol['pants']})
        shirtAndShoesTuples.append({sol['shirt'], sol['shoes']})
        pantsAndShoesTuples.append({sol['pants'], sol['shoes']})
    solutions_list = shirtAndPantsTuples + shirtAndShoesTuples + pantsAndShoesTuples
    return solutions_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
