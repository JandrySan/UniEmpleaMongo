import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("❌ MONGO_URI no está definida")

client = MongoClient(MONGO_URI)

db = client["uniemplea"]  # 👈 NOMBRE EXPLÍCITO DE LA BD
