import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise RuntimeError("MONGO_URI no está configurada")

client = MongoClient(MONGO_URI)
db = client["uniemplea"]
