import numpy as np
import Constants
# colors = {"black", "white", "grey", "blue", "yellow", "red", "green", "orange", "brown", "pink", "purple"}
FORMALITY_IDX = 0
TEMPERATURE_RANGE_IDX = 1
COLOR_IDX = 2
MIN_TEMPERATURE_IDX = 0
MAX_TEMPERATURE_IDX = 1


def create_item_from_np_array(name: str, array: np.array):
	return Item(name, array[FORMALITY_IDX], array[TEMPERATURE_RANGE_IDX], array[COLOR_IDX])


class Item:
	def __init__(self, name: str, formality: int, temperature_range: tuple, color):
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
				 color):
		super().__init__(name, formality, temperature_range, color)
		self.type = "Shirt"


class Pants(Item):
	def __init__(self, name: str, formality: int, temperature_range: tuple,
				 color):
		super().__init__(name, formality, temperature_range, color)
		self.type = "Pants"


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

def filter_db(temperturre_curr, formality_curr,db):
	curr_db = filter_from_temperature(temperturre_curr,db)
	res_db = filter_from_formality(formality_curr,curr_db)
	return res_db


if __name__ == '__main__':
	temperature = input("What is the temperature today?")
	while not temperature.isdecimal() or not (-5<=float(temperature)<=35):
			temperature = input("Should be a number between [-5,35], please try again")
	formality = input("form 0 to 10 how much does this event demands formal dress:")
	while not formality.isdecimal() or not (0<=float(formality)<=10):
		formality = input("input should be a number between 0-10, please try again")

	res_db = filter_db(temperature,formality,db_shirts)
