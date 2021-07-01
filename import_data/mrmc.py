
import SupermarketModel
import numpy as np
import pandas as pd

class Customer:
    def __init__(self, name, transition_probs, budget=100):
        self.name = name
        self.state = np.random.choice(['spices', 'dairy', 'drinks', 'fruit'])
        self.transition_probs=transition_probs
        self.budget = budget
        
    def is_active(self):
         if self.state == 'checkout':
            return 'False'
         else:
            return 'True'
        
    def __repr__(self):                                     #convert an object to a string and create a summary of the object
        return f'<Customer {self.name} in {self.state}>'


    def next_state(self):
        self.state= np.random.choice(['spices', 'dairy', 'drinks', 'fruit', 'checkout'], p=self.transition_probs.loc[self.state])
                             # add a method that changes the state attribute of the customer.
                              ## Propagates the customer to the next state.
                               ###Returns nothing.   

df = pd.read_csv(
    'import_data/data/monday_mc.csv', delimiter=',', parse_dates=True,  dtype=None)

Supermarket=SupermarketModel.SupermarketModel(df)
cross=Supermarket.generate_transition_probs()
c1=Customer(name='Thomas', transition_probs=cross)
print(c1)

c1.state

c1.next_state()

c1.state

c1.next_state()

c1.state

c1.is_active()

c2=Customer(name='Ana', transition_probs=cross)

print(c2)

c2.state

c2.next_state()

c2.is_active()

c3=Customer(name='Dan', transition_probs=cross)
print(c3)

c3.state

c3.is_active()

c3.next_state()

c3.state

c3.is_active()
