import pandas as pd
from sensor.config import client
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:

    """
    This functions returns collections as dataframe
    database_name:database name
    collection_name:collection name
    =======================================
    returns pandas DataFrame.
    """

    try:
        logging.info(f"Reading data from database:{database_name}, and collection:{collection_name}")
        df = pd.DataFrame(list(client[database_name][collection_name].find()))
        logging.info(f"Found Columns : {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id.")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and column in df :{df.shape}")
        return df
    except Exception as e:
        raise SensorException(error_message=e, error_detail=sys)













