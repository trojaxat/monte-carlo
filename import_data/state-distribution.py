import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from IPython.display import display

path = 'import_data/data/monday.csv'
endpath = 'import_data/data/monday_mc.csv'


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

# # shows where people go from one location
# cross.plot.bar(stacked=False)
# plt.show()

# #                   checkout  dairy     drinks    fruit     spices
# dairyMc = np.array([0.347924, 0.000000, 0.244669, 0.202020, 0.205387])
# drinksMc = np.array([0.534504,  0.028858, 0.000000, 0.233375, 0.203262])
# fruitMc = np.array([0.523477, 0.224775, 0.129870, 0.000000, 0.121878])
# spicesMc = np.array([0.236631, 0.314171, 0.290107, 0.159091, 0.000000])

# # shows heat map of probability
# sns.heatmap(cross, annot=True)
# plt.show()


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
