import libros
import usuarios
import prestamos

def menu_principal():
    while True:
        print("---Gestión Biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            libros.menu_libros()
        elif opcion == "2":
            usuarios.menu_usuarios()
        elif opcion == "3":
            prestamos.menu_prestamos()
        elif opcion == "4":
           print("Gracias por utilizar nuestra app")
           break
        else:
            print("Opción no válida. Inténtalo otra vez")


menu_principal()










