# from constraint import *
from Constants import *
import Item



class Action:
    """
    a class representing an Action.
    """
    def __init__(self,item_, wants_to_wear: bool):
        self.item = item_
        self.to_wear = wants_to_wear

    def get_item(self):
        return self.item

    def get_wants_to_wear(self):
        return self.to_wear

    def get_action(self):
        (int(self.get_wants_to_wear()),self.get_item())


    def __str__(self):
        return self.get_item().__str__() + "#" + str(self.get_wants_to_wear())