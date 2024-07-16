import utils

usuarios = []

def anadir_usuario(nombre, apellido, dni, email):
    if not utils.validar_dni_unique(dni, usuarios):
        print(f"Usuario con el DNI {dni} ya existe.")
        return
    
    if not utils.validar_dni_format(dni):
        print("El formato del DNI incorrecto")
        return
        
    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "email": email
    }
    usuarios.append(usuario)
    print(f"Usuario '{usuario}' añadido correctamente.")

def eliminar_usuario(dni):
    for usuario in usuarios:
        if usuario["dni"] == dni:
            usuarios.remove(usuario)
            print(f"Usuario con DNI {dni} eliminado correctamente.")
            return
    print("Usuario no existe.")

def buscar_usuario(busqueda):
    resultados = []
    for usuario in usuarios:
        if (busqueda.lower() in usuario["nombre"].lower() or 
            busqueda.lower() in usuario["apellido"].lower() or 
            busqueda.lower() in usuario["dni"].lower() or 
            busqueda.lower() in usuario["email"].lower()):
            resultados.append(usuario)
    if resultados:
        for resultado in resultados:
            print(f"Encontrado: {resultado}")
    else:
        print("No se encontraron resultados.")

def mostrar_todos_usuarios():
    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print("No hay usuarios en la biblioteca.")

def menu_usuarios():
    while True:
        print("---Gestión de usuarios---")
        print("1. Añadir un usuario")
        print("2. Eliminar un usuario")
        print("3. Buscar usuarios")
        print("4. Mostrar todos los usuarios")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre: ")
            apellido = input("Introduce el apellido: ")
            dni = input("Introduce el DNI: ")
            email = input("Introduce el email: ")
            anadir_usuario(nombre, apellido, dni, email)

        elif opcion == "2":
            eliminar_dni = input("Introduce DNI del usuario para eliminar: ")
            eliminar_usuario(eliminar_dni)

        elif opcion == "3":
            busqueda = input("Busca un nombre, apellido, dni o email: ")
            buscar_usuario(busqueda)

        elif opcion == "4":
            mostrar_todos_usuarios()

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Inténtalo otra vez.")

menu_usuarios()