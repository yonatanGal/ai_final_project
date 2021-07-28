import util
import random
import numpy as np
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

    def __init__(self, learningRate,epsilon,gamma,numTraining):
        "You can initialize Q-values here..."

        self.qValue = util.Counter()
        self.learningRate = float(learningRate)
        self.epsilon = float(epsilon)
        self.discount = float(gamma)
        self.numTraining = int(numTraining)

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we never seen
          a state or (state,action) tuple
        """
        return self.qValue[(state, action)]

    def getValue(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        actions = self.getLegalActions(state)
        if not actions:
            return 0.0
        maxAction = max(actions, key=lambda a: self.getQValue(state, a))
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
        maxAction = max(actions, key=lambda a: self.getQValue(state, a))
        return maxAction

    def getLegalActions(self,state):
        # todo: checks for all possible actions regarding the given state
        shirt = state.getState()[0]
        pants = state.getState()[1]
        if (shirt is None):
            if (pants is None):
                # get all actions of putting

            else:
                # get all shirts putting and pants removing
        elif (pants is None):
            #get all pants puting and shirts removing
        else:
            # get all removing

    def getReward(self,state,goodOutfit):
        # todo: make sure this implementation is good (maybe change calculations to do sqrt of squares, etc.
        formalityReward = util.formalDistance(state,goodOutfit)
        weatherDistance = util.weatherDistance(state,goodOutfit)
        color_Distance = util.colorDistanceWrapperLearning(state,goodOutfit)
        return formalityReward + weatherDistance + color_Distance

    def apply_action(self,state,action):
        isWear = action.get_wants_to_wear()
        itemType = action.get_item().getType()
        if isWear:
            if itemType == "Shirts":
                state.set_shirt(action.get_item())
            elif itemType == "Pants":
                state.set_pants(action.get_item())
        else:
            if itemType == "Shirts":
                state.set_shirt(None)
            elif itemType == "Pants":
                state.set_pants(None)

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

        self.qValue[(state, action)] = self.qValue[
                                           (state, action)] + self.learningRate * (
                                               reward + self.discount * self.getValue(
                                           nextState) - self.qValue[
                                                   (state, action)])