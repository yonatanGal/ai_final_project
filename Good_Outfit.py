from constraint import *
from Constants import *
import Clothes


class Good_Outfit:
    def __init__(self, shirt_: Shirt, pants_: Pants):
        self.shirt = shirt_
        self.pants = pants_

    def get_shirt(self):
        return self.shirt

    def get_pants(self):
        return self.pants
