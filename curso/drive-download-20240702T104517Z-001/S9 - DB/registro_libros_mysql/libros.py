from registro_libros_mysql.libros import utils

class Libro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class GestionLibros:
    def anadir_libro(self):
        titulo = input("Introduce el titulo: ")
        autor = input("Introduce el autor: ")
        isbn = input("Introduce ISBN: ")
        genero = input("Introduce el genero: ")

        if not utils.validar_isbn_format(isbn):
            return "ISBN no valido"
        
        libro = Libro(titulo, autor, isbn, genero)
        utils.set_data_db(libro)

    def borrar_libro(self):
        isbn = input("Introduce el ISBN del libro: ")
        if utils.delete_data_db(isbn):
            print(f"Libro con ISBN {isbn} borrado")
        else:
            print(f"Libro con ISBN {isbn} no registrado")
        
    def mostrar_libro(self):
        isbn = input("Introduce el ISBN del libro: ")
        if utils.find_data_db(isbn):
            libro = utils.find_data_db(isbn)
            print(libro)
        else:
            print("No se ha encontrado el libro con ISBN " + isbn)
    
    def mostrar_libros(self):
        if not utils.get_data_db():
            print("No hay libros registrados")
        else:
            print(utils.get_data_db())
