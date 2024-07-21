import csv
from abc import ABC, abstractmethod
from app.modelos import Copias, Director, Generos, Pelicula

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

class DAO_CSV(DAO):
    model = None

    def __init__(self, path, enconding = "utf-8"):
        self.path = path
        self.encoding = enconding

    def todos(self):
        with open(self.path, "r", newline="", encoding = self.encoding) as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(self.model.create_from_dict(registro))
        return lista
    
    def guardar(self, instancia):
        diccionario = self.model.create_dict_from_instance(instancia)
        with open(self.path, "a", newline="", encoding = self.encoding) as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter = ";", quotechar = "'", fieldnames = list(diccionario.keys()), lineterminator='\n')
            escribir_csv.writerow(diccionario)
    
    def consultar(self, id):
        lista_consulta = self.todos()
        for consulta in lista_consulta:
            if consulta.id == id:
                return consulta
        return None
    
    def borrar(self, id):
        consulta = self.consultar(id)
        lista_consulta = self.todos()
        if consulta in lista_consulta:
            lista_consulta.remove(consulta)
        fieldnames = list(self.model.create_dict_from_instance(consulta).keys())
        with open(self.path, "w", newline="", encoding=self.encoding) as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter=";", quotechar="'", fieldnames=fieldnames, lineterminator='\n')
            escribir_csv.writeheader()
            for registro in lista_consulta:
                escribir_csv.writerow(self.model.create_dict_from_instance(registro))
    
    def actualizar(self, instancia):
        lista_consulta = self.todos()
        for i, registro in enumerate(lista_consulta):
            if registro.id == instancia.id:
                lista_consulta[i] = instancia
        fieldnames = list(self.model.create_dict_from_instance(instancia).keys())
        with open(self.path, "w", newline="", encoding=self.encoding) as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter=";", quotechar="'", fieldnames=fieldnames, lineterminator='\n')
            escribir_csv.writeheader()
            for registro in lista_consulta:
                escribir_csv.writerow(self.model.create_dict_from_instance(registro))

class DAO_CSV_Director(DAO_CSV):    
    model = Director
    
class DAO_CSV_Pelicula(DAO_CSV):
    model = Pelicula

class DAO_CSV_Generos(DAO_CSV):
    model = Generos

class DAO_CSV_Copias(DAO_CSV):
    model = Copias