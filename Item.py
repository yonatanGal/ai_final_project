import numpy as np
import Constants as consts

FORMALITY_IDX = 0
TEMPERATURE_RANGE_IDX = 1
COLOR_IDX = 2
MIN_TEMPERATURE_IDX = 0
MAX_TEMPERATURE_IDX = 1


def create_item_from_np_array(name: str, array: np.array):
    """
    parser for items
    :param name:
    :param array:
    :return:
    """
    return Item(name, array[FORMALITY_IDX], array[TEMPERATURE_RANGE_IDX],
                array[COLOR_IDX])


class Item():
    """
    a class representing garments.
    """
    def __init__(self, name: str, formality: int, temperature_range: tuple,
                 color):
        self.name = name
        self.formality = formality
        self.temperature_range = temperature_range
        self.color = color

    def get_as_np_array(self):
        return np.asarray([self.formality, self.temperature_range, self.color],
                          dtype=object)

    def __str__(self):
        return "{0}: {1}, {2} - {3}, {4}".format(self.name, self.formality,
                                                 self.temperature_range[
                                                     MIN_TEMPERATURE_IDX],
                                                 self.temperature_range[
                                                     MAX_TEMPERATURE_IDX],
                                                 self.color)
    # getters
    def getTemperture(self):
        return self.temperature_range

    def getColor(self):
        return self.color

    def getFormality(self):
        return self.formality

    def getName(self):
        return self.name

class Shirt(Item):
    """
    a class representing shirts.
    """
    def __init__(self, name: str, formality: int, temperature_range: tuple,
                 color):
        super().__init__(name, formality, temperature_range, color)
        self.type = consts.SHIRT

    def __eq__(self, other):
        if other==None or other.name =="Unassigned":
            return False
        try:
            return (
                    self.name == other.getName() and self.formality == other.getFormality() and
                    self.temperature_range[0] == other.getTemperture()[0] and
                    self.temperature_range[1] == other.getTemperture()[
                        1] and self.color == other.getColor() and self.type == other.getType())
        except Exception as e:
            print("couldnt compare Unassigned Variable")

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return "{0},{1},({2},{3}),{4},{5}".format(self.name, self.formality,
                                                  self.temperature_range[0],
                                                  self.temperature_range[1],
                                                  self.color, self.type)

    def getType(self):
        return self.type


class Pants(Item):
    """
    a class representing pants.
    """
    def __init__(self, name: str, formality: int, temperature_range: tuple,
                 color):
        super().__init__(name, formality, temperature_range, color)
        self.type = consts.PANTS

    def __eq__(self, other):
        if other == None or other.name =="Unassigned":
            return False
        try:
            return (
                    self.name == other.getName() and self.formality == other.getFormality() and
                    self.temperature_range[0] == other.getTemperture()[0] and
                    self.temperature_range[1] == other.getTemperture()[
                        1] and self.color == other.getColor() and self.type == other.getType())
        except Exception as e:
            print("couldnt compare Unassigned Variable")

    def __hash__(self):
        return hash(self.__str__())

    def getType(self):
        return self.type

    def __str__(self):
        return "{0},{1},({2},{3}),{4},{5}".format(self.name, self.formality,
                                                  self.temperature_range[0],
                                                  self.temperature_range[1],
                                                  self.color, self.type)

class Shoes(Item):
    """
    a class representing shoes.
    """
    def __init__(self, name: str, formality: int, temperature_range: tuple,
                 color):
        super().__init__(name, formality, temperature_range, color)
        self.type = consts.SHOES

    def __eq__(self, other):
        if other == None or other.name =="Unassigned":
            return False
        try:
            return (
                    self.name == other.getName() and self.formality == other.getFormality() and
                    self.temperature_range[0] == other.getTemperture()[0] and
                    self.temperature_range[1] == other.getTemperture()[
                        1] and self.color == other.getColor() and self.type == other.getType())
        except Exception as e:
            print("couldnt compare Unassigned Variable")

    def __hash__(self):
        return hash(self.__str__())

    def getType(self):
        return self.type

    def __str__(self):
        return "{0},{1},({2},{3}),{4},{5}".format(self.name, self.formality,
                                                  self.temperature_range[0],
                                                  self.temperature_range[1],
                                                  self.color, self.type)

def filter_from_temperature(current_temperature, db):
    """
    Filters the garments that satisfies the temperature constraints.
    :param current_temperature: a number in the range [0,36)
    :param db: a data base of cloths.
    :return: the filtered garments.
    """
    filltered_db = []
    for item in db:
        if item.get_as_np_array()[TEMPERATURE_RANGE_IDX][
            MIN_TEMPERATURE_IDX] - 3 <= current_temperature <= \
                item.get_as_np_array()[
                    TEMPERATURE_RANGE_IDX][MAX_TEMPERATURE_IDX] + 3:
            filltered_db.append(item)
    return filltered_db


def filter_from_formality(current_formality, db):
    """
    Filters the garments that satisfies the formality constraints.
    :param current_formality: a number in the range [1,5].
    :param db: a data base of cloths.
    :return: the filtered garments.
    """
    filltered_db = []
    for item in db:
        if current_formality == item.getFormality():
            filltered_db.append(item)
    return filltered_db


def filter_db(temperturre_curr, formality_curr, db):
    """
    Filters the data base.
    :param temperturre_curr: a number in the range [0,36)
    :param formality_curr: a number in the range [1,5].
    :param db: a data base of cloths.
    :return: the filtered garments.
    """
    curr_db = filter_from_temperature(temperturre_curr, db)
    res_db = filter_from_formality(formality_curr, curr_db)
    return res_db
