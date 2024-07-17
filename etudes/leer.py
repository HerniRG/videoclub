fichero = open("data/generos.csv", "r")
for ix, linea in enumerate(fichero):
    
    print(linea)
    if ix > 20:
        break
