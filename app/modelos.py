from abc import ABC, abstractmethod

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

class Generos(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["genero"], int(diccionario["id"]))
    
    @classmethod
    def create_dict_from_instance(cls, instancia):
        return {"id": instancia.id, "genero": instancia.genero}

    def __init__(self, genero, id=-1) -> None:
        self.id = id
        self.genero = genero

    def __repr__(self) -> str:
        return f"Genero({self.id}): {self.genero}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.genero == other.genero
        return False
    
    def __hash__(self) -> int:
        return hash((self.id, self.genero))
    
class Copias(Model):
    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(int(diccionario["id_pelicula"]), int(diccionario["id_copia"]))
    
    @classmethod
    def create_dict_from_instance(cls, instancia):
        return {"id_copia": instancia.id, "id_pelicula": instancia.id_pelicula}
    
    def __init__(self,id_pelicula, id = -1) -> None:
        self.id_pelicula = id_pelicula
        self.id = id
    
    def __repr__(self) -> str:
        return f"Copia ID {self.id}, Pelicula ID {self.id_pelicula}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id_pelicula == other.id_pelicula and self.id == other.id
        return False
    
    def __hash__(self) -> int:
        return hash((self.id, self.id_pelicula))