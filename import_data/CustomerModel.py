import numpy as np


class CustomerModel:
    """ Customer that moves through a in a MCMC simulation"""

    def __init__(self, name, state, transition_probs, budget=100):
        self.name = name
        self.state = "entrance"
        self.transition_probs = transition_probs
        self.budget = budget

    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'

    def next_state(self):
        ''' Propagates the customer to the next state '''
        if self.is_active() == False:
            return None

        if self.state == 'checkout':
            new_state = 'end'
        else:
            probability = self.transition_probs.T[self.state].array
            probability /= probability.sum()
            new_state = np.random.choice(
                self.transition_probs.T.index, 1, p=probability, replace=False)[0]
        if new_state == self.state:
            tesdt = 1
        self.state = new_state

    def is_active(self):
        if self.state == 'end':
            return False

        return True
