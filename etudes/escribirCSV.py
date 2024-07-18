import csv

fichero = open("data/grupos_zoo.csv", "a" , newline = "")

escribir_csv = csv.writer(fichero, delimiter = ";", quotechar = "'")

escribir_csv.writerow([1,3,1,23])
escribir_csv.writerow([1,4,1,18])

fichero.close()


# con un dictWriter, con diccionarios

with open("data/grupos_zoo.csv", "a" , newline = "") as fichero: # error se cierra archivo bien con with y close no hace falta

    escribir_csv = csv.DictWriter(fichero, delimiter = ";", quotechar = "'", fieldnames = ['id_grupo','tipo_entrada','cantidad_entrada','subtotal'])
    escribir_csv.writerows([
        {"id_grupo":1, "tipo_entrada": 3, "cantidad_entrada": 1, "subtotal":23},
        {"id_grupo":1, "tipo_entrada": 4, "cantidad_entrada": 1, "subtotal":18}
    ])