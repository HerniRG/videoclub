from abc import ABC, abstractmethod

class Director():
    def __init__(self, nombre, id=-1) -> None:
        self.nombre = nombre
        self.id = id


class DAO(ABC):
    @abstractmethod
    def guardar(self, instancia):
        pass

    @abstractmethod
    def actualizar(self, instancia):
        pass

    @abstractmethod
    def borrar(self, id):
        pass

    @abstractmethod
    def consultar(self, id):
        pass
    
    @abstractmethod
    def todos(self):
        pass
    