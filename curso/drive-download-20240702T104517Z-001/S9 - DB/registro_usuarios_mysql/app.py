from usuarios import GestionUsuarios

def mostrar_menu(gestion_usuarios):
    while True:
        print("--Gestión Usuarios--")
        print("1: Añadir Usuario")
        print("2: Eliminar Usuario (dni)")
        print("3: Buscar Usuario (dni)")
        print("4: Mostrar todos los Usuarios")
        print("5: Salir")
    
        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestion_usuarios.anadir_usuario()
        elif opcion == "2":
            gestion_usuarios.borrar_usuario()
        elif opcion == "3":
            gestion_usuarios.mostrar_usuario()
        elif opcion == "4":
            gestion_usuarios.mostrar_usuarios()
        elif opcion == "5":
            print("Bye")
            break
        else:
            print("Opción no válida")

# instancia
gestion_usuarios = GestionUsuarios()

mostrar_menu(gestion_usuarios)