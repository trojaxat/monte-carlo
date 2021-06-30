import numpy as np
import pandas as pd


class SupermarketModel:
    """ Supermarket that provides the possible states in a MCMC simulation"""

    def __init__(self, daily_info, states=[]):
        self.states = states
        self.daily_info = daily_info

    def generate_transition_probs(self):
        try:
            cross = pd.crosstab(
                self.daily_info['before'], self.daily_info['after'], normalize=1)
            self.states = cross.columns
            return cross
        except Exception:
            print("Key error")
        return False

    def randomNextStepGenerator(self, location):
        index = self.state.index(location)
        current_state = [0, 0, 0, 0, 0]
        current_state[index] = 1
        chance = np.random.choice(current_state, p=self.cross.loc['dairy'])
        return chance
