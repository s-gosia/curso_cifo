from prestamos import GestionPrestamos

def mostrar_menu(gestion_prestamos):
    while True:
        print("--Gestión Prestamos--")
        print("1: Añadir Prestamos")
        print("2: Eliminar Prestamos (isbn)")
        print("3: Buscar Prestamos (dni)")
        print("4: Mostrar todos los prestamos")
        print("5: Salir")
    
        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestion_prestamos.anadir_prestamo()
        elif opcion == "2":
            gestion_prestamos.borrar_prestamo()
        elif opcion == "3":
            gestion_prestamos.mostrar_prestamo()
        elif opcion == "4":
            gestion_prestamos.mostrar_prestamo()
        elif opcion == "5":
            print("Bye")
            break
        else:
            print("Opción no válida")

# instancia
gestion_prestamos = GestionPrestamos()

mostrar_menu(gestion_prestamos)