from abc import ABC, abstractmethod
from database.mongo_connection import db

class RepositorioBaseMongo(ABC):

    def __init__(self, collection):
        self.collection = collection

    @abstractmethod
    def guardar(self, entidad):
        pass

    @abstractmethod
    def buscar_por_id(self, entidad_id):
        pass

