import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os 

# Provide the mongodb localhost url to connect python to mongodb.
@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_key:str = os.getenv('AWS_ACCESS_KEY')
    aws_secter_key:str = os.getenv('AWS_SECTER_KEY')


env_var = EnvironmentVariable()
client = pymongo.MongoClient(env_var.mongo_db_url)


