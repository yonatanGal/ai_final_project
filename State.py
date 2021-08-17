# from constraint import *
from Constants import *
import Item


class State:
    """
    a class representing a state of the q learning agent.
    """
    def __init__(self, shirt_: Shirt, pants_: Pants, shoes_: Item.Shoes):
        self.shirt = shirt_
        self.pants = pants_
        self.shoes = shoes_

    # getters and setters
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
        """
        checks if the current state is a terminal state.
        :return: True if current state is a terminal state, False otherwise.
        """
        return self.getShirt() is not None and self.getPants() is not None and self.getShoes() is not None

    def __str__(self):
        """
        Parse the state into a string.
        :return: state in string representation.
        """
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

    def stateToResult(self):
        """
        Wrapper for printing the state.
        :return: string representation of the current state details.
        """
        try:
            shirt = "Shirt: " + self.getShirt().getName() + ", Temp: " + str(self.getShirt().getTemperture()) + "\n"
            pants = "Pants: " + self.getPants().getName() + ", Temp: " + str(self.getPants().getTemperture()) + "\n"
            shoes = "Shoes: " + self.getShoes().getName() + ", Temp: " + str(self.getShoes().getTemperture())
        except(AttributeError):
            return "Couldn't find a full outfit for you to wear."
        return shirt + pants + shoes



class CelebState(State):
    """
    a class representing garments of a trendy person (Celeb).
    """
    def __init__(self, shirt_: Shirt, pants_: Pants, shoes_: Item.Shoes,
                 celeb_: str):
        super().__init__(shirt_, pants_, shoes_)
        self.celeb = celeb_

    def getCeleb(self):
        return self.celeb

    def stateToResult(self):
        """
        Wrapper for printing the state.
        :return: string representation of the current state details.
        """
        celeb = self.getCeleb()
        shirt = "Shirt: " + self.getShirt().getName() + ", Temp: " + str(self.getShirt().getTemperture()) + "\n"
        pants = "Pants: " + self.getPants().getName() + ", Temp: " + str(self.getPants().getTemperture()) + "\n"
        shoes = "Shoes: " + self.getShoes().getName() + ", Temp: " + str(self.getShoes().getTemperture())
        return celeb +":\n" +shirt + pants + shoes

def filter_from_temperature(current_temperature, states):
    filltered_states = []
    for state in states:
        if (state.getShirt().getTemperture()[0] - 5 <= current_temperature <=
            state.getShirt().getTemperture()[1] + 5) and (
                state.getPants().getTemperture()[
                    0] - 5 <= current_temperature <=
                state.getPants().getTemperture()[1] + 5) and (
                state.getShoes().getTemperture()[
                    0] - 5 <= current_temperature <=
                state.getShoes().getTemperture()[1] + 5):
            filltered_states.append(state)
    return filltered_states
