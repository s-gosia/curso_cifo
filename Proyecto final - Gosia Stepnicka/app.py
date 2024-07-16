def menu_principal(): 
   
    while True:

        print("---Gestión de registro de perros---")
        print("1. Gestión de usuarios")
        print("2. Gestión de perros")
        print("3. Gestión de registro")
        print("4. Salir")

        opcion = input("Elije una opción ")

        if opcion == "1":
            import app_usuarios
            app_usuarios.ApiUsuarios()
        elif opcion == "2":
            import app_perros
            app_perros.ApiPerros()
        elif opcion == "3":
            import app_registro
            app_registro.ApiRegistro()
        elif opcion == "4":
           print("Gracias por utilizar nuestra app")
           break
        else: 
            print("Opción no valida. Intentalo otra vez")

menu_principal()