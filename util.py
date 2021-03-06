# util.py
# -------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import sys
import inspect
import heapq, random
import numpy as np
from Action import Action
import State
import Constants


# For more information about the distance calculations see project report (p. 5-6)
def formalDistance(state1: State, state2: State):
    """
    Calculates the distance in the formality values.
    :param state1: State object.
    :param state2: State object.
    :return: distance calculated.
    """
    formal1_shirt = state1.getShirt()
    formal1_pants = state1.getPants()
    formal1_shoes = state1.getShoes()

    formal2_shirt = state2.getShirt()
    formal2_pants = state2.getPants()
    formal2_shoes = state2.getShoes()

    shirtsReward = 0
    pantsReward = 0
    shoesReward = 0

    if formal1_shirt:
        try:
            shirtsReward = 1 / float((
                                             formal1_shirt.getFormality() - formal2_shirt.getFormality()) ** 2)
        except ZeroDivisionError:
            shirtsReward = 5  # i want to increase reward when the formality is the same
    if formal1_pants:
        try:
            pantsReward = 1 / float((
                                            formal1_pants.getFormality() - formal2_pants.getFormality()) ** 2)
        except ZeroDivisionError:
            pantsReward = 5  # i want to increase reward when the formality is the same

    if formal1_shoes:
        try:
            shoesReward = 1 / float((
                                            formal1_shoes.getFormality() - formal2_shoes.getFormality()) ** 2)
        except ZeroDivisionError:
            shoesReward = 5  # i want to increase reward when the formality is the same

    return shirtsReward + pantsReward + shoesReward


def weatherDistance(state1: State, state2):
    """
    Calculates the distance in the weather values.
    :param state1: State object.
    :param state2: State object.
    :return: distance calculated.
    """
    shirts_distance = 0
    pants_distance = 0
    shoes_distance = 0

    if (state1.getShirt()):
        temp1_shirt_range = state1.getShirt().getTemperture()
        temp2_shirt_range = state2.getShirt().getTemperture()
        shirts_distance = itemWeatherDistance(temp1_shirt_range,
                                              temp2_shirt_range)
    if (state1.getPants()):
        temp1_pants_range = state1.getPants().getTemperture()
        temp2_pants_range = state2.getPants().getTemperture()
        pants_distance = itemWeatherDistance(temp1_pants_range,
                                             temp2_pants_range)
    if (state1.getShoes()):
        temp1_shoes_range = state1.getShoes().getTemperture()
        temp2_shoes_range = state2.getShoes().getTemperture()
        shoes_distance = itemWeatherDistance(temp1_shoes_range,
                                             temp2_shoes_range)

    return shirts_distance + pants_distance + shoes_distance


def itemWeatherDistance(temp1, temp2):
    """
    Calculates the distance in the weather values.
    :param temp1: a tuple representing the temperature range of the first item.
    :param temp2: a tuple representing the temperature range of the second item.
    :return: distance calculated.
    """
    temp1_set = set(np.arange(temp1[0], temp1[1] + 1))
    temp2_set = set(np.arange(temp2[0], temp2[1] + 1))
    size_temp1 = len(temp1_set)
    size_temp2 = len(temp2_set)
    intersection = temp1_set.intersection(temp2_set)
    if (intersection):
        sizeIntersection = len(intersection)
        minSize = min(size_temp1, size_temp2)
        return float(sizeIntersection) / minSize
    else:
        avgTemp1 = (temp1[0] + temp1[1]) / 2
        avgTemp2 = (temp2[0] + temp2[1]) / 2
    try:
        avgDiff = 1 / abs(float(avgTemp1) - avgTemp2)
    except ZeroDivisionError:
        avgDiff = 5  # i want to increase reward when the weather is the same
    return avgDiff


def colorDistanceWrapperLearning(state1, state2):
    """

    A wrapper for the color distance calculator.
    :param state1: State object.
    :param state2: State object.
    :return: distance calculated.
    """
    shirts_distance = 0
    pants_distance = 0
    shoes_distance = 0

    if (state1.getShirt()):
        shirt1_color = state1.getShirt().getColor()
        shirt2_color = state2.getShirt().getColor()
        shirts_distance = colors_distance_for_qLearning(shirt1_color,
                                                        shirt2_color)
    if (state1.getPants()):
        pants1_color = state1.getPants().getColor()
        pants2_color = state2.getPants().getColor()
        pants_distance = colors_distance_for_qLearning(pants1_color,
                                                       pants2_color)
    if (state1.getShoes()):
        shoes1_color = state1.getShoes().getColor()
        shoes2_color = state2.getShoes().getColor()
        shoes_distance = colors_distance_for_qLearning(shoes1_color,
                                                       shoes2_color)

    return shirts_distance + pants_distance + shoes_distance


