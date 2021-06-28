import pandas as pd

df = pd.read_csv(
    'src/input.csv')

df.to_csv(
    'src/output.csv')
