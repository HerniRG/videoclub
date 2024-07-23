import sqlite3

con = sqlite3.connect("data/peliculas.sqlite")
cur = con.cursor()

nombre = input("Nombre: ")
foto = input("Url foto: ")
web = input("Url web: ")

#query = f"INSERT INTO directores (nombre, url_foto, url_web) values('{nombre}', '{foto}', '{web}')" MAL, se puede hackear

query = f"INSERT INTO directores (nombre, url_foto, url_web) values(?, ?, ?)"

cur.execute(query, (nombre, foto, web))

con.commit()

con.close()