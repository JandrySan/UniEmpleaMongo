from pymongo import MongoClient
import os

class MongoDB:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

            mongo_uri = os.getenv("MONGO_URI")
            if not mongo_uri:
                raise Exception("La variable de entorno MONGO_URI no está configurada")

            client = MongoClient(mongo_uri)
            cls._instancia.db = client.get_default_database()

        return cls._instancia
