import csv
from abc import ABC, abstractmethod
import sqlite3
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

class DAO_SQLite(DAO):
    model = None
    table = None

    def __init__(self, path):
        self.path = path
    
    def todos(self):
        conexion = sqlite3.connect(self.path)
        cursor = conexion.cursor()
        # Ejecutar consulta
        cursor.execute(f"SELECT * FROM {self.table}")
        # Obtener resultados y descripción de columnas
        resultados = cursor.fetchall()  
        columnas_finales = list(map(lambda i: i[0], cursor.description))
        lista = self.__rows_to_dictlist(resultados, columnas_finales)
        conexion.close()
        return lista
    
    def consultar(self, id):
        conexion = sqlite3.connect(self.path)
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        conexion.close()
        if resultado:
            descripcion_columnas = list(map(lambda i: i[0], cursor.description))
            registro_diccionario = {descripcion_columnas[i]: resultado[i] for i in range(len(descripcion_columnas))}
            return self.model.create_from_dict(registro_diccionario)
        return None

    def actualizar(self, instancia):
        diccionario = self.model.create_dict_from_instance(instancia)
        campos = ', '.join([f"{key} = ?" for key in diccionario.keys()])
        valores = list(diccionario.values())
        conexion = sqlite3.connect(self.path)
        cursor = conexion.cursor()
        cursor.execute(f"UPDATE {self.table} SET {campos} WHERE id = ?", valores + [instancia.id])
        conexion.commit()
        conexion.close()
    
    def borrar(self, id):
        conexion = sqlite3.connect(self.path)
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM {self.table} WHERE id = ?", (id,))
        conexion.commit()
        conexion.close()
    
    def guardar(self, instancia):
        diccionario = self.model.create_dict_from_instance(instancia)
        campos = ', '.join(diccionario.keys())
        placeholders = ', '.join(['?' for _ in diccionario.values()])
        valores = list(diccionario.values())
        conexion = sqlite3.connect(self.path)
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO {self.table} ({campos}) VALUES ({placeholders})", valores)
        conexion.commit()
        conexion.close()
        
    
    def __rows_to_dictlist(self, filas, nombres):
        lista_registros_bbdd = []
        for registro in filas:
            registro_diccionario = {}
            for i, nombre_columna in enumerate(nombres):       
                registro_diccionario[nombre_columna] = registro[i]
            lista_registros_bbdd.append(self.model.create_from_dict(registro_diccionario)) # lo hacemos aqui para no hacer 2 bucles
        return lista_registros_bbdd


class DAO_SQLite_Director(DAO_SQLite):
    model = Director
    table = "directores"

class DAO_SQLite_Pelicula(DAO_SQLite):
    model = Pelicula
    table = "peliculas"

class DAO_SQLite_Generos(DAO_SQLite):
    model = Generos
    table = "generos"

class DAO_SQLite_Copias(DAO_SQLite):
    model = Copias
    table = "copias"