from constraint import *
from Constants import *
import Clothes


class Action:
    def __init__(self,item_ :Item, wants_to_wear: bool):
        self.item = item_
        self.to_wear = wants_to_wear

    def get_item(self):
        return self.item

    def get_wants_to_wear(self):
        return self.to_wear

