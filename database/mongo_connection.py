# database/mongodb.py (por ejemplo)
import os
from pymongo import MongoClient

class MongoDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

            mongo_uri = os.getenv(
                "MONGO_URI",
                "mongodb://localhost:27017/"  # fallback local
            )

            client = MongoClient(mongo_uri)
            cls._instancia.db = client["uniemplea_db"]

        return cls._instancia
