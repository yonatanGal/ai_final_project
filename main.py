# from Item import *
from constraint import *
from Constants import *
from CspSolver import *
import argparse
from Action import Action
import State
import qLearningAgent
import time
import random

ITER_LIMIT = 300


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--algorithm",
                        help=f"choose algorithm to use: 1 - CSP + QLearning\n2 - CSP only with best match\n3 - CSP only with random choice",
                        default=1, type=int, choices=range(1, 4))
    parser.add_argument("--style",
                        help=f"choose a style: 1 - Home\n2 - Sport\n3 - Casual\n4 - Casual Elegant\n5 - Formal",
                        default=5, type=int, choices=range(1, 6))
    parser.add_argument("--temperature", help="what is the temperature today?",
                        default=7, type=int, choices=range(0, 36))
    args = parser.parse_args()

    alg = args.algorithm
    temperature = args.temperature
    style = args.style
    return alg, style, temperature


def findSolutions(problem, type=2):
    """
    Finds all the CSP solutions and creates tuples of every pair
    in every solution triple.
    :param problem: CSP Problem object.
    :param type: the type of algorithm for solving the problem.
    :return: all possible solutions list.
    """
    solutions_dictionary_list = problem.getSolutions()
    if (type == CSP_AND_QLEARNING):
        shirtAndPantsTuples = []
        shirtAndShoesTuples = []
        pantsAndShoesTuples = []
        for sol in solutions_dictionary_list:
            shirtAndPantsTuples.append({sol['shirt'], sol['pants']})
            shirtAndShoesTuples.append({sol['shirt'], sol['shoes']})
            pantsAndShoesTuples.append({sol['pants'], sol['shoes']})
        solutions_list = shirtAndPantsTuples + shirtAndShoesTuples + pantsAndShoesTuples
    else:
        solutions_list = []
        for sol in solutions_dictionary_list:
            solutions_list.append(
                State.State(sol['shirt'], sol['pants'], sol['shoes']))
    return solutions_list


def learnAndPredict(db_shirts, db_pants, db_shoes, possibleSolutions,
                    goodOutfit):
    """
    Creates and trains a qLearning agent to suggest an outfit that is:
    1. One of the possibleSolutions extracted from the CSP solver
    2. As close as it can to the trendy (celeb) outfit (goodOutfit)

    :param db_shirts: list of shirts.
    :param db_pants: list of pants.
    :param db_shoes: list of shoes.
    :param possibleSolutions: list of all solutions given by the CSP Solver.
    :param goodOutfit: the trendy outfit.
    :return: the resulted state.
    """
    qLearner = qLearningAgent.QLearningAgent(db_shirts, db_pants, db_shoes,
                                             possibleSolutions, goodOutfit)
    qLearner.learn()
    end_learning_time = time.time()
    s = State.State(None, None, None)
    counter = 0
    while not qLearner.isTerminalState(s) and counter < ITER_LIMIT:
        action1 = qLearner.getPolicy(s)
        if (not action1 is None):
            s = qLearner.apply_action(s, action1)
        counter += 1

    return s,end_learning_time


def findCspBestSolution(goodOutfits, solution_list):
    """
    Finds the CSP solution that is the closest one to the trendy outfits.
    :param goodOutfits: trendy outfits states.
    :param solution_list: list of possible CSP solutions.
    :return: best solution details, the closest trendy outfit details, award accordingly.
    """
    bestSolution = State.State(None, None, None)
    celeb = None
    maxReward = -np.inf
    for outfit in goodOutfits:
        for sol in solution_list:
            formalityReward = formalDistance(sol, outfit)
            weatherReward = weatherDistance(sol, outfit)
            color_Reward = colorDistanceWrapperLearning(sol, outfit)
            sum = formalityReward + weatherReward + color_Reward
            if (sum > maxReward):
                maxReward = sum
                bestSolution = sol
                celeb = outfit
    return bestSolution, celeb, maxReward


def main():
    alg, style, temperature = parseArgs()

    # filter the outfits that meet the temperature and the style the user has chosen
    res_db_shirts = Item.filter_db(int(temperature), style, DB_SHIRTS)
    res_db_pants = Item.filter_db(int(temperature), style, DB_PANTS)
    res_db_shoes = Item.filter_db(int(temperature), style, DB_SHOES)
    # solve the csp problem to get all possible solutions that fulfill the constraints and the user needs
    problem = Problem()
    try:
        createCspSolver(problem, res_db_shirts, res_db_pants, res_db_shoes)
    except ValueError as e:
        print(
            "you haven't got any outfit that fits the current constraints! Go and get some cloths!")
        return
    if (problem.getSolutions() is None):
        print(
            "you haven't got any outfit that fits the current constraints! Go and get some cloths!")
        return

    goodOutfits = State.filter_from_temperature(temperature, STYLES[style])

    print(f'style - {style}, temperature - {temperature} , algorithm - {alg}')
    startTime = time.time()
    if (alg == CSP_AND_QLEARNING):
        solutions_list = findSolutions(problem, CSP_AND_QLEARNING)
        # train the qLearner and suggest a solution meeting all constraints and as close as it can to the "good" outfit
        finalState,end_learning_time = learnAndPredict(DB_SHIRTS, DB_PANTS, DB_SHOES,
                                     solutions_list,
                                     goodOutfits)

        endTime = time.time()
        s, closest_celeb, matchScore = findCspBestSolution(goodOutfits,
                                                           [finalState])

        if (s.getShirt() and s.getPants() and s.getShoes()):
            print(finalState.stateToResult() + "\n Learning Running Time: " + str(end_learning_time - startTime) +"sec\n Predictiong Running Time: "+ str(endTime-end_learning_time) + " sec")
            print(f'matchScore: {matchScore}\nThis outfit is closer to {closest_celeb.stateToResult()}')
        else:
            print("Qlearner couldn't find a solution!")
    elif (alg == CSP_ONLY_BEST_MATCH):
        solutions_list = findSolutions(problem, CSP_ONLY_BEST_MATCH)
        finalState, closest_celeb, matchScore = findCspBestSolution(goodOutfits,
                                                                 solutions_list)
        if (closest_celeb):
            endTime = time.time()
            print(
                "Based on the given parameters, This is our best recommendation: \n " + finalState.stateToResult() + "\n Running Time: " + str(
                    endTime - startTime) +" sec")
            print(
                f'matchScore: {matchScore}\nThis outfit is as close as you can get to {closest_celeb.stateToResult()}')
        else:
            print(
                "There is no celeb outfit that fits your closet. What is wrong with you?")
    elif (alg == CSP_ONLY_RANDOM_CHOICE):
        solutions_list = findSolutions(problem, CSP_ONLY_RANDOM_CHOICE)
        if (solutions_list != []):
            finalState = random.choice(solutions_list)
            endTime=time.time()
            s, closest_celeb, matchScore = findCspBestSolution(goodOutfits,
                                                               [finalState])
            print("Based on the given parameters, This is our random recommendation: \n" + finalState.stateToResult() + "\n Running time: " + str(
                    endTime - startTime) + " sec")
            print(
                f'matchScore: {matchScore}\nThis outfit is as close as you can get to {closest_celeb.stateToResult()}')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

