from app.modelos import Director, DAO_CSV_Director

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
    directores = dao.todos()
    alfred = dao.consultar(3)

    assert alfred == Director("Alfred Hitchcock", 3)

def test_dao_directores_borrar_director():
    dao = DAO_CSV_Director("tests/data/directores.csv")
       
    dao.borrar(8)
    directores = dao.todos()

    assert len(directores) == 7
    assert Director("Charlie Chaplin", 8) not in directores

    dao.guardar(Director("Charlie Chaplin", 8))