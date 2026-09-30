import random
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
import os
from urllib.parse import quote_plus


load_dotenv()

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

user = os.getenv('Mongo_User')
password = os.getenv('Mongo_Password')
cluster = os.getenv('Mongo_Cluster')
db = os.getenv('Mongo_DB')
collection = os.getenv('Mongo_Collection')


if not all([user,password,cluster,db,collection]): 
    raise ValueError("")


mongo_uri = f"mongodb+srv://{user}:{password}@{cluster}"

client = MongoClient(mongo_uri)
db = client[db]
collection = db[collection]

productos = ["laptop","tablet","celular","monitor"]


for _ in range(50):
    venta = {
        "producto": random.choice(productos),
        "cantidad": random.randint(1,5),
        "precio": random.randint(5000,20000)
        
    }
    
    collection.insert_one(venta)
    
    print("datos generados correctamente")