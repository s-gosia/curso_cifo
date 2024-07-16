# DEF: Podemos definir un Objeto en Programación, como un conjunto de propiedades ó atributos y métodos.
# A las props, también le podemos llamar DATOS
# A los métodos, FUNCIONES
string = "Hola Mundo" # longitud es 4 (prop)
string.replace("Mundo", "World") # accion

# TERMINOLOGIA OOP
# CLASE: Plantilla / "Fábrica" que define las caracteristicas de un objecto
# INSTANCIA: El proceso en el que se crea un objecto
# PROP o ATRIBUTOS: Caracteristicas de un objecto
# MÉTODOS: Capacidad o accion de un objeto
# CONSTRUCTOR: Método especial. Su funcion principal es incializar las prop de un objeto al instanciarse. Se ejecuta automáticamente en esa instancia. NO OBLIGATORIO
# HERENCIA: Una clase creada mediante herencia (subclase) y hereda todas las props y los metodos de la (superclase)
# ENCAPSULAMIENTO: La capacidad de ocultar props/metodos que se consideren o bien privados o innecesarios para la interaccion de el objeto desde el exterior 
# ABSTRACCION: Proceso de diseño de las clases que nos definen la cualidades del objeto
# POLIMORFISMO: La manera de que diferentes clases podrian definir la misma prop o metodo

# Ejemplo clase Usuario
class Usuario:
    # constructor
    # self: hace referencia a la instancia de la clase
    def __init__(self, nombreUsuario, email, password):
        # asigno a las prop de la clase, lo que llega de la instancia del objecto
        self.nombreUsuario = nombreUsuario
        self.email = email
        self.password = password
        self.emailConfirmado = False
        
    # NO DEFINIR CON MISMO NOMBRE LA PROP Y EL METODO
    # metodo que confirma el email
    def isEmailConfirmado(self):
        self.emailConfirmado = True
        
# instancia de un usuario
usuario1 = Usuario("armand", "armand@gmail.com", "1111")
usuario2 = Usuario("maria", "maria@gmail.com", "1234")
# Interaccion con los objetos
print(usuario1.email)
print(usuario2.email)

# Imprimir todas las props de un objeto (dict)
print(usuario1.__dict__)
# suponer que el usuario ha confirmado el email
usuario1.isEmailConfirmado()
print(usuario1.__dict__)

# Puedo crear una nueva prop desde aqui: SI
usuario1.ciudad = "Barcelona"
print(usuario1.__dict__)

# --------------------------------------------------
class Coche:
    # constructor
    def __init__(self, any, color, marca="Mercedes"):
        self.any = any
        self.color = color
        self.marca = marca
        self.ensamblado = False

    def get_antig_coche(self):
        from datetime import datetime
        # siempre que dentro hacemos referencia a una prop o metodo va precedido de "self"
        return datetime.now().year - self.any
    
    # metodo setter (si llamo a este metodo, setea la prop a True)
    def set_ensamblado(self):
        self.ensamblado = True

    # metodo getter 
    def get_ensamblado(self):
        return self.ensamblado

# Instancias
miCoche1 = Coche(2022, "Verde")
print(miCoche1.__dict__)
print("La antigüedad de miCoche1: " + str(miCoche1.get_antig_coche()) + " años")
print(f"La antigüedad de miCoche1: {miCoche1.get_antig_coche()} años")
# Desde fuera lo podemos cambiar (podemos gestionar este acceso con encapsulamiento)
# miCoche1.ensamblado = True
# print(miCoche1.__dict__)
# cambiamos el ensamblado
miCoche1.set_ensamblado() # ensamblado = True
print(miCoche1.get_ensamblado()) # ensamblado = True

# Ejemplo de un método estático. No es necesario llamar a estos metodos a traves de la instancia de su clase (creación del objeto)
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @staticmethod # define el metodo como estático
    def get_distancia(a, b):
        dx = a.x - b.x
        dy = a.y - b.y
        return (dx ** 2 + dy ** 2) ** 0.5


punto1 = Punto(5,5)
punto2 = Punto(10,10)
print(Punto.get_distancia(punto1, punto2))

# Herencia
# superclase
class Vehiculo:
    def __init__(self, color, marca, any):
        self.color = color
        self.marca = marca
        self.any = any

    def get_antiguedad_vehiculo(self):
        from datetime import datetime
        print(datetime.now().year - self.any)

# subclase Coche
class Coche(Vehiculo):
    # El constructor hereda de la superclase sus props y añadimos las exclusivas de esta propia clase (subclase)
    def __init__(self, color, marca, any, num_puertas):
        super().__init__(color, marca, any)
        self.num_puertas = num_puertas

    def abrir_maletero(self):
        print("Has abierto el maletero!")

# subclase Moto
class Moto(Vehiculo):
    # El constructor hereda de la superclase sus props y añadimos las exclusivas de esta propia clase (subclase)
    def __init__(self, color, marca, any):
        super().__init__(color, marca, any)

    def hacer_caballito(self):
        print("Has hecho caballito!")

# Encapsulamiento
class CocheEncapsulacion:
    # constructor
    def __init__(self, any, color, marca):
        self.any = any
        self.color = color
        self.marca = marca
        # prop privada: En python: Se precede de "__"
        self.__nivel_deposito = 0 

    # Si queremos interactuar con props privados utilizamos metodos "setters" y "getters"
    # SETTER
    def set_llenar_deposito(self, litros):
        total = self.__nivel_deposito + litros
        # suponemos que el deposito tiene capacidad max de 100 litros
        if total > 100:
            self.__nivel_deposito = 100
            print("Depósito lleno!")
        else: 
            self.__nivel_deposito = total
            print(f"El depósito tiene {total} litros")
        
    # GETTER
    def get_nivel_deposito(self):
        return self.__nivel_deposito
    
miCoche2 = CocheEncapsulacion(2020, "Rojo", "Fiat")
# comprobacion de prop privada
# print(miCoche2.__nivel_deposito)
# AttributeError: 'CocheEncapsulacion' object has no attribute '__nivel_deposito'
# utilizamos el metodo getter para leer la prop privada
print(miCoche2.get_nivel_deposito())
# respostamos
miCoche2.set_llenar_deposito(50)
print(miCoche2.get_nivel_deposito())
miCoche2.set_llenar_deposito(40)





















