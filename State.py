from constraint import *
from Constants import *
import Item


class State:
    def __init__(self, shirt_: Shirt, pants_: Pants):
        self.shirt = shirt_
        self.pants = pants_

    def getShirt(self):
        return self.shirt

    def getPants(self):
        return self.pants

    def setShirt(self, new_shirt: Shirt):
        self.shirt = new_shirt

    def setPants(self, new_pants: Pants):
        self.pants = new_pants

    def getState(self):
        return self.shirt, self.pants

    def is_state_terminal(self):
        return self.getShirt() is not None and self.getPants() is not None

    # def __eq__(self, other):
    #     if (other == None):
    #         return False
    #     return (
    #             self.getShirt() == other.getShirt() and self.getPants() == other.getPants())
    #
    # def __hash__(self):
    #     return id(self)

    def __str__(self):
        if (self.getShirt() is None):
            if (self.getPants() is None):
                return "None#None"
            else:
                return "None#" + self.getPants().__str__()
        elif (self.getPants() is None):
            return self.getShirt().__str__() + "#None"
        else:
            return self.getShirt().__str__() + "#" + self.getPants().__str__()

