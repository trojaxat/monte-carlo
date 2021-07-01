import pandas as pd
import time
import names
import numpy as np
import datetime
import cv2
from local_functions import getConnectionString
from supermarket import Supermarket
from customer import Customer
from dataPreparation import DataPreparation
from visualize import Visualize_Simulation
from import_data.tiles_skeleton import SupermarketMap, MARKET

# conn = getConnectionString()
# csv_to_database(conn, ",")

# First time?
# dataModel = DataPreparation(
#     "import_data/data/monday.csv", 'import_data/data/monday_mc.csv')
# df = dataModel.createMcCsv()

# Second time
df = pd.read_csv(
    'import_data/data/monday_mc.csv', delimiter=',', parse_dates=True,  dtype=None)
supermarket = Supermarket(df)
cross = supermarket.generate_transition_probs()

# each array spot is a customer, value is how many stops they make
customerArray = [3, 4, 5, 2, 4]
tiles = cv2.imread("import_data/media/tiles.png")
avatar = cv2.imread("import_data/media/sprite.jpeg")
market = SupermarketMap(MARKET, tiles)

for customer_steps in customerArray:
    random_start = supermarket.random_first_state()
    customer = Customer(
        names.get_full_name(), cross, avatar, market, random_start)
    [(customer.next_state(), print(
        f"{customer.name} is in", customer.state)) for x in range(customer_steps)]

quit()
no_of_customer_per_min_list = 5
customer_list = []
for time_index, no_of_customer_per_min in enumerate(no_of_customer_per_min_list):
    for no_of_customer in range(no_of_customer_per_min):
        customer_list.append(
            Customer.Customer(
                names.get_full_name(),
                random_start,
                cross,
                generate_first_location_index(),
                transition_matrix,
                time_spent_prob,
                time_index,
            )
        )

starting_time = datetime.datetime(2000, 1, 1, 7, 0, 0).time()
background = cv2.imread("market.png")
# masks for path finding. mask_exit is to prevent the pathfinding algorithm from going
# to the cashier in the opposite direction
mask = cv2.imread("market_maskv2.png")
mask_exit = cv2.imread("market_mask_exit.png")
Sim = Visualize_Simulation(
    customer_list, starting_time, background, mask, mask_exit, scale=0.2
)

Sim.visualize()
