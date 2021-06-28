import pandas as pd
from import_csv_to_database import csv_to_database
from import_csv_to_database import getConnectionString
import time

time.sleep(5)

df = pd.read_csv(
    'src/input.csv', delimiter=';', parse_dates=True)
conn = getConnectionString()
csv_to_database(conn, ";")

df.to_csv(
    'src/output.csv')
