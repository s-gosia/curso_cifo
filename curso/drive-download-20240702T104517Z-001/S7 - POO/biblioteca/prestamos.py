import utils

class Prestamo:
    def __init__(self, dni, isbn, fecha):
        self.dni = dni
        self.isbn = isbn
        self.fecha = fecha

class GestionPrestamos: 
    def __init__(self, gestionLibros, gestionUsuarios):
        self.prestamosDB = [] # database
        self.gestionLibros = gestionLibros
        self.gestionUsuarios = gestionUsuarios

    def menu_prestamos(self):
        while True:
            print("---Gestión de Préstamos---")
            print("1: Añadir un préstamo")
            print("2: Eliminar un préstamos (por dni ó isbn)")
            print("3: Buscar préstamos por usuario (dni)")
            print("4: Mostrar todos los préstamos")
            print("5: Volver al menú principal")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                dni = input("Introduce el dni del usuario: ").upper()
                isbn = input("Introduce el isbn del libro: ")
                fecha = input("Introduce la fecha del préstamo: ")
                self.anadir_prestamo(dni, isbn, fecha)

            if opcion == "2":
                busqueda = input("Introduce el DNI ó ISBN del préstamo que quieres eliminar: ")
                self.eliminar_prestamo(busqueda, busqueda)

            if opcion == "3":
                busqueda = input("Introduce el DNI ó ISBN del préstamo a buscar: ")
                resultados = self.buscar_prestamo(busqueda, busqueda)
                if resultados:
                    print("Resultados de la búsqueda: ")
                    for prestamo in resultados:
                        print(f"DNI: {prestamo.dni}, ISBN: {prestamo.isbn}, Fecha: {prestamo.fecha}")
                else:
                    print ("No se encontraron resultados")

            if opcion == "4":
                self.mostrar_prestamos()
            
            elif opcion == "5":
                break

    def anadir_prestamo(self, dni, isbn, fecha):

        # if not utils.validar_isbn_unique(dni, self.prestamosDB):
        #     print("DNI ya registrado")
        #     return

        # Validar si existe usuario mediante el metodo "buscar_usuario" de la clase GestionUsuarios
        resultados = self.gestionUsuarios.buscar_usuario(dni)
        if not resultados: 
            print("No se ha encontrado usuario con este dni " + dni)
            return
        
        # TODO: Lo mismo para validar el libro

        prestamo = Prestamo(dni, isbn, fecha)
        self.prestamosDB.append(prestamo)
        print(f"Préstamo añadido: {prestamo.__dict__}")

    def eliminar_prestamo(self, dni=None, isbn=None):
        for prestamo in self.prestamosDB:
            if prestamo.dni == dni or prestamo.isbn == isbn:
                self.prestamosDB.remove(prestamo)
                print(f"Préstamo borrado")
                return
        print("Préstamo no encontrado")

    def buscar_prestamo(self, dni=None, isbn=None): # Si no llega valor al param, toma el valor None
        resultados = []
        for prestamo in self.prestamosDB:
            if dni and dni.lower() == prestamo.dni.lower():
                resultados.append(prestamo)
            elif isbn and isbn.lower() == prestamo.isbn.lower():
                resultados.append(prestamo)
        return resultados

    def mostrar_prestamos(self):
        if self.prestamosDB:
            print("Préstamos registrados: ")
            for prestamo in self.prestamosDB:
                print(f"DNI: {prestamo.dni}, ISBN: {prestamo.isbn}, Fecha: {prestamo.fecha}")
        else:
            print("No hay prestamos registrados")