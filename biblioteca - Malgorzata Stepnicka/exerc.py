class Persona:
    def __init__(self, nombre, edad, pais_de_origen):
        self.nombre = nombre
        self.edad = edad
        self.pais_de_origen = pais_de_origen

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.pais_de_origen}"

persona1 = Persona("nombre", "edad", "pais de origen")
print(persona1)

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

Rectangulo1 = Rectangulo(10, 5)
print(Rectangulo1.calcular_area())

# 3. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad.
# Un titular será obligatorio al crear una cuenta, la cantidad es opcional.
# La clase tendrá dos métodos:
# - ingresar: se ingresa una cantidad a la cuenta, si la cantidad es negativa, no se hará nada.
# - retirar: se retira una cantidad a la cuenta, si la cantidad es negativa, no se hará nada.

class Cuenta:
    def __init__(self, titular, cantidad, retiro, ingreso):
        self.titular = titular
        self.cantidad = cantidad
        self.retiro = retiro
        self.ingreso = ingreso

    def ingresar(self):
        if self.ingreso > 0:
            self.cantidad += self.ingreso
            print(f"El total de la cuenta es {self.cantidad}")
        else:
            self.cantidad
    
    def retirar(self):
            if self.retiro > self.cantidad:
                return "No hay saldo suficiente"
            if self.retiro <= self.cantidad:
                return self.cantidad - self.retiro
            

cuenta1 = Cuenta("nombre", 6, 0, 4)
print(cuenta1.ingresar())

# 4. Crea una clase llamada Libro que tendrá los siguientes atributos: título y autor.
# La clase tendrá un método llamado mostrar_datos que mostrará los datos del libro.
# Crea una clase llamada LibroTecnico que herede de la clase Libro y añade un atributo llamado tema.
# La clase LibroTecnico tendrá un método llamado mostrar_datos que mostrará los datos del libro.

class libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_datos(self):
        return libro
    
    