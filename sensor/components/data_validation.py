from sensor.entity import artifact_entity
from sensor.entity import config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import pandas as pd
import os,sys
from typing import Optional


class DataValidation:

    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(msg=f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException(error_message=e, error_detail=sys)

    def is_required_columns_exists(self,)->bool:
        pass
    
    def drop_missing_values_columns(self,df:pd.DataFrame,threshold:float=0.3)->Optional(pd.DataFrame):
        """
        This function will drop column which contains missing values more than specific threshold.

        df:Accepts a pandas DataFrame
        threshold : percentage criteria to drop a column.
        =============================================================================
        returns Pandas DataFrame if atleast a single column is available after missing columns drop else none.
        """
        try:
            pass
        except Exception as e:
            raise SensorException(error_message=e, error_detail=sys)





    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        pass

    


