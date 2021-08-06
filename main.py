# from Item import *
from Constants import *
from CspSolver import *
import argparse
from Action import Action
import State
import Good_Outfit
import qLearningAgent






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--temperature", help="what is the temperature today?", default=10, type=int, choices=range(-5, 36))
    parser.add_argument("--formality", help="rate the formality of the occasion, between 1-10.", default=5, type=int, choices=range(1,11))

    args = parser.parse_args()
    temperature = args.temperature
    formality = args.formality

    res_db_shirts = filter_db(int(temperature), int(formality), db_shirts)
    res_db_pants = filter_db(int(temperature), int(formality), db_pants)

    problem = Problem()
    try:
        createCspSolver(problem,res_db_shirts,res_db_pants)
    except ValueError as e:
        print("Error! \n" + str(e))
        return
    solutions_dict = problem.getSolutions()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main()
    # db = db_pants + db_shirts
    goodOutfit = State.State(Shirt("button long shirt", 5, (5, 20), Color.GREEN),Pants("jeans_long", 5, (-5, 25), Color.BLACK))
    qLearner = qLearningAgent.QLearningAgent(db_shirts,db_pants,goodOutfit)
    qLearner.learn()
    s = State.State(None,None)
    while not qLearner.isTerminalState(s):
        action1 = qLearner.getPolicy(s)
        s = qLearner.apply_action(s,action1)

    a= 2
