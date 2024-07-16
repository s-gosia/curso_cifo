def menu_principal(): 
   
    while True:

        print("---Gestión biblioteca---")
        print("1. Gestión de libros")
        print("2. Gestión de usuarios")
        print("3. Gestión de prestamo")
        print("4. Salir")

        opcion = input("Elije una opción ")

        if opcion == "1":
            import libros
            libros.menu_libros()
        elif opcion == "2":
            import usuarios
            usuarios.menu_usuarios()
        elif opcion == "3":
            import prestamos
            prestamos.menu_prestamos()
        elif opcion == "4":
           print("Gracias por utilizar nuestra app")
           break
        else: 
            print("Opción no valida. Intentalo otra vez")

menu_principal()