# Ejercicios:
 
# 1. Crea una clase llamada Persona que tendrá los siguientes atributos: nombre, edad y país de origen.
# La clase tendrá un método llamado mostrar_datos que mostrará los datos de la persona.
class Persona:
    # constructor
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def mostrar_datos(self):
        print(f"Te llamas {self.nombre}, tienes {self.edad} años y eres de {self.pais}")

persona1 = Persona("Pepe", 30, "España")
persona2 = Persona("María", 32, "Portugal")

persona1.mostrar_datos()
persona2.mostrar_datos()
 
# 2. Crea una clase llamada Rectangulo que tendrá los siguientes atributos: base y altura. La clase tendrá un método llamado calcular_area que mostrará el área del rectangulo
class Rectangulo:
    # constructor
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        print(f"Area: {self.base * self.altura}")

rectangulo1 = Rectangulo(10, 5)
rectangulo1.calcular_area()

# 3. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad.
# Un titular será obligatorio al crear una cuenta, la cantidad es opcional.
# La clase tendrá dos métodos:
# - ingresar: se ingresa una cantidad a la cuenta, si la cantidad es negativa, no se hará nada.
# - retirar: se retira una cantidad a la cuenta, si la cantidad es negativa, no se hará nada.
class Cuenta:
    # constructor
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad tiene que ser positiva")
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad tiene que ser positiva")

    # extra: Mostrar saldo
    def mostrar_saldo(self):
        print("Tu saldo es: " + str(self.cantidad))

cuenta1 = Cuenta("Pepe")
cuenta2 = Cuenta("Maria", 1000)

cuenta1.ingresar(500)
cuenta1.retirar(300)
cuenta1.mostrar_saldo()

# 4. Crea una clase llamada Libro que tendrá los siguientes atributos: título y autor.
# La clase tendrá un método llamado mostrar_datos que mostrará los datos del libro.
# Crea una clase llamada LibroTecnico que herede de la clase Libro y añade un atributo llamado tema.
# La clase LibroTecnico tendrá un método llamado mostrar_datos que mostrará los datos del libro.
# superclase
class Libro: 
    # constructor
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_datos(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}")

    def mostrar_autor(self):
        print(f"Autor: {self.autor}")

# subclase
class LibroTecnico(Libro):
    # constructor
    def __init__(self, titulo, autor, tema):
        super().__init__(titulo, autor)
        self.tema = tema

    def mostrar_datos(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Tema: {self.tema}")

libroPython = LibroTecnico("Introducción a Python", "Pepe", "Programación")
libroPython.mostrar_datos() # metodo de la subclase
libroPython.mostrar_autor() # metodo de la superclase (heredado)
 
# 5. Crea una clase llamada Electrodomestico que tendrá los siguientes atributos: precio, color, consumo_energetico y peso.
# Los atributos precio y peso deben tener valores por defecto de 100 y 5 respectivamente.
# La clase tendrá un método llamado precio_final que calculará el precio final del electrodoméstico.

class Electrodomestico:
    # constructor
    def __init__(self, color, consumo_energetico, peso=5, precio=100):
        self.precio = precio
        self.color = color
        self.consumo_energetico = consumo_energetico
        self.peso = peso

    def precio_final(self):
        # precio final sobre el consumo
        if self.consumo_energetico == "A":
            self.precio += 50
        elif self.consumo_energetico == "B":
            self.precio += 60
        elif self.consumo_energetico == "C":
            self.precio += 70
        # precio final sobre el peso
        if self.peso >= 5 and self.peso < 7:
            self.precio += 30
        elif self.peso >= 7 and self.peso < 10:
            self.precio += 40
        elif self.peso >= 10 and self.peso < 15:
            self.precio += 50

        return self.precio

electrodomestico1 = Electrodomestico("blanco", "A")
electrodomestico1.peso = 13
print(electrodomestico1.precio_final())





