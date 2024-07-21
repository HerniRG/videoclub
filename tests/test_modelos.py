from app.modelos import Copias, Director, Pelicula, Generos
from app.daos import DAO_CSV_Copias, DAO_CSV_Director, DAO_CSV_Pelicula, DAO_CSV_Generos

def test_create_director():
    director = Director("Robert Redford", -1)

    assert director.nombre == "Robert Redford"
    assert director.id == -1

def test_dao_directores_traer_todos():
    dao = DAO_CSV_Director("tests/data/directores.csv")
    directores = dao.todos()

    assert len(directores) == 8
    assert directores[7] == Director("Charlie Chaplin", 8)

def test_dao_directores_guardar_director():
    dao = DAO_CSV_Director("tests/data/directores.csv")
    
    guardar_director = dao.guardar(Director("Wolframio", 9))
    directores = dao.todos()

    assert len(directores) == 9
    assert directores[8] == Director("Wolframio", 9)

    dao.borrar(9)

def test_dao_directores_consulta():
    dao = DAO_CSV_Director("tests/data/directores.csv")
    alfred = dao.consultar(3)

    assert alfred == Director("Alfred Hitchcock", 3)

def test_dao_directores_borrar_director():
    dao = DAO_CSV_Director("tests/data/directores.csv")
       
    dao.borrar(8)
    directores = dao.todos()

    assert len(directores) == 7
    assert Director("Charlie Chaplin", 8) not in directores

    dao.guardar(Director("Charlie Chaplin", 8))

def test_dao_directores_actualizar_director():
    dao = DAO_CSV_Director("tests/data/directores.csv")
    
    director = dao.consultar(1)
    director.nombre = "Wolframio Actualizado"
    dao.actualizar(director)
    
    director_actualizado = dao.consultar(1)
    assert director_actualizado.nombre == "Wolframio Actualizado"

    director.nombre = "Director 1"  # Restaurar valor original
    dao.actualizar(director)

def test_create_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", 9)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._director_id == 9
    assert pelicula.id == -1
    assert pelicula.director is None

def test_create_pelicula_and_informar_director_completo():
    director = Director("Peter Jackson", 9)
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", director)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._director_id == 9
    assert pelicula.id == -1
    assert pelicula.director is director

def test_asigna_director_a_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Sauron es muy malo", -1)
    director = Director("Peter Jackson", 9)

    pelicula.director = director

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es muy malo"
    assert pelicula._director_id == 9
    assert pelicula.id == -1
    assert pelicula.director == director

def test_dao_peliculas_traer_todos():
    dao = DAO_CSV_Pelicula("tests/data/peliculas.csv")
    peliculas = dao.todos()

    assert len(peliculas) == 5
    assert peliculas[1] == Pelicula("Los siete samuráis", "Una banda de forajidos atemorizan a los habitantes de un pequeño pueblo, saqueándolos periódicamente sin piedad. Para repeler estos ataques, los aldeanos deciden contratar a mercenarios. Finalmente, consiguen los servicios de 7 guerreros, 7 samurais dispuestos a defenderlos a cambio, tan solo, de cobijo y comida.", 2, 17)

def test_dao_peliculas_guardar_pelicula():
    dao = DAO_CSV_Pelicula("tests/data/peliculas.csv")
    
    # Guardar una nueva película
    nueva_pelicula = Pelicula("Nueva Pelicula", "Sinopsis de prueba", 3, 66)
    dao.guardar(nueva_pelicula)
    
    # Consultar todas las películas y verificar que se ha añadido
    peliculas = dao.todos()
    assert len(peliculas) == 6
    assert peliculas[-1] == nueva_pelicula
    
    # Borrar la película recién añadida para restaurar el estado original
    dao.borrar(66)
    
    # Consultar todas las películas y verificar que se ha eliminado
    peliculas = dao.todos()
    assert len(peliculas) == 5
    assert nueva_pelicula not in peliculas

def test_dao_peliculas_consultar():
    dao = DAO_CSV_Pelicula("tests/data/peliculas.csv")
    pelicula = dao.consultar(17)

    assert pelicula == Pelicula("Los siete samuráis", "Una banda de forajidos atemorizan a los habitantes de un pequeño pueblo, saqueándolos periódicamente sin piedad. Para repeler estos ataques, los aldeanos deciden contratar a mercenarios. Finalmente, consiguen los servicios de 7 guerreros, 7 samurais dispuestos a defenderlos a cambio, tan solo, de cobijo y comida.", 2, 17)

