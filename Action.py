# from constraint import *
from Constants import *
import Item



class Action:
    def __init__(self,item_, wants_to_wear: bool):
        self.item = item_
        self.to_wear = wants_to_wear

    def get_item(self):
        return self.item

    def get_wants_to_wear(self):
        return self.to_wear

    def get_action(self):
        (int(self.get_wants_to_wear()),self.get_item())

    # def __eq__(self, other):
    #     if other==None:
    #         return False
    #     return (self.item==other.get_item() and self.to_wear==other.get_wants_to_wear())
    #
    # def __hash__(self):
    #     return id(self)

    def __str__(self):
        return self.get_item().__str__() + "#" + str(self.get_wants_to_wear())