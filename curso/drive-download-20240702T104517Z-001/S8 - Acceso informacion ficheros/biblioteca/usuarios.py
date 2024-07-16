import utils

class Usuario:
    def __init__(self, dni, email, nombre, apellido):
        self.dni = dni
        self.email = email
        self.nombre = nombre
        self.apellido = apellido 

class GestionUsuarios:
    def __init__(self):
        self.usuariosDB = []

    def menu_usuarios(self):
        while True:
            print("---Gestión de Usuarios---")
            print("1: Añadir un usuario")
            print("2: Eliminar un usuario (por dni)")
            print("3: Buscar usuarios")
            print("4: Mostrar todos los usuarios")
            print("5: Generar JSON de todos los usuarios")
            print("6: Volver al menú principal")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                dni = input("Introduce el dni del usuario: ").upper()
                email = input("Introduce el email del usuario: ").lower()
                nombre = input("Introduce el nombre del usuario: ")
                apellido = input("Introduce el apellido del usuario: ")
                self.anadir_usuario(dni, email, nombre, apellido)

            if opcion == "2":
                dni = input("Introduce el DNI del usuario que quieres eliminar: ")
                self.eliminar_usuario(dni)

            if opcion == "3":
                busqueda = input("Introduce el dni ó email del usuario a buscar: ")
                resultados = self.buscar_usuario(busqueda, busqueda)
                if resultados:
                    print("Resultados de la búsqueda: ")
                    for usuario in resultados:
                        print(f"DNI: {usuario.dni}, Email: {usuario.email}, Nombre: {usuario.nombre}, Apellido: {usuario.apellido}")
                else:
                    print ("No se encontraron resultados")

            if opcion == "4":
                self.mostrar_usuarios()

            if opcion == "5":
                utils.exportar_json(self.usuariosDB, "usuarios.json")
                print("Se ha generado el archivo JSON con todos los usuarios")

            
            elif opcion == "6":
                break
    
    def anadir_usuario(self, d, e, n, a):

        if not utils.validar_dni_format(d):
            print("DNI con formato incorrecto")
            return
        
        if not utils.validar_dni_unique(d, self.usuariosDB):
            print("DNI ya registrado")
            return

        usuario = Usuario(d, e, n, a)
        self.usuariosDB.append(usuario)
        print(f"Usuario añadido: {usuario.__dict__}")

    def eliminar_usuario(self, d):
        for usuario in self.usuariosDB:
            if usuario.dni == d:
                self.usuariosDB.remove(usuario)
                print(f"Usuario con dni {d} borrado")
                return
        print("Usuario no encontrado")

    def buscar_usuario(self, dni=None, email=None): # Si no llega valor al param, toma el valor None
        resultados = []
        for usuario in self.usuariosDB:
            if dni and dni.lower() == usuario.dni.lower():
                resultados.append(usuario)
            elif email and email.lower() == usuario.email.lower():
                resultados.append(usuario)
        return resultados

    def mostrar_usuarios(self):
        if self.usuariosDB:
            print("Usuarios registrados: ")
            for usuario in self.usuariosDB:
                print(f"DNI: {usuario.dni}, Email: {usuario.email}, Nombre: {usuario.nombre}, Apellido: {usuario.apellido}")
        else:
            print("No hay usuarios registrados")
    