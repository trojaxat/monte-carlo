""" Supermarket
This script contains the class supermarket and functions for 
generating shopping behaviour.
"""
import numpy as np
import pandas as pd


class Supermarket:
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

    def random_first_state(self):
        return np.random.choice(self.states.delete(0))
