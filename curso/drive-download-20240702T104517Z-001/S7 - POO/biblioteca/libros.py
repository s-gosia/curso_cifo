import utils

class Libro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

# Clase que contiene la gestión de todas las acciones sobre la entidad Libro
class GestionLibros:
    def __init__(self):
        self.librosDB = [] # database

    # Métodos de gestion libros
    # 1- Método de Imprimir el menu de Libros
    def menu_libros(self):
        while True:
            print("---Gestión de Libros---")
            print("1: Añadir un libro")
            print("2: Eliminar un libro (por isbn)")
            print("3: Buscar libros")
            print("4: Mostrar todos los libros")
            print("5: Volver al menú principal")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                titulo = input("Introduce el título del libro: ")
                autor = input("Introduce el autor del libro: ")
                isbn = input("Introduce el ISBN del libro: ")
                genero = input("Introduce el genero del libro: ")
                self.anadir_libro(titulo, autor, isbn, genero)
            
            elif opcion == "2":
                isbn = input("Introduce el ISBN del libro que quieres eliminar: ")
                self.eliminar_libro(isbn)
            if opcion == "3":
                busqueda = input("Introduce el titulo, autor, o isbn del libro que quieres buscar: ")
                resultados = self.buscar_libro(busqueda, busqueda, busqueda)
                if resultados:
                    print("Resultados de la búsqueda: ")
                    for resultado in resultados:
                        print(f"Titulo: {resultado.titulo}, Autor: {resultado.autor}, ISBN: {resultado.isbn}, Género: {resultado.genero}")
                else:
                    print ("No se encontraron resultados")

            if opcion == "4":
                self.mostrar_libros()
        
            elif opcion == "5":
                break

    def anadir_libro(self, titulo, autor, isbn, genero):
        if not utils.validar_isbn_format(isbn):
            print("ISBN con formato incorrecto")
            return

        if not utils.validar_isbn_unique(isbn, self.librosDB):
            print("ISBN ya existente")
            return
        
        libro = Libro(titulo, autor, isbn, genero)
        self.librosDB.append(libro)
        print(f"Libro añadido: {libro.__dict__}")

    def eliminar_libro(self, isbn):
        for libro in self.librosDB:
            if libro.isbn == isbn:
                self.librosDB.remove(libro)
                print(f"Libro con isbn {isbn} borrado")
                return
        print("Libro no encontrado")

    def buscar_libro(self, titulo=None, autor=None, isbn=None): # Si no llega valor al param, toma el valor None
        resultados = []
        for libro in self.librosDB:
            if titulo and titulo.lower() == libro.titulo.lower():
                resultados.append(libro)
            elif autor and autor.lower() == libro.autor.lower():
                resultados.append(libro)
            elif isbn and isbn == libro.isbn:
                resultados.append(libro)
        return resultados
    
    def mostrar_libros(self):
        if self.librosDB:
            print("Libros disponibles: ")
            for libro in self.librosDB:
                print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Género: {libro.genero}")
        else:
            print("No hay libros disponibles")