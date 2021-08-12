# from constraint import *
from Constants import *
import Item


class Good_Outfit:
    def __init__(self, shirt_, pants_):
        self.shirt = shirt_
        self.pants = pants_

    def get_shirt(self):
        return self.shirt

    def get_pants(self):
        return self.pants