def test_dao_peliculas_borrar_pelicula():
    dao = DAO_CSV_Pelicula("tests/data/peliculas.csv")
    
    dao.borrar(64)
    peliculas = dao.todos()

    assert len(peliculas) == 4
    assert Pelicula("El infierno del odio", "En un momento crucial de su vida financiera, Gondo, un hombre de negocios, recibe la noticia de que su hijo ha sido secuestrado, y el rescate exigido es una cantidad de dinero similar a la que necesita para cerrar una importante negociación. Gondo está dispuesto a pagar el rescate hasta que comprende que los secuestradores se han equivocado y se han llevado al hijo del chófer. Ahora deberá decidir si el dinero es más importante que la vida del niño.", 2, 64) not in peliculas

    dao.guardar(Pelicula("El infierno del odio", "En un momento crucial de su vida financiera, Gondo, un hombre de negocios, recibe la noticia de que su hijo ha sido secuestrado, y el rescate exigido es una cantidad de dinero similar a la que necesita para cerrar una importante negociación. Gondo está dispuesto a pagar el rescate hasta que comprende que los secuestradores se han equivocado y se han llevado al hijo del chófer. Ahora deberá decidir si el dinero es más importante que la vida del niño.", 2, 64))

def test_dao_peliculas_actualizar_pelicula():
    dao = DAO_CSV_Pelicula("tests/data/peliculas.csv")
    
    pelicula = dao.consultar(6)
    pelicula.titulo = "Un amor contra viento y marea Actualizada"
    dao.actualizar(pelicula)
    
    pelicula_actualizada = dao.consultar(6)
    assert pelicula_actualizada.titulo == "Un amor contra viento y marea Actualizada"

    pelicula.titulo = "Un amor contra viento y marea"  # Restaurar valor original
    dao.actualizar(pelicula)

def test_create_genero():
    genero = Generos("Accion", 1)

    assert genero.genero == "Accion"
    assert genero.id == 1

def test_dao_generos_traer_todos():
    dao = DAO_CSV_Generos("tests/data/generos.csv")
    generos = dao.todos()

    assert len(generos) == 14
    assert generos[0] == Generos("Accion", 1)

def test_dao_generos_guardar_genero():
    dao = DAO_CSV_Generos("tests/data/generos.csv")
    
    nuevo_genero = Generos("Ciencia Ficcion", 14)
    dao.guardar(nuevo_genero)
    generos = dao.todos()

    assert len(generos) == 15
    assert generos[-1] == nuevo_genero

    dao.borrar(14)
    generos = dao.todos()
    assert len(generos) == 14

def test_dao_generos_consultar():
    dao = DAO_CSV_Generos("tests/data/generos.csv")
    genero = dao.consultar(3)

    assert genero == Generos("Aventura", 3)

def test_dao_generos_borrar_genero():
    dao = DAO_CSV_Generos("tests/data/generos.csv")
    
    dao.borrar(13)
    generos = dao.todos()

    assert len(generos) == 13
    assert Generos("Western", 13) not in generos

    dao.guardar(Generos("Western", 13))
    generos = dao.todos()
    assert len(generos) == 14

def test_dao_generos_actualizar_genero():
    dao = DAO_CSV_Generos("tests/data/generos.csv")
    
    genero = dao.consultar(1)
    original_genero = genero.genero
    genero.genero = "Accion Actualizada"
    dao.actualizar(genero)
    
    genero_actualizado = dao.consultar(1)
    assert genero_actualizado.genero == "Accion Actualizada"

    genero.genero = original_genero  # Restaurar valor original
    dao.actualizar(genero)
    genero_restaurado = dao.consultar(1)
    assert genero_restaurado.genero == original_genero

def test_create_copias():
    copia = Copias(1, 1)

    assert copia.id_pelicula == 1
    assert copia.id == 1

def test_dao_copias_traer_todos():
    dao = DAO_CSV_Copias("tests/data/copias.csv")
    copias = dao.todos()

    assert len(copias) == 9
    assert copias[0] == Copias(1, 1)

def test_dao_copias_guardar_copia():
    dao = DAO_CSV_Copias("tests/data/copias.csv")
    
    nueva_copia = Copias(5, 10)
    dao.guardar(nueva_copia)
    copias = dao.todos()

    assert len(copias) == 10
    assert copias[-1] == nueva_copia

    dao.borrar(10)

def test_dao_copias_consultar():
    dao = DAO_CSV_Copias("tests/data/copias.csv")
    copia = dao.consultar(1)

    assert copia == Copias(1, 1)

def test_dao_copias_borrar_copia():
    dao = DAO_CSV_Copias("tests/data/copias.csv")
    
    dao.borrar(9)
    copias = dao.todos()

    assert len(copias) == 8
    assert Copias(4, 9) not in copias

    dao.guardar(Copias(4, 9))

def test_dao_copias_actualizar_copia():
    dao = DAO_CSV_Copias("tests/data/copias.csv")
    
    copia = dao.consultar(1)
    copia.id_pelicula = 2
    dao.actualizar(copia)
    
    copia_actualizada = dao.consultar(1)
    assert copia_actualizada.id_pelicula == 2

    copia.id_pelicula = 1  # Restaurar valor original
    dao.actualizar(copia)