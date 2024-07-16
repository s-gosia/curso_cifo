import utils

libros = []

def anadir_libro(titulo, autor, isbn, genero):
    if not utils.validar_isbn_unique(isbn, libros):
        print(f"Libro con el ISBN {isbn} ya existe.")
        return
    
    if not utils.validar_isbn_format(isbn):
        print("El formato del ISBN incorrecto")
        return
    
    libro = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "genero": genero
    }
    libros.append(libro)
    print(f"Libro '{titulo}' añadido correctamente.")

def eliminar_libro(isbn):
    for libro in libros:
        if libro["isbn"] == isbn:
            libros.remove(libro)
            print(f"Libro con ISBN {isbn} eliminado correctamente.")
            return
    print("Libro no existe.")

def buscar_libros(busqueda):
    resultados = []
    for libro in libros:
        if (busqueda.lower() in libro["titulo"].lower() or 
            busqueda.lower() in libro["autor"].lower() or 
            busqueda.lower() in libro["isbn"].lower() or 
            busqueda.lower() in libro["genero"].lower()):
            resultados.append(libro)
    if resultados:
        for resultado in resultados:
            print(f"Encontrado: {resultado}")
    else:
        print("No se encontraron resultados.")

def mostrar_todos_libros():
    if libros:
        for libro in libros:
            print(libro)
    else:
        print("No hay libros en la biblioteca.")

def menu_libros():
    while True:
        print("---Gestión de libros---")
        print("1. Añadir un libro")
        print("2. Eliminar un libro")
        print("3. Buscar libros")
        print("4. Mostrar todos los libros")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            genero = input("Introduce el género del libro: ")
            anadir_libro(titulo, autor, isbn, genero)

        elif opcion == "2":
            eliminar_isbn = input("Introduce ISBN del libro para eliminar: ")
            eliminar_libro(eliminar_isbn)

        elif opcion == "3":
            busqueda = input("Busca un título, autor, ISBN o género: ")
            buscar_libros(busqueda)

        elif opcion == "4":
            mostrar_todos_libros()

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Inténtalo otra vez.")

menu_libros()
