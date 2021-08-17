import util
import random
import Constants as consts
import numpy as np
import State
import copy


class QLearningAgent():
    """
    Q learning agent.

    self.goodOutFits is a list of State objects representing the contemporary
    trends.
    self.possibleSolutions is a list of terminal states that are solution
    for the csp problem.
    """

    def __init__(self, db_shirts, db_pants, db_shoes, possibleSolutions,
                 goodOutFits: list, gamma=0.8, learningRate=1, epsilon=0.3,
                 numTraining=100):

        self.qValue = util.Counter()
        self.learningRate = float(learningRate)
        self.epsilon = float(epsilon)
        self.discount = float(gamma)
        self.numTraining = int(numTraining)
        self.allActions = util.get_all_actions(db_shirts + db_pants + db_shoes)
        self.goodOutFits = goodOutFits
        self.possibleSolutions = possibleSolutions

    def isTerminalState(self, state):
        """
        a state is a terminal state if all its 3 fields are filled.
        :param state: state representing the current appearance.
        :return: true if state is terminal state, false otherwise.
        """
        if (state.getShirt() and state.getPants() and state.getShoes()):
            return True
        return False

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we never seen
          a state or (state,action) tuple
        """
        key = self.stateActionToKey(state, action)
        return self.qValue[key]

    def getValue(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.
        """
        actions = self.getLegalActions(state)
        if not actions:
            return 1  # because the only state where you have no legal action to make is a terminal state
        maxAction = self.findMaxAction(actions, state)

        return self.getQValue(state, maxAction)

    def getPolicy(self, state):
        """
          Computes the best action to take in a state.
          if there is no legal action it returns None.
        """
        actions = self.getLegalActions(state)
        if (not actions):
            return None
        # maxAction = max(actions, key=lambda a: self.getQValue(state, a))
        maxAction = self.findMaxAction(actions, state)
        return maxAction

    def getLegalActions(self, state):
        """
        find all the legal actions the agent can take in a given state.
        :param state: State object.
        :return: a list of all the legal actions.
        """
        shirt = state.getState()[0]
        pants = state.getState()[1]
        shoes = state.getState()[2]

        legalActions = []
        if (shirt is None):
            if (pants is None):
                if (shoes is None):
                    for action in self.allActions:
                        if action.get_wants_to_wear():
                            legalActions.append(action)
                else:
                    # get all shirts putting, pants putting and one shoes removing
                    for action in self.allActions:
                        if action.get_item().getType() == consts.SHIRT and action.get_wants_to_wear() and {
                            action.get_item(),
                            shoes} in self.possibleSolutions:
                            legalActions.append(action)

                        elif action.get_item().getType() == consts.PANTS and action.get_wants_to_wear() and {
                            action.get_item(),
                            shoes} in self.possibleSolutions:
                            legalActions.append(action)
                        elif (
                                action.get_item() == shoes and not action.get_wants_to_wear()):
                            legalActions.append(action)
            elif (shoes is None):
                # get all shirts putting, one pants removing and all shoes putting
                for action in self.allActions:
                    if action.get_item().getType() == consts.SHIRT and action.get_wants_to_wear() and {
                        action.get_item(),
                        pants} in self.possibleSolutions:
                        legalActions.append(action)
                    elif (
                            action.get_item().getType() == consts.SHOES and action.get_wants_to_wear() and {
                        action.get_item(),
                        pants} in self.possibleSolutions):
                        legalActions.append(action)
                    elif (
                            action.get_item() == pants and not action.get_wants_to_wear()):
                        legalActions.append(action)
            else:
                # get all shirts putting, one pants removing and one shoes removing
                for action in self.allActions:
                    if (
                            action.get_item().getType == consts.SHIRT and action.get_wants_to_wear() and {
                        action.get_item(),
                        pants} in self.possibleSolutions and {
                        action.get_item(),
                        shoes} in self.possibleSolutions):
                        legalActions.append(action)
                    elif (
                            action.get_item() == shoes and not action.get_wants_to_wear()):
                        legalActions.append(action)

        elif (pants is None):
            if (shoes is None):
                # get one shirt removing, all pants putting and all shoes putting
                for action in self.allActions:
                    if (
                            action.get_item().getType() == consts.PANTS and action.get_wants_to_wear() and {
                        action.get_item(), shirt} in self.possibleSolutions):
                        legalActions.append(action)
                    elif (
                            action.get_item().getType() == consts.SHOES and action.get_wants_to_wear() and {
                        action.get_item(), shirt} in self.possibleSolutions):
                        legalActions.append(action)
                    elif (
                            action.get_item() == shirt and not action.get_wants_to_wear()):
                        legalActions.append(action)
            else:
                # get one shirt removing, all pants putting and one shoes removing
                for action in self.allActions:
                    if (
                            action.get_item().getType() == consts.PANTS and action.get_wants_to_wear() and {
                        action.get_item(),
                        shirt} in self.possibleSolutions and {
                        action.get_item(), shoes} in self.possibleSolutions):
                        legalActions.append(action)
                    elif (
                            action.get_item() == shirt and not action.get_wants_to_wear()):
                        legalActions.append(action)
                    elif (
                            action.get_item() == shoes and not action.get_wants_to_wear()):
                        legalActions.append(action)
        elif (shoes is None):
            # get one shirt removing, one pants removing and all shoes putting
            for action in self.allActions:
                if (
                        action.get_item().getType() == consts.SHOES and action.get_wants_to_wear() and {
                    action.get_item(), shirt} in self.possibleSolutions and {
                    action.get_item(), pants} in self.possibleSolutions):
                    legalActions.append(action)
                elif (
                        action.get_item() == shirt and not action.get_wants_to_wear()):
                    legalActions.append(action)
                elif (
                        action.get_item() == pants and not action.get_wants_to_wear()):
                    legalActions.append(action)
        else:
            # get one shirt removing, one pants removing and one shoes re
            for action in self.allActions:
                if action.get_item() == pants and not action.get_wants_to_wear():
                    legalActions.append(action)
                elif action.get_item() == shirt and not action.get_wants_to_wear():
                    legalActions.append(action)
                elif (
                        action.get_item() == shoes and not action.get_wants_to_wear()):
                    legalActions.append(action)

        return legalActions

    def getReward(self, state, goodOutfits, action):
        """
        Computes the reward of the pair (state,action).
        :param state: State object.
        :param goodOutfits: list of states.
        :param action: Action object.
        :return: The reward.
        """
        if (not action.get_wants_to_wear()):
            return -10
        maxReward = self.findMaxReward(goodOutfits, state)
        return maxReward

    def findMaxReward(self, goodOutfits, state):
        maxReward = -np.inf
        for outfit in goodOutfits:
            formalityReward = util.formalDistance(state, outfit)
            weatherDistance = util.weatherDistance(state, outfit)
            color_Distance = util.colorDistanceWrapperLearning(state, outfit)
            sum = formalityReward + weatherDistance + color_Distance
            if (sum > maxReward):
                maxReward = sum
        return maxReward

    def apply_action(self, state, action):
        """
        makes an action in the current state.
        :param state: State object.
        :param action: Action object.
        :return: The new state.
        """
        isWear = action.get_wants_to_wear()
        itemType = action.get_item().getType()
        state = copy.deepcopy(state)
        if isWear:
            if itemType == consts.SHIRT:
                state.setShirt(action.get_item())
            elif itemType == consts.PANTS:
                state.setPants(action.get_item())
            else:
                state.setShoes(action.get_item())
        else:
            if itemType == consts.SHIRT:
                state.setShirt(None)
            elif itemType == consts.PANTS:
                state.setPants(None)
            else:
                state.setShoes(None)

        return state

    def getAction(self, state):
        """
          Compute the action to take in the current state.
          With probability self.epsilon, we should take a random action and
          take the best policy action otherwise.
          If there are no legal actions, it returns None.

        """
        legalActions = self.getLegalActions(state)
        action = None
        if (not legalActions):
            return action
        if (util.flipCoin(self.epsilon)):
            action = random.choice(legalActions)
        else:
            action = self.getPolicy(state)
        return action

    def update(self, state, action, nextState, reward):
        """
          This method updates the Q value.
        """
        key = self.stateActionToKey(state, action)
        self.qValue[key] = self.qValue[key] + self.learningRate * (
                reward + self.discount * self.getValue(
            nextState) - self.qValue[key])

    def learn(self):
        """
        Runs the Q learning algorithm.
        """
        for epoch in range(self.numTraining):
            s = State.State(None, None, None)
            counter = 0
            while (not self.isTerminalState(s) and counter < 100):
                a = self.getAction(s)
                if (a is None):
                    return
                nextState = self.apply_action(s, a)
                self.update(s, a, nextState,
                            self.getReward(nextState, self.goodOutFits, a))
                s = nextState
                counter += 1

    def findMaxAction(self, actions, state):
        """
        Finds the action that maximizes the Q value.
        :param actions: list of actions.
        :param state: State object.
        :return: the action that was found or None if there is no legal action.
        """
        maxQValue = -np.inf
        maxAction = None
        for a in actions:
            if self.getQValue(state, a) > maxQValue:
                maxQValue = self.getQValue(state, a)
                maxAction = a
        return maxAction

    def stateActionToKey(self, state, action):
        """
        Converting the pair (state,action) to string that will serve as the key
        for the Q values dictionary - self.qValue .
        :param state: State object.
        :param action: Action object.
        :return: The representing String.
        """
        return state.__str__() + "#" + action.__str__()
