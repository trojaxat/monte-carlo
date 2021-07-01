import numpy as np

TILE_SIZE = 32


class Customer:
    """ Customer that moves through a in a MCMC simulation"""

    def __init__(
            self,
            name,
            transition_probs,
            avatar,
            supermarketmap,
            x=12,
            y=12,
            state="entrance",
    ):
        self.name = name
        self.transition_probs = transition_probs
        self.state = state
        self.supermarket = supermarketmap
        self.avatar = avatar
        self.row = x
        self.col = y

    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'

    def draw(self, frame):
        x = self.col * TILE_SIZE
        y = self.col * self.row
        frame[y:12, x:12] = self.avatar

    def next_state(self):
        ''' Propagates the customer to the next state '''
        if self.is_active() == False:
            return None

        if self.state == 'checkout':
            new_state = 'end'
        else:
            # if the probability does not add up to 1, it is then realigned on itself
            probability = self.transition_probs.T[self.state].array
            probability /= probability.sum()
            new_state = np.random.choice(
                self.transition_probs.T.index, 1, p=probability, replace=False)[0]
        self.state = new_state

    def move(self, direction):
        new_row = self.row
        new_col = self.col

        if direction == 'up':
            new_row -= 1

        if self.supermarket.contents[new_row][new_col] == '.':
            self.col = new_col
            self.row = new_row

    def is_active(self):
        if self.state == 'end':
            return False

        return True
