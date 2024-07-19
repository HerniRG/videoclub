from app.modelos import Director, Pelicula, DAO_CSV_Director, DAO_CSV_Pelicula

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