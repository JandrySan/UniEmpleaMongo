import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

class MongoDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            client = MongoClient(MONGO_URI)
            cls._instancia.db = client["uniemplea"]  # nombre explícito
        return cls._instancia



