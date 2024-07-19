from abc import ABC, abstractmethod
import csv

class Director:
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

class Pelicula:
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
        return f"Pelicula: Título ({self.titulo}), Sinopsis {self.sinopsis} y Director {self.director.nombre}."
    
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

class DAO_CSV_Director(DAO):
    
    def __init__(self, path):
        self.path = path

    def guardar(self, instancia):
        with open(self.path, "a", newline="") as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter = ";", quotechar = "'", fieldnames = ['nombre','id'], lineterminator='\n')
            escribir_csv.writerow({"nombre": instancia.nombre, "id": instancia.id})
    
    def borrar(self, id): # tengo que escribir el CSV entero?? DUDA
        director = self.consultar(id)
        directores = self.todos()
        if director in directores:
            directores.remove(director)
        with open(self.path, "w", newline="") as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter=";", quotechar="'", fieldnames=['nombre', 'id'], lineterminator='\n') # lineterminator en google
            escribir_csv.writeheader() # lo he tenido que consultar porque me escirbía sin las etiquetas nombre e id
            for director in directores:
                escribir_csv.writerow({"nombre": director.nombre, "id": director.id})
                        
    def consultar(self, id):
        directores = self.todos()
        for director in directores:
            if director.id == id:
                return director
        return None

    def todos(self):
        with open(self.path, "r", newline="") as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(Director(registro["nombre"], int(registro["id"])))
        return lista
    
    def actualizar(self, instancia):
        directores = self.todos()
        for i, director in enumerate(directores):
            if director.id == instancia.id:
                directores[i] = instancia # si coincide los id de director y el que metimos lo sustituye por el que metimos con los nuevos datos
        with open(self.path, "w", newline="") as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter=";", quotechar="'", fieldnames=['nombre', 'id'], lineterminator='\n')
            escribir_csv.writeheader()
            for director in directores:
                escribir_csv.writerow({"nombre": director.nombre, "id": director.id})

class DAO_CSV_Pelicula(DAO):
    def __init__(self, path):
        self.path = path 

    def guardar(self, instancia):
        with open(self.path, "a", newline="") as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter=";", quotechar="'", fieldnames=["id", "titulo", "sinopsis", "director_id"], lineterminator='\n')
            escribir_csv.writerow({"id": instancia.id, "titulo": instancia.titulo, "sinopsis": instancia.sinopsis, "director_id": instancia._director_id})

    def todos(self):
        with open(self.path, "r", newline="") as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                try:
                    id = int(registro["id"])
                    director_id = int(registro["director_id"])
                    lista.append(Pelicula(registro["titulo"], registro["sinopsis"], director_id, id))
                except ValueError as e:
                    print(f"Error processing record {registro}: {e}")
        return lista

    def consultar(self, id):
        peliculas = self.todos()
        for pelicula in peliculas:
            if pelicula.id == id:
                return pelicula
        return None
    
    def borrar(self, id):
        pelicula = self.consultar(id)
        peliculas = self.todos()
        if pelicula in peliculas:
            peliculas.remove(pelicula)
        with open(self.path, "w", newline="") as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter=";", quotechar="'", fieldnames=["id","titulo","sinopsis","director_id"], lineterminator='\n') # lineterminator en google
            escribir_csv.writeheader() # lo he tenido que consultar porque me escirbía sin las etiquetas nombre e id
            for pelicula in peliculas:
                escribir_csv.writerow({"id": pelicula.id, "titulo": pelicula.titulo, "sinopsis": pelicula.sinopsis, "director_id": pelicula._director_id})
    
    def actualizar(self, instancia):
        peliculas = self.todos()
        for i, pelicula in enumerate(peliculas):
            if pelicula.id == instancia.id:
                peliculas[i] = instancia # si coincide los id de pelicula y el que metimos lo sustituye por el que metimos con los nuevos datos
        with open(self.path, "w", newline="") as fichero:
            escribir_csv = csv.DictWriter(fichero, delimiter=";", quotechar="'", fieldnames=["id", "titulo", "sinopsis", "director_id"], lineterminator='\n')
            escribir_csv.writeheader()
            for pelicula in peliculas:
                escribir_csv.writerow({"id": pelicula.id, "titulo": pelicula.titulo, "sinopsis": pelicula.sinopsis, "director_id": pelicula._director_id})