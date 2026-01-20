import os
from pymongo import MongoClient

class MongoDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

            uri = os.getenv("MONGO_URI")
            if not uri:
                raise Exception("❌ MONGO_URI no está definido")

            client = MongoClient(uri)
            cls._instancia.db = client.get_default_database()

        return cls._instancia
