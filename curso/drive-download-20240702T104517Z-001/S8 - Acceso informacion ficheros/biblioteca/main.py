from libros import GestionLibros
from usuarios import GestionUsuarios
from prestamos import GestionPrestamos

def menu_principal(gestionLibros, gestionUsuarios, gestionPrestamos):
    while True:
        print("---Gestión Biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestionLibros.menu_libros()
        elif opcion == "2":
            gestionUsuarios.menu_usuarios()
        elif opcion == "3":
            gestionPrestamos.menu_prestamos()
        elif opcion == "4":
            print("Gracias por utilizar nuestra app")
            break
        else:
            print("Opción no válida. Inténtalo otra vez")

# instancias
gestionLibros = GestionLibros()
gestionUsuarios = GestionUsuarios()
gestionPrestamos = GestionPrestamos(gestionLibros, gestionUsuarios)
# carga el menu principal
menu_principal(gestionLibros, gestionUsuarios, gestionPrestamos)










