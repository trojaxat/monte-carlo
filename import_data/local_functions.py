from os.path import join, dirname
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
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


def getEnv():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)


def trim_all_columns(df):
    """ 
    Trim whitespace from ends of each value across all series in dataframe
    """
    def trim_strings(x): return x.strip() if isinstance(x, str) else x
    return df.applymap(trim_strings)


def getConnectionString():
    getEnv()
    USERNAME = os.environ.get("USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
    HOST = os.environ.get("HOST")
    PORT = os.environ.get("PORT")
    DATABASE = os.environ.get("DATABASE")

    return f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
