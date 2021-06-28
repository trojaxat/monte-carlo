import glob
import os
import pandas as pd

if __name__ == '__main__':
    subPath = "\\data"


def csv_to_database(connection_string, delimiter, subPath="\\data"):
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    for filename in glob.glob(CURR_DIR + subPath + "/*.csv"):
        df = pd.read_csv(filename, delimiter=delimiter, parse_dates=True)
        endOfCsv = os.path.basename(os.path.normpath(filename))
        tableName = endOfCsv.split('.', 1)[0]
        df.to_sql(tableName, connection_string)
