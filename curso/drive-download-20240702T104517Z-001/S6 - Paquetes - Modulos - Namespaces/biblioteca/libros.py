import utils

# Nuestra Base de Datos (temporal) para gestionar los libros
libros = []

def menu_libros():
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
            anadir_libro(titulo, autor, isbn, genero)

        if opcion == "2":
            isbn = input("Introduce el ISBN del libro que quieres eliminar: ")
            eliminar_libro(isbn)

        if opcion == "3":
            busqueda = input("Introduce el titulo, autor, o isbn del libro que quieres buscar")
            resultados = buscar_libro(busqueda, busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for resultado in resultados:
                    print(f"Titulo: {resultado["titulo"]}, Autor: {resultado["autor"]}, ISBN: {resultado["isbn"]}, Género: {resultado["genero"]}")
            else:
                print ("No se encontraron resultados")

        if opcion == "4":
            mostrar_libros()
        
        elif opcion == "5":
            break

def anadir_libro(t, a, isbn, g):

    if not utils.validar_isbn_format(isbn):
        print("ISBN con formato incorrecto")
        return

    if not utils.validar_isbn_unique(isbn, libros):
        print("ISBN ya existente")
        return

    libro = {
        "titulo": t,
        "autor": a,
        "isbn": isbn,
        "genero": g
    }
    libros.append(libro)
    print(f"Libro añadido: {libro}")

def eliminar_libro(isbn):
    for libro in libros:
        if libro["isbn"] == isbn:
            libros.remove(libro)
            print(f"Libro con isbn {isbn} borrado")
            return
    print("Libro no encontrado")

def buscar_libro(titulo=None, autor=None, isbn=None): # Si no llega valor al param, toma el valor None
    resultados = []
    for libro in libros:
        if titulo and titulo.lower() == libro["titulo"].lower():
            resultados.append(libro)
        elif autor and autor.lower() == libro["autor"].lower():
            resultados.append(libro)
        elif isbn and isbn == libro["isbn"]:
            resultados.append(libro)
    return resultados

def mostrar_libros():
    if libros:
        print("Libros disponibles: ")
        for libro in libros:
            print(f"Titulo: {libro["titulo"]}, Autor: {libro["autor"]}, ISBN: {libro["isbn"]}, Género: {libro["genero"]}")
    else:
        print("No hay libros disponibles")
    
