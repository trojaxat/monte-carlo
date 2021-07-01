import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from IPython.display import display


class DataPreparation:
    """ Supermarket that provides the possible states in a MCMC simulation"""

    def __init__(self, path='import_data/data/monday.csv', endpath='import_data/data/monday_mc.csv'):
        self.path = path
        self.endpath = endpath

    def createMcCsv(self):
        df = pd.read_csv(self.path, parse_dates=True,
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

                # if index+1 in df.loc[df['customer_no'] == customer_number]['location'].index
                try:
                    after = df.loc[df['customer_no'] ==
                                   customer_number]['location'].iloc[index+1]
                    dfmc = dfmc.append(
                        {"before": before, "after": after}, ignore_index=True)
                except Exception:
                    print("Python sucks")

        dfmc.to_csv(self.endpath)
        return dfmc

    def showHeatMap(cross):
        cross.plot.bar(stacked=False)
        plt.show()

    def showHeatMap(cross):
        sns.heatmap(cross, annot=True)
        plt.show()

    def getInitialState():
        '''Plot the result'''
        return np.array([0.4, 0.6])
