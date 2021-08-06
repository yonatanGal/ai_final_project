# from Item import *
from Constants import *
from CspSolver import *
import argparse
from Action import Action
import State
import Good_Outfit
import qLearningAgent

def learnAndPredict(db_shirts, db_pants, possibleSolutions, goodOutfit):
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
    qLearner = qLearningAgent.QLearningAgent(db_shirts, db_pants,
                                             possibleSolutions, goodOutfit)
    qLearner.learn()
    s = State.State(None, None)
    while not qLearner.isTerminalState(s):
        action1 = qLearner.getPolicy(s)
        s = qLearner.apply_action(s, action1)
    return s

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--temperature", help="what is the temperature today?",
                        default=10, type=int, choices=range(-5, 36))
    parser.add_argument("--formality",
                        help="rate the formality of the occasion, between 1-10.",
                        default=5, type=int, choices=range(1, 11))

    args = parser.parse_args()
    temperature = args.temperature
    formality = args.formality

    # filter the outfits that meet the temperature and the formality the user has chosen
    res_db_shirts = Item.filter_db(int(temperature), int(formality), db_shirts)
    res_db_pants = Item.filter_db(int(temperature), int(formality), db_pants)

    # solve the csp problem to get all possible solutions that fulfill the constraints and the user needs
    problem = Problem()
    try:
        createCspSolver(problem, res_db_shirts, res_db_pants)
    except ValueError as e:
        print("Error! \n" + str(e))
        return
    solutions_dictionary_list = problem.getSolutions()
    solutions_list = []
    for sol in solutions_dictionary_list:
        solutions_list.append((sol['shirt'], sol['pants']))

    # an example for a good out fit to dress like
    goodOutfit = State.State(
        Shirt("kind of long shirt", 3, (5, 20), Color.GREEN),
        Pants("jeans_long", 5, (-5, 25), Color.BLACK))
    # train the qLearner and suggest a solution meeting all constraints and as close as it can to the "good" outfit
    finalState = learnAndPredict(res_db_shirts, res_db_pants, solutions_list,
                                 goodOutfit)
    print(finalState)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
