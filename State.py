# from constraint import *
from Constants import *
import Item


class State:
    def __init__(self, shirt_: Shirt, pants_: Pants, shoes_: Item.Shoes):
        self.shirt = shirt_
        self.pants = pants_
        self.shoes = shoes_

    def getShirt(self):
        return self.shirt

    def getPants(self):
        return self.pants

    def getShoes(self):
        return self.shoes

    def setShirt(self, new_shirt: Shirt):
        self.shirt = new_shirt

    def setPants(self, new_pants: Pants):
        self.pants = new_pants

    def setShoes(self, new_shoes: Item.Shoes):
        self.shoes = new_shoes

    def getState(self):
        return self.shirt, self.pants, self.shoes

    def is_state_terminal(self):
        return self.getShirt() is not None and self.getPants() is not None and self.getShoes() is not None

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
                if (self.getShoes() is None):
                    return "None#None#None"
                else:
                    return "None#" + "None#" + self.getShoes().__str__()
            elif (self.getShoes() is None):
                return "None#" + self.getPants().__str__() + "#None"
            else:
                return "None#" + self.getPants().__str__() + "#" + self.getShoes().__str__()
        elif (self.getPants() is None):
            if (self.getShoes() is None):
                return self.getShirt().__str__() + "#None" + "#None"
            else:
                return self.getShirt().__str__() + "#None" + "#" + self.getShoes().__str__()
        elif (self.getShoes() is None):
            return self.getShirt().__str__() + "#" + self.getPants().__str__() + "#None"
        else:
            return self.getShirt().__str__() + "#" + self.getPants().__str__() + "#" + self.getShoes().__str__()
