import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("data/peliculas.sqlite")
cursor = conexion.cursor()

# Ejecutar consulta
cursor.execute("select id, nombre, url_foto, url_web from directores")

# Obtener resultados y descripción de columnas
resultados = cursor.fetchall()
descripcion_columnas = cursor.description

print(f'\nResultados: {resultados}')
print(f'\nColumnas Sin Filtrar: {descripcion_columnas}')

columnas_finales = list(map(lambda i: i[0], descripcion_columnas))

# hacer un diccionario con clave valor
# id 1 nombre perico ur... como lo queremos el diccionario del DAO

print(f'\nColumnas Finales: {columnas_finales}')

lista_registros_bbdd = []

for registro in resultados:
    registro_diccionario = {}
    for i, nombre_columna in enumerate(columnas_finales):       
        registro_diccionario[nombre_columna] = registro[i]
    lista_registros_bbdd.append(registro_diccionario)

print(f'\nLista de Registros BBDD: {lista_registros_bbdd}\n')

conexion.close()




