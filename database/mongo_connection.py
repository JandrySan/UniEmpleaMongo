# database/mongo_connection.py
import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["uniemplea"]  # nombre de la BD (aunque no exista, Mongo la crea)


