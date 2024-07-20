from abc import ABC, abstractmethod
import csv

class Model(ABC):
    @classmethod
    @abstractmethod
    def create_from_dict(cls, diccionario):
        pass

    @classmethod
    @abstractmethod
    def create_dict_from_instance(cls, instancia):
        pass

class Director(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["nombre"], int(diccionario["id"]))
    
    @classmethod
    def create_dict_from_instance(cls, instancia):
        return {"nombre": instancia.nombre, "id": instancia.id}

    def __init__(self, nombre, id=-1) -> None:
        self.nombre = nombre
        self.id = id

    def  __repr__(self) -> str:
        return f"Director({self.id}): {self.nombre}"
    
    def __eq__(self, other: object) -> bool:
        isEqual = False
        if isinstance(other, self.__class__): # self.__class__ es lo mismo que Director
            isEqual = self.nombre == other.nombre and self.id == other.id       
        return isEqual
    
    def __hash__(self) -> int:
        return hash((self.id, self.nombre))

class Pelicula(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["titulo"], diccionario["sinopsis"], int(diccionario["director_id"]), int(diccionario["id"]))
    
    @classmethod
    def create_dict_from_instance(cls, instancia):
        return {
            "id": instancia.id,
            "titulo": instancia.titulo,
            "sinopsis": instancia.sinopsis,
            "director_id": instancia._director_id
        }

    def __init__(self, titulo, sinopsis, director: object, id = -1) -> None:
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.id = id
        self.director = director
        
    @property    
    def director(self):
        return self._director
    
    @director.setter
    def director(self, value):
        if isinstance(value, Director):
            self._director = value
            self._director_id = value.id
        elif isinstance(value, int):
            self._director = None
            self._director_id = value
        else:
            raise TypeError(f"{value} debe ser un entero o instancia de Director")
    
    def  __repr__(self) -> str:
        return f"Pelicula: Título ({self.titulo}), Sinopsis {self.sinopsis} y Director {self.director}."
    
    def __eq__(self, other: object) -> bool:
        isEqual = False
        if isinstance(other, self.__class__): # self.__class__ es lo mismo que Director
            isEqual = self.id == other.id and self.director == other.director and self.sinopsis == other.sinopsis and self.titulo == other.titulo      
        return isEqual
    
    def __hash__(self) -> int:
        return hash((self.id, self.titulo, self.sinopsis, self.director))

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
    