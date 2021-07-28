from constraint import *
from Constants import *
import Clothes


class State:
    def __init__(self, shirt_: Shirt, pants_: Pants):
        self.shirt = shirt_
        self.pants = pants_

    def get_shirt(self):
        return self.shirt

    def get_pants(self):
        return self.pants

    def set_shirt(self, new_shirt: Shirt):
        self.shirt = new_shirt

    def set_pants(self, new_pants: Pants):
        self.pants = new_pants

    def get_state(self):
        return self.shirt, self.pants

    def is_state_terminal(self):
        return self.getShirt() is not None and self.getPants() is not None


