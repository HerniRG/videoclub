from app.daos import DAO_CSV_Pelicula
from app.vistas import VistaCatalogo, VistaTituloPagina
from simple_screen import locate, DIMENSIONS, Input, cls, Screen_manager

class VideoClub:
    def __init__(self) -> None:
        self.tituloPagina = VistaTituloPagina("CATALOGO VC")
        self.titulo2 = VistaTituloPagina("===========") 

        self.vista_catalogo = VistaCatalogo([], 0, 2, 0, 3)
        self.daoPelis = DAO_CSV_Pelicula("tests/data/peliculas.csv")
    
    def run(self):
        continuar = "S"
        with Screen_manager:
            while continuar.upper() == "S":
                cls()
                peliculas = self.daoPelis.todos()
                self.vista_catalogo.peliculas = peliculas

                self.tituloPagina.paint()
                self.titulo2.paint()
                self.vista_catalogo.paint()            
            
                locate(0, DIMENSIONS.h -1, "Repetir (S/N)")
                continuar = Input()