import pandas as pd
from local_functions import csv_to_database, getConnectionString
import SupermarketModel
import CustomerModel
import time
import names
import numpy as np

df = pd.read_csv(
    'import_data/data/monday_mc.csv', delimiter=',', parse_dates=True,  dtype=None)
# conn = getConnectionString()
# csv_to_database(conn, ";")

supermarket = SupermarketModel.SupermarketModel(df)
cross = supermarket.generate_transition_probs()
supermarket_layout = supermarket.states

# each array spot is a customer, value is how many stops they make
customerArray = [3, 4, 5, 2, 4]
for customer_steps in customerArray:
    random_start = np.random.choice(supermarket.states.delete(0))
    customer = CustomerModel.CustomerModel(
        names.get_full_name(), random_start, cross)
    [(customer.next_state(), print(
        f"{customer.name} is in", customer.state)) for x in range(customer_steps)]
