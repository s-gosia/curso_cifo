from registro_usuarios_mysql.usuarios import utils

class Usuario:
    def __init__(self, dni, nombre, email, password):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.password = password

class GestionUsuarios:
    def anadir_usuario(self):
        dni = input("Introduce tu dni: ")
        nombre = input("Introduce tu nombre: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu password: ")
        
        if not utils.validar_dni(dni):
            print("DNI no válido")
            return
        if not utils.validar_nombre(nombre):
            print("Nombre no válido")
            return
        if not utils.validar_email(email):
            print("Email no válido")
            return
        if not utils.validar_password(password):
            print("Password no válido. Debe contener al menos 8 caracteres, incluyendo letras y números")
            return
        
        usuario = Usuario(dni, nombre, email, password)
        utils.set_data_db(usuario)

    def borrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if utils.delete_data_db(dni):
            print(f"Usuario con dni {dni} borrado")
        else:
            print(f"Usuario con dni {dni} no registrado")
        
    def mostrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if utils.find_data_db(dni):
            usuario = utils.find_data_db(dni)
            print(usuario)
        else:
            print("No se ha encontrado el usuario con dni " + dni)
    
    def mostrar_usuarios(self):
        if not utils.get_data_db():
            print("No hay usuarios registrados")
        else:
            print(utils.get_data_db())