def colors_distance_for_qLearning(color1, color2):
    """
    Calculates color distance for the q learning algorithm.
    :param color1: the first item color as a tuple of size 3 (R,G,B).
    :param color2: the second item color as a tuple of size 3 (R,G,B).
    :return: color distance as reward for the q learner.
    """
    (r1, g1, b1) = color1
    (r2, g2, b2) = color2
    try:
        colorDiff = 1 / float((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)
    except ZeroDivisionError:
        colorDiff = 5  # i want to increase reward when the color is the same
    return colorDiff


def colors_distance_for_cspSolver(color1, color2):
    """
    Calculates colors distance for the CSP Solver.
    :param color1: the first item color as a tuple of size 3 (R,G,B).
    :param color2: the second item color as a tuple of size 3 (R,G,B).
    :return: the colors distance.
    """
    (r1, g1, b1) = color1
    (r2, g2, b2) = color2
    return np.sqrt((r1 - r2) ^ 2 + (g1 - g2) ^ 2 + (b1 - b2) ^ 2)


def get_all_actions(db):
    """
    Returns all the possible actions regarding the given dataBase
    :param db: list of shirts and pants
    :return: list of all possible actions.
    """
    all_pos_actions = []
    for item in db:
        all_pos_actions.append(Action(item, False))
        all_pos_actions.append(Action(item, True))
    return all_pos_actions

class Counter(dict):
    """
    A counter keeps track of counts for a set of keys.

    The counter class is an extension of the standard python
    dictionary type.  It is specialized to have number values
    (integers or floats), and includes a handful of additional
    functions to ease the task of counting data.  In particular,
    all keys are defaulted to have value 0.  Using a dictionary:

    a = {}
    print(a['test'])

    would give an error, while the Counter class analogue:

    >>> a = Counter()
    >>> print(a['test'])
    0

    returns the default 0 value. Note that to reference a key
    that you know is contained in the counter,
    you can still use the dictionary syntax:

    >>> a = Counter()
    >>> a['test'] = 2
    >>> print(a['test'])
    2

    This is very useful for counting things without initializing their counts,
    see for example:

    >>> a['blah'] += 1
    >>> print(a['blah'])
    1

    The counter also includes additional functionality useful in implementing
    the classifiers for this assignment.  Two counters can be added,
    subtracted or multiplied together.  See below for details.  They can
    also be normalized and their total count and arg max can be extracted.
    """

    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)

    def incrementAll(self, keys, count):
        """
        Increments all elements of keys by the same count.

        >>> a = Counter()
        >>> a.incrementAll(['one','two', 'three'], 1)
        >>> a['one']
        1
        >>> a['two']
        1
        """
        for key in keys:
            self[key] += count

    def argMax(self):
        """
        Returns the key with the highest value.
        """
        if len(self.keys()) == 0: return None
        all = list(self.items())
        values = [x[1] for x in all]
        maxIndex = values.index(max(values))
        return all[maxIndex][0]

    def sortedKeys(self):
        """
        Returns a list of keys sorted by their values.  Keys
        with the highest values will appear first.

        >>> a = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> a['third'] = 1
        >>> a.sortedKeys()
        ['second', 'third', 'first']
        """
        sortedItems = list(self.items())
        sortedItems.sort(key=lambda item: -item[1])
        return [x[0] for x in sortedItems]

    def totalCount(self):
        """
        Returns the sum of counts for all keys.
        """
        return sum(self.values())

    def normalize(self):
        """
        Edits the counter such that the total count of all
        keys sums to 1.  The ratio of counts for all keys
        will remain the same. Note that normalizing an empty
        Counter will result in an error.
        """
        total = float(self.totalCount())
        if total == 0: return
        for key in self.keys():
            self[key] = self[key] / total

    def divideAll(self, divisor):
        """
        Divides all counts by divisor
        """
        divisor = float(divisor)
        for key in self:
            self[key] /= divisor

    def copy(self):
        """
        Returns a copy of the counter
        """
        return Counter(dict.copy(self))

    def __mul__(self, y):
        """
        Multiplying two counters gives the dot product of their vectors where
        each unique label is a vector element.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['second'] = 5
        >>> a['third'] = 1.5
        >>> a['fourth'] = 2.5
        >>> a * b
        14
        """
        sum = 0
        x = self
        if len(x) > len(y):
            x, y = y, x
        for key in x:
            if key not in y:
                continue
            sum += x[key] * y[key]
        return sum

    def __radd__(self, y):
        """
        Adding another counter to a counter increments the current counter
        by the values stored in the second counter.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> a += b
        >>> a['first']
        1
        """
        for key, value in y.items():
            self[key] += value

    def __add__(self, y):
        """
        Adding two counters gives a counter with the union of all keys and
        counts of the second added to counts of the first.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> (a + b)['first']
        1
        """
        addend = Counter()
        for key in self:
            if key in y:
                addend[key] = self[key] + y[key]
            else:
                addend[key] = self[key]
        for key in y:
            if key in self:
                continue
            addend[key] = y[key]
        return addend

    def __sub__(self, y):
        """
        Subtracting a counter from another gives a counter with the union of all keys and
        counts of the second subtracted from counts of the first.

        >>> a = Counter()
        >>> b = Counter()
        >>> a['first'] = -2
        >>> a['second'] = 4
        >>> b['first'] = 3
        >>> b['third'] = 1
        >>> (a - b)['first']
        -5
        """
        addend = Counter()
        for key in self:
            if key in y:
                addend[key] = self[key] - y[key]
            else:
                addend[key] = self[key]
        for key in y:
            if key in self:
                continue
            addend[key] = -1 * y[key]
        return addend


def getProbability(value, distribution, values):
    """
      Gives the probability of a value under a discrete distribution
      defined by (distributions, values).
    """
    total = 0.0
    for prob, val in zip(distribution, values):
        if val == value:
            total += prob
    return total


def flipCoin(p):
    r = random.random()
    return r < p
