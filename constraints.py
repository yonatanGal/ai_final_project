from constraint import *

if __name__ == '__main__':

    problem = Problem()
    problem.addVariable("top", [1,2,3])
    problem.addVariable("bottom", [4,5,6])
    print(problem.getSolutions())
