from os.path import join, dirname
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus


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
