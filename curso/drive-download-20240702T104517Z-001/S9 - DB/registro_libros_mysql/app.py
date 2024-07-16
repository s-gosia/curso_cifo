from libros import GestionLibros

def mostrar_menu(gestion_libros):
    while True:
        print("--Gestión Libros--")
        print("1: Añadir Libro")
        print("2: Eliminar Libro (isbn)")
        print("3: Buscar Usuario (isbn)")
        print("4: Mostrar todos los libros")
        print("5: Salir")
    
        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestion_libros.anadir_libro()
        elif opcion == "2":
            gestion_libros.borrar_libro()
        elif opcion == "3":
            gestion_libros.mostrar_libro()
        elif opcion == "4":
            gestion_libros.mostrar_libro()
        elif opcion == "5":
            print("Bye")
            break
        else:
            print("Opción no válida")

# instancia
gestion_libros = GestionLibros()

mostrar_menu(gestion_libros)