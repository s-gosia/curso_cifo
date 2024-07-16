from registro_prestamos_mysql.prestamos import utils

class Prestamo:
    def __init__(self, dni_usuario, isbn_libro, fecha_prestamo):
        self.dni_usuario = dni_usuario
        self.isbn_libro = isbn_libro
        self.fecha_prestamo = fecha_prestamo

class GestionPrestamos:
    def anadir_prestamo(self):
        dni_usuario = input("Introduce el DNI: ")
        isbn_libro = input("Introduce el ISBN: ")
        fecha_prestamo = input("Introduce la fecha del prestamo: ")

        if not utils.validar_isbn_format(isbn_libro):
            return "ISBN no valido"
        
        prestamo = Prestamo(dni_usuario, isbn_libro, fecha_prestamo)
        utils.set_data_db(prestamo)

    def borrar_prestamo(self):
        isbn_libro = input("Introduce el ISBN del libro: ")
        if utils.delete_data_db(isbn_libro):
            print(f"Libro con ISBN {isbn_libro} borrado")
        else:
            print(f"Libro con ISBN {isbn_libro} no registrado")
        
    def mostrar_prestamo(self):
        dni_usuario = input("Introduce el DNI del usuario: ")
        if utils.find_data_db(dni_usuario):
            prestamo = utils.find_data_db(dni_usuario)
            print(prestamo)
        else:
            print("No se ha encontrado prestamos del usuario " + dni_usuario)
    
    def mostrar_prestamo(self):
        if not utils.get_data_db():
            print("No hay libros registrados")
        else:
            print(utils.get_data_db())
