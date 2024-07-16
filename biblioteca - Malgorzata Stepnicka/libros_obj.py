class libro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.isbn}, {self.genero}"
    

libro1 = libro("book", "autor", 54455564, "genero")
print(libro1)