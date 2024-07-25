from simple_screen import locate, DIMENSIONS, Input

class VistaTituloPagina:
    def __init__(self, texto: str, y: int = 0) -> None:
        self.texto = texto
        self.y = y
    
    def paint(self):
        x = (DIMENSIONS.w - len(self.texto)) // 2
        locate(x, self.y, self.texto)

class VistaCatalogo:
    def __init__(self, peliculas, x, y, w, num_filas) -> None:
        self. x = x
        self.y = y
        self.w = w
        self.num_filas = num_filas
        self.peliculas = peliculas
    
    def paint(self):
        locate(self.x, self.y, "Título")
        locate(self.x + 15, self.y, "| Director")
        locate(self.x + 30, self.y, "| Sinopsis")

        locate(self.x, self.y + 1, "--------------+--------------+--------------------------------------------------")
        
        contador = 0
        for pelicula in self.peliculas:
            if contador and contador % self.num_filas == 0:
                locate(self.x, self.y + 2 + contador)
                Input("Pulsa Enter para continuar")
                self.__cls()
                contador = 0

            locate(self.x, self.y + 2 + contador, pelicula.titulo[:14])
            locate(self.x + 15, self.y + 2 + contador, f"| {pelicula.id}")
            locate(self.x + 30, self.y + 2 + contador, f"| {pelicula.sinopsis[:30]}")
            contador += 1
    
    def __cls(self):
        locate(self.x, self.y, "Título")
        locate(self.x + 15, self.y, "| Director")
        locate(self.x + 30, self.y, "| Sinopsis")

        locate(self.x, self.y + 1, "--------------+--------------+--------------------------------------------------")

        for contador, pelicula in enumerate(self.peliculas):
            locate(self.x, self.y + 2 + contador, " " * 14)
            locate(self.x + 15, self.y + 2 + contador, f"| {' ' * 14}")
            locate(self.x + 30, self.y + 2 + contador, f"| {' ' * 48}")
        locate(self.x, self.y + 3 + contador, " " * 80)
