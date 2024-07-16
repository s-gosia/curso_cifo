import utils

# Nuestra Base de Datos (temporal) para gestionar los prestamos
prestamos = []

def menu_prestamos():
    while True:
        print("---Gestión de Préstamos---")
        print("1: Añadir un préstamo")
        print("2: Eliminar un préstamos (por dni ó isbn)")
        print("3: Buscar préstamos por usuario (dni)")
        print("4: Mostrar todos los préstamos")
        print("5: Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dni = input("Introduce el dni del usuario: ").upper()
            isbn = input("Introduce el isbn del libro: ")
            fecha = input("Introduce la fecha del préstamo: ")
            anadir_prestamo(dni, isbn, fecha)

        if opcion == "2":
            busqueda = input("Introduce el DNI ó ISBN del préstamo que quieres eliminar: ")
            eliminar_prestamo(busqueda, busqueda)

        if opcion == "3":
            busqueda = input("Introduce el DNI ó ISBN del préstamo a buscar")
            resultados = buscar_prestamo(busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for prestamo in resultados:
                    print(f"DNI: {prestamo["dni"]}, ISBN: {prestamo["isbn"]}, Fecha: {prestamo["fecha"]}")
            else:
                print ("No se encontraron resultados")

        if opcion == "4":
            mostrar_prestamos()
        
        elif opcion == "5":
            break

def anadir_prestamo(dni, isbn, fecha):
    
    if not utils.validar_prestamo_unique(dni, prestamos):
        print("DNI ya registrado")
        return

    prestamo = {
        "dni": dni,
        "isbn": isbn,
        "fecha": fecha
    }
    prestamos.append(prestamo)
    print(f"Préstamo añadido: {prestamo}")

def eliminar_prestamo(dni=None, isbn=None):
    for prestamo in prestamos:
        if prestamo["dni"] == dni or prestamo["isbn"] == isbn:
            prestamos.remove(prestamo)
            print(f"Préstamo borrado")
            return
    print("Préstamo no encontrado")

def buscar_prestamo(dni=None, isbn=None): # Si no llega valor al param, toma el valor None
    resultados = []
    for prestamo in prestamos:
        if dni and dni.lower() == prestamo["dni"].lower():
            resultados.append(prestamo)
        elif isbn and isbn.lower() == prestamo["isbn"].lower():
            resultados.append(prestamo)
    return resultados

def mostrar_prestamos():
    if prestamos:
        print("Préstamos registrados: ")
        for prestamo in prestamos:
            print(f"DNI: {prestamo["dni"]}, ISBN: {prestamo["isbn"]}, Fecha: {prestamo["fecha"]}")
    else:
        print("No hay prestamos registrados")
    
