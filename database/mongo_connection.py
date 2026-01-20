import os
from pymongo import MongoClient

class MongoDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

            MONGO_URI = os.getenv("MONGO_URI")
            client = MongoClient(MONGO_URI)

            
            cls._instancia.db = client["uniemplea_db"]

        return cls._instancia


