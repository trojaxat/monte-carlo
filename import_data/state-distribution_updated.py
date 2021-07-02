#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from IPython.display import display
# Set figure size to (14,6)
plt.rcParams['figure.figsize'] = (14,6)

path = 'data/monday.csv'
endpath = 'data/monday_mc.csv'

def createMcCsv(path, endpath):
    df = pd.read_csv(path, parse_dates=True,
                     delimiter=';')
    df = df.sort_values(by=['customer_no', 'timestamp'])

    dfmc = pd.DataFrame(data=None, columns=[
                        'before', 'after'], dtype=None, copy=False)

    for customer_number in df['customer_no'].unique():
        entrance = True
        for index, location in enumerate(df.loc[df['customer_no'] == customer_number]['location'].iloc):
            before = df.loc[df['customer_no'] ==
                            customer_number]['location'].iloc[index]
            if entrance is True:
                dfmc = dfmc.append(
                    {"before": 'entrance', "after": before}, ignore_index=True)
                entrance = False
            try:
                after = df.loc[df['customer_no'] ==
                               customer_number]['location'].iloc[index+1]
                dfmc = dfmc.append(
                    {"before": before, "after": after}, ignore_index=True)
            except Exception:
                print("Python is a trash language")
    dfmc.to_csv(endpath)

# createMcCsv(path, endpath)

df = pd.read_csv(endpath, delimiter=',')
cross = pd.crosstab(df['before'], df['after'], normalize=0)
print(cross)

cross.loc['dairy']

cross

import numpy as np

checkout=pd.DataFrame(np.array([1,0,0,0,0]).reshape(1,5),columns=cross.columns, index=['checkout']) #add the checkout the raw
checkout

cross = pd.concat([cross,checkout],axis=0) #CONCAT WITH THE DF

cross

# # shows where people go from one location
cross.plot.bar(stacked=False)
plt.show()

# #                   checkout  dairy     drinks    fruit     spices
dairyMc = np.array([0.347924, 0.000000, 0.244669, 0.202020, 0.205387])
drinksMc = np.array([0.534504,  0.028858, 0.000000, 0.233375, 0.203262])
fruitMc = np.array([0.523477, 0.224775, 0.129870, 0.000000, 0.121878])
spicesMc = np.array([0.236631, 0.314171, 0.290107, 0.159091, 0.000000])

#shows heat map of probability
sns.heatmap(cross, annot=True)
plt.show()

def randomNextStepGenerator(location):
    S = ['checkout', 'dairy', "drinks", "fruit", "spices"]  # possible states
    index = S.index(location)
    current_state = [0, 0, 0, 0, 0]
    current_state[index] = 1

    dot_product = np.dot(current_state, cross)
    # given the current probability distribution, a next step
    chance = np.random.choice(S, p=cross.loc['dairy'])
    # What is the probability for the conditions in two steps
    step2 = np.dot(np.dot(current_state, cross), cross)
    print("dot_product", dot_product)
    print("chance", chance)
    print("step2", step2)
    return chance

print(randomNextStepGenerator('dairy'))

def getInitialState():
    '''Set an initial state distribution vector with all customers in the entrance'''
    return np.array([0.4, 0.6])


def getInitialState():
    '''Store the state distribution in a result object (list, DataFrame or similar)'''
    return np.array([0.4, 0.6])

def getInitialState():
    '''Calculate the next state as a dot product of your transition probability matrix P'''
    return np.array([0.4, 0.6])


def getInitialState():
    '''Repeat from 2 for a number of steps'''
    return np.array([0.4, 0.6])


def getInitialState():
    '''Plot the result'''
    return np.array([0.4, 0.6])

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
    def next_state(self):
        self.state= np.random.choice(['spices', 'dairy', 'drinks', 'fruit', 'checkout'], p=self.transition_probs.loc[self.state])
                             # add a method that changes the state attribute of the customer.
                              ## Propagates the customer to the next state.
                               ###Returns nothing.   

c1=Customer(name='Thomas', transition_probs=cross)
c1

c1.state

c1.next_state()

c1.state

c1.next_state()

c1.state

c1.is_active()

c2=Customer(name='Ana', transition_probs=cross)
c2

c2.state

c2.next_state()

c2.is_active()

c3=Customer(name='Dan', transition_probs=cross)
c3

c3.state

c3.is_active()

c3.next_state()

c3.state

c3.is_active()

from faker import Faker

fake = Faker()

fake.name()

cross

df=pd.read_csv(f'data/monday.csv',parse_dates=True, delimiter=';', index_col='timestamp')

all_data=[]
all_days=['monday','tuesday','wednesday','thursday','friday']
for days in all_days:
    all_data.append(pd.read_csv(f'data/{days}.csv', parse_dates=True, delimiter=';'))
df=pd.concat (all_data, axis=0)

df['timestamp']=pd.to_datetime(df['timestamp'])
df['year']=pd.to_datetime(df['timestamp'].astype(str)).dt.year
df['day']=df.timestamp.dt.day_name()
df['hour']=pd.to_datetime(df['timestamp'].astype(str)).dt.hour
df['minute']=pd.to_datetime(df['timestamp'].astype(str)).dt.minute
df

min_stats = df.groupby(['hour', 'minute']).customer_no.count()   ##customer per minute
min_stats

min_stats[7][15] #check the amount on specific hour and minute

"""
Start with this to implement the supermarket simulator.
"""

SIMULATE_MINUTES = 60 * 15

import numpy as np
import pandas as pd
import time

class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self,name):        
        # a list of Customer objects
        self.customers = []
        self.name=name
        self.minutes = 0
        self.last_id = 0
        self.state = np.random.choice(['spices', 'dairy', 'drinks', 'fruit','entrance'])
    
    @property   
    def n_customers(self):
        return len(self.customers)

    @property
    def time(self):
        hour = 7 + self.minutes // 60
        min = self.minutes % 60
        #return f"{hour:02}:{min:02}:00", 
        return hour, min
        
    def next_minute(self):
        """propagates all customers to the next state.
        """
        self.minutes += 1
        for c in self.customers:
            c.next_state()
            self.print_row(c)

    
    def add_new_customers(self, hour, min_, min_stats):
        n = min_stats[hour][min_]
        #n = np.random.poisson(NEW_CUSTOMERS_PER_MINUTE)
        for i in range(n):
            self.last_id += 1
            c = Customer(fake.name,cross)
            self.customers.append(c)
            self.print_row(c)

        """randomly creates new customers.
        """

    def remove_exited_customers(self):
         self.customers = [c for c in self.customers if c.is_active]
    
    
    def __repr__(self):
        """formats as CSV"""
        return f"{self.time}, {self.name}, {self.n_customers}"
    
    
    def print_row(self, customer):
        """prints one row of CSV"""
        row = str(self) + ", " + str(customer)
        print(row)
    
if __name__ == "__main__":
    s = Supermarket("Doodl")
    for i in range(SIMULATE_MINUTES):
        s.next_minute()
        hour, min_ = s.time[0], s.time[1]
        s.add_new_customers(hour,min_, min_stats)
        s.remove_exited_customers()

