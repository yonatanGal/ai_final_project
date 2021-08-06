import util
import random
import Constants as consts
import numpy as np
import State
import copy


class QLearningAgent():
    """
      Q-Learning Agent

      Functions you should fill in:
        - getQValue
        - getAction
        - getValue
        - getPolicy
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions
          for a state
    """

    def __init__(self, db_shirts, db_pants,
                 goodOutFit: State, gamma=0.8, learningRate=1, epsilon=0.3,
                 numTraining=100):
        "You can initialize Q-values here..."

        self.qValue = util.Counter()
        # self.qValue = util.initQvalues(db_shirts, db_pants, dict())

        self.learningRate = float(learningRate)
        self.epsilon = float(epsilon)
        self.discount = float(gamma)
        self.numTraining = int(numTraining)
        self.allActions = util.get_all_actions(db_shirts + db_pants)
        self.goodOutFit = goodOutFit


    def isTerminalState(self, state):
        # todo: think about it
        if (state.getShirt() and state.getPants()):
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
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        actions = self.getLegalActions(state)
        if not actions:
            return 1  # todo: maybe change to 1? because the only state where you have no legal action to take is a terminal state
        # maxAction = max(actions, key=lambda a: self.getQValue(state, a))
        maxAction = self.findMaxAction(actions, state)

        return self.getQValue(state, maxAction)

    def getPolicy(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        actions = self.getLegalActions(state)
        if (not actions):
            return None
        # maxAction = max(actions, key=lambda a: self.getQValue(state, a))
        maxAction = self.findMaxAction(actions, state)
        return maxAction

    def getLegalActions(self, state):
        # todo: checks for all possible actions regarding the given state
        shirt = state.getState()[0]
        pants = state.getState()[1]
        legalActions = []
        if (shirt is None):
            if (pants is None):
                for action in self.allActions:
                    if action.get_wants_to_wear():
                        legalActions.append(action)
            else:
                # get all shirts putting and one pants removing
                for action in self.allActions:
                    if action.get_item().getType() == consts.SHIRT and action.get_wants_to_wear():
                        legalActions.append(action)
                    elif action.get_item() == state.getPants() and not action.get_wants_to_wear():
                        legalActions.append(action)

        elif (pants is None):
            # get all pants puting and one shirt removing
            for action in self.allActions:
                if action.get_item().getType() == consts.PANTS and action.get_wants_to_wear():
                    legalActions.append(action)
                elif action.get_item() == state.getShirt() and not action.get_wants_to_wear():
                    legalActions.append(action)
        else:
            # get all removing
            for action in self.allActions:
                if action.get_item() == state.getShirt() or action.get_item() == state.getPants():
                    legalActions.append(action)
        return legalActions

    def getReward(self, state, goodOutfit,action):
        # todo: make sure this implementation is good (maybe change calculations to do sqrt of squares, etc.
        if (self.isTerminalState(state)):
            return 1
        if (not action.get_wants_to_wear()):
            return -10
        formalityReward = util.formalDistance(state, goodOutfit)
        weatherDistance = util.weatherDistance(state, goodOutfit)
        color_Distance = util.colorDistanceWrapperLearning(state, goodOutfit)
        return formalityReward + weatherDistance + color_Distance

    def apply_action(self, state, action):
        isWear = action.get_wants_to_wear()
        itemType = action.get_item().getType()
        state = copy.deepcopy(state)
        if isWear:
            if itemType == consts.SHIRT:
                state.setShirt(action.get_item())
            elif itemType == consts.PANTS:
                state.setPants(action.get_item())
        else:
            if itemType == consts.SHIRT:
                state.setShirt(None)
            elif itemType == consts.PANTS:
                state.setPants(None)
        return state

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
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
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        key = self.stateActionToKey(state, action)
        self.qValue[key] = self.qValue[key] + self.learningRate * (
                reward + self.discount * self.getValue(
            nextState) - self.qValue[key])


    def learn(self):
        for epoch in range(self.numTraining):
            s = State.State(None, None)
            # counter = 0
            while (not self.isTerminalState(s)):  # change to termoninal state?
                a = self.getAction(s)
                nextState = self.apply_action(s, a)
                self.update(s, a, nextState,
                            self.getReward(nextState, self.goodOutFit,a))
                s = nextState
                # counter += 1

    def findMaxAction(self, actions, state):
        maxQValue = -np.inf
        maxAction = None
        for a in actions:
            if self.getQValue(state, a) > maxQValue:
                maxQValue = self.getQValue(state, a)
                maxAction = a
        return maxAction

    def stateActionToKey(self, state, action):
        return state.__str__() + "#" + action.__str__()
