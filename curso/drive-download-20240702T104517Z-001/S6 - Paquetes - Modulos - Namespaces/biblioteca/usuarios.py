import utils

# Nuestra Base de Datos (temporal) para gestionar los Usuarios
usuarios = []

def menu_usuarios():
    while True:
        print("---Gestión de Usuarios---")
        print("1: Añadir un usuario")
        print("2: Eliminar un usuario (por dni)")
        print("3: Buscar usuarios")
        print("4: Mostrar todos los usuarios")
        print("5: Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dni = input("Introduce el dni del usuario: ").upper()
            email = input("Introduce el email del usuario: ").lower()
            nombre = input("Introduce el nombre del usuario: ")
            apellido = input("Introduce el apellido del usuario: ")
            anadir_usuario(dni, email, nombre, apellido)

        if opcion == "2":
            dni = input("Introduce el DNI del usuario que quieres eliminar: ")
            eliminar_usuario(dni)

        if opcion == "3":
            busqueda = input("Introduce el dni ó email del usuario a buscar")
            resultados = buscar_usuario(busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for usuario in resultados:
                    print(f"DNI: {usuario["dni"]}, Email: {usuario["email"]}, Nombre: {usuario["nombre"]}, Apellido: {usuario["apellido"]}")
            else:
                print ("No se encontraron resultados")

        if opcion == "4":
            mostrar_usuarios()
        
        elif opcion == "5":
            break

def anadir_usuario(d, e, n, a):
    
    if not utils.validar_dni_format(d):
        print("DNI con formato incorrecto")
        return
    
    if not utils.validar_dni_unique(d, usuarios):
        print("DNI ya registrado")
        return

    usuario = {
        "dni": d,
        "email": e,
        "nombre": n,
        "apellido": a
    }
    usuarios.append(usuario)
    print(f"Usuario añadido: {usuario}")

def eliminar_usuario(d):
    for usuario in usuarios:
        if usuario["dni"] == d:
            usuarios.remove(usuario)
            print(f"Usuario con dni {d} borrado")
            return
    print("Usuario no encontrado")

def buscar_usuario(dni=None, email=None): # Si no llega valor al param, toma el valor None
    resultados = []
    for usuario in usuarios:
        if dni and dni.lower() == usuario["dni"].lower():
            resultados.append(usuario)
        elif email and email.lower() == usuario["email"].lower():
            resultados.append(usuario)
    return resultados

def mostrar_usuarios():
    if usuarios:
        print("Usuarios registrados: ")
        for usuario in usuarios:
            print(f"DNI: {usuario["dni"]}, Email: {usuario["email"]}, Nombre: {usuario["nombre"]}, Apellido: {usuario["apellido"]}")
    else:
        print("No hay usuarios registrados")
    
