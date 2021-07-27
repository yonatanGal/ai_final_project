import numpy as np

colors = {"black", "white", "grey", "blue", "yellow", "red", "green", "orange", "brown", "pink", "purple"}
FORMALITY_IDX = 0
TEMPERATURE_RANGE_IDX = 1
COLOR_IDX = 2
MIN_TEMPERATURE_IDX = 0
MAX_TEMPERATURE_IDX = 1


def create_item_from_np_array(name: str, array: np.array):
	return Item(name, array[FORMALITY_IDX], array[TEMPERATURE_RANGE_IDX], array[COLOR_IDX])


class Item:
	def __init__(self, name: str, formality: int, temperature_range: tuple, color: str):
		self.name = name
		self.formality = formality
		self.temperature_range = temperature_range
		self.color = color

	def get_as_np_array(self):
		return np.array([self.formality, self.temperature_range, self.color])

	def __str__(self):
		return "{0}: {1}, {2} - {3}, {4}".format(self.name, self.formality, self.temperature_range[
			MIN_TEMPERATURE_IDX], self.temperature_range[ MAX_TEMPERATURE_IDX], self.color)


class Shirt(Item):
	def __init__(self, name: str, formality: int, temperature_range: tuple,
				 color: str):
		super().__init__(name, formality, temperature_range, color)
		self.type = "Shirt"


class Pants(Item):
	def __init__(self, name: str, formality: int, temperature_range: tuple,
				 color: str):
		super().__init__(name, formality, temperature_range, color)
		self.type = "Pants"


db_shirts = {Shirt("my_black_T_shirt", 3, (18, 30), "black"),
			 Shirt("button long shirt", 5, (5, 20), "green"),
			 Shirt("blouse", 7, (15, 35), "white"),
			 Shirt("sport_tshirt", 1, (15, 40), "blue"),
			 Shirt("pyjama", 0, (12, 22), "pink"),
			 Shirt("thermal shirt", 3, (-5, 12), "black")}

db_pants = {Pants("jeans_long", 5, (-5, 25), "black"),
			Pants("tailored pants", 9, (-5, 25), "brown"),
			Pants("tights", 2, (2, 27), "grey"),
			Pants("short skirt", 7, (18, 35), "white"),
			Pants("buissnes casual pants", 6, (10, 30), "yellow"),
			Pants("thermal pants", 3, (-5, 13), "orange")}


def filter_from_temperature(current_temperature, db):
	filltered_db = {}
	for key in db.keys():
		if db[key][TEMPERATURE_RANGE_IDX][MIN_TEMPERATURE_IDX] - 5 <= current_temperature <= db[key][
			TEMPERATURE_RANGE_IDX][MAX_TEMPERATURE_IDX] + 5:
			filltered_db[key] = db[key]
	return filltered_db


def filter_from_formality(current_formality, db):
	filltered_db = {}
	for key in db.keys():
		if current_formality - 1 <= db[key][FORMALITY_IDX] <= current_formality + 1:
			filltered_db[key] = db[key]
	return filltered_db
