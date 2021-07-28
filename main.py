from Clothes import *
from Constants import *
from CspSolver import *
import argparse


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--temperature", help="what is the temperature today?", default=10, type=int, choices=range(-5, 36))
    parser.add_argument("--formality", help="rate the formality of the occasion, between 1-10.", default=5, type=int, choices=range(1,11))

    args = parser.parse_args()
    temperature = args.temperature
    formality = args.formality

    res_db_shirts = filter_db(int(temperature), int(formality), db_shirts)
    res_db_pants = filter_db(int(temperature), int(formality), db_pants)

    problem = Problem()
    createCspSolver(problem,res_db_shirts,res_db_pants)

    # todo: if there is no solution, let the user know!
    # for shirt,pants in problem.getSolutions()
