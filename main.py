from Clothes import *
from Constants import *
from CspSolver import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temperature = input("What is the temperature today?")
    while not temperature.isdecimal() or not (-5 <= float(temperature) <= 35):
        temperature = input(
            "Should be a number between [-5,35], please try again")
    formality = input(
        "form 0 to 10 how much does this event demands formal dress:")
    while not formality.isdecimal() or not (0 <= float(formality) <= 10):
        formality = input(
            "input should be a number between 0-10, please try again")
    res_db_shirts = filter_db(int(temperature), int(formality), db_shirts)
    res_db_pants = filter_db(int(temperature), int(formality), db_pants)

    problem = Problem()
    createCspSolver(problem,res_db_shirts,res_db_pants)

    # todo: if there is no solution, let the user know!
    # for shirt,pants in problem.getSolutions()
