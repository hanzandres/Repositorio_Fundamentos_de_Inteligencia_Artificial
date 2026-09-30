import os
from dotenv import load_dotenv
from pathlib import Path
from pymogo import mongo_client

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path = env_path)

user = os.getenv('Mongo_User')
password = os.getenv('Mongo_Password')
cluster = os.getenv('Mongo_Cluster')
db = os.getenv('Mongo_DB')
collection = os.getenv('Mongo_Collection')

mongo_uri = f"mongodb+srv://{user}:{password}@{cluster}"