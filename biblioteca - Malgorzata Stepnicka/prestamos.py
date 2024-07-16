import utils
prestamos = []

def registrar_prestamo(dni, isbn, fecha):
    
    if not utils.validar_dni_format(dni):
        print("El formato del DNI incorrecto")
        return
    
    if not utils.validar_isbn_prestado(isbn, prestamos):
        print(f"El libro con ISBN {isbn} ya esta prestado.")
        return
    
    if not utils.validar_isbn_format(isbn):
        print("ISBN incorrecto.")
        return
        
    prestamo = {
        "dni": dni,
        "isbn": isbn,
        "fecha": fecha
    }
    prestamos.append(prestamo)
    print(f"Prestamo '{prestamo}' creado correctamente.")

def devolver_libro(isbn):

    if not utils.validar_isbn_format(isbn):
        print("ISBN incorrecto.")

    for prestamo in prestamos:
        if prestamo["isbn"] == isbn:
            prestamos.remove(prestamo)
            print(f"Libro con ISBN {isbn} devuelto correctamente.")
            return
        else:
            print("Libro no prestado.")

def buscar_prestamo(busqueda):
       
    resultados = []
    for prestamo in prestamos:
        if (busqueda.lower() in prestamo["dni"].lower() or 
            busqueda.lower() in prestamo["isbn"].lower() or 
            busqueda.lower() in prestamo["fecha"].lower()):
            resultados.append(prestamo)
    if resultados:
        for resultado in resultados:
            print(f"Encontrado: {resultado}")
    else:
        print("No se encontraron resultados.")

def mostrar_todos_prestamos():
    if prestamos:
        for prestamo in prestamos:
            print(prestamo)
    else:
        print("No hay prestamos en la biblioteca.")

def menu_prestamos():
    while True:
        print("---Gestión de prestamos---")
        print("1. Registrar un prestamo")
        print("2. Devolver un libro")
        print("3. Buscar prestamos")
        print("4. Mostrar todos los prestamos")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dni = input("Introduce el DNI: ")
            isbn = input("Introduce el ISBN: ")
            fecha = input("Introduce la fecha del prestamo: ")
            registrar_prestamo(dni, isbn, fecha)

        elif opcion == "2":
            devolver_isbn = input("Introduce ISBN del libro para eliminar: ")
            devolver_libro(devolver_isbn)

        elif opcion == "3":
            busqueda = input("Busca un DNI, ISBN o fecha: ")
            buscar_prestamo(busqueda)

        elif opcion == "4":
            mostrar_todos_prestamos()

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Inténtalo otra vez.")

menu_prestamos()