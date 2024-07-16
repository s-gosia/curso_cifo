# Esto es un comentario
# Linea 1 comentario
# Linea 2 comentario

# Indentación
if 5 > 2: 
    print("Cinco es mayor que dos") # correcto
# print("Cinco es mayor que dos") incorrecto

# Python es un lenguaje dinámicamente tipado
# Esto significa que el tipo es una variable que se determina en tiempo de ejecución y no es necesario declarar explicitamente el tipo de variable al definirla

x = 5       # x es un entero
y = 3.14    # y es un flotante
z = "Hola"  # z es una cadena

print(x)
print(type(x))
print(type(y))
print(type(z))

# Comprobacion de tipos en tiempo de ejecucion
def sumar(a, b): # definicion
    return a+b  # retorno valor de la suma de los 2 params

print(sumar(2,2))  # llamada e impresion : 4

# Dinamicamente tipado:
# ventajas:
# - Mayor flexibilidad y rapidez en el desarrollo
# - Codigo mas conciso y facil de leer

# deventajas:
# - Mayor riesgo a errores
# - Mas dificil de mantener y depurar

# Estaticamente tipado:
# ventajas: - Robusted en el codigo. Mejor manejo de errores.
# deventajas: - Mayor desarrollo de codigo

# --------------------------------------------
# Def Variable: Un contenedor que tiene un nombre propio que nos permite almacenar diferentes tipos de datos. Podemos leer, escribir, borrar y actualizar esos datos
# Tipos de datos

# Numericos
entero = 10 # declaro la variable con nombre "entero" y la inicializo a un valor entero 10 
print(entero)
decimal = 10.143
print(decimal)

# Cadenas / String
saludo = "Hola Mundo!"
print(saludo)

# Booleanos
verdadero = True
falso = False
print(falso)

# Listas 
lista = [1, 2, 3, "cuatro", 5.0, True, [1,"hola"]]
print(lista)
# Acceso a un determinado dato por posición
# El primer valor de posicion es 0
print(lista[0])
# El ultimo valor de posicion es 5
print(lista[5])
print(lista[6][1])

# Tuplas
tupla = (1, 2, 3, "cuatro", 5.0, True)
# El mismo acceso para las Tuplas
print(tupla[3])
# Diferencia entre Lista y Tupla
# Lista: Es mutable, podemos modificar sus datos
# Ejemplo: 
lista[5] = False
print(lista)
# Tupla: Es inmutable, NO podemos modificar sus datos
# tupla[5] = False  # error

# Diccionarios (es mutable)
diccionario = {
    "clave1": "valor1", 
    "clave2": "valor2",
    "clave3": {
        "clave3-1": "valor3-1"
    }
}
# accedo a "valor1"
print(diccionario["clave1"])
print(diccionario["clave3"])
print(diccionario["clave3"]["clave3-1"])

alumnos = [
{
    "nombre":"Alumno1",
    "email": "email@gmail.com",
    "fecha_nac": "10/10/1990",
    "titulacion": True,
    "nota_curso": 8.4,
    "contenido": ["UF1-> Introd","UF2-> POO","UF3-> Proyecto"],
    "contenido_nota": {
        "UF1-> Introd": 7.45,
    }   
},{
    "nombre":"Alumno2",
    "email": "email@gmail.com",
    "fecha_nac": "10/10/1990",
    "titulacion": True,
    "nota_curso": 8.4,
    "contenido": ["UF1-> Introd","UF2-> POO","UF3-> Proyecto"],
    "contenido_nota": {
        "UF1-> Introd": 7.45,
    }   
},{
    "nombre":"Alumno2",
    "email": "email@gmail.com",
    "fecha_nac": "10/10/1990",
    "titulacion": True,
    "nota_curso": 8.4,
    "contenido": ["UF1-> Introd","UF2-> POO","UF3-> Proyecto"],
    "contenido_nota": {
        "UF1-> Introd": 7.45,
    }
}]

# Operadores y expresiones
# Aritmeticos
suma = 10 + 5
resta = 10 -5
mult = 10 * 5
div = 10 / 5
mod = 10 % 5
potencia = 10 ** 2

print(suma)
print(resta)
print(mult)
print(div)
print(mod)
print(potencia)

# De comparacion
igual = 10 == 5 
print(igual) # False

diferente = 10 != 5
print(diferente) # True

mayor = 10 > 5
print(igual) # True

menor = 10 < 5
print(igual) # False

mayor_igual = 10 >= 5
print(mayor_igual) # True

menor_igual = 10 <= 5
print(menor_igual) # False

# Logicos
# and: devuelve True si todos las comparaciones son True
# or: devuelve True si una de las comparaciones es True
# not: Invierte estado booleano True -> False 

and_operador = (10 > 5) and (10 < 5) # False
and_operador2 = (10 > 5) and (10 > 7) and (10 > 11) # False

or_operador = (10 > 5) or (10 < 5) # True
or_operador2 = (10 > 5) or (10 > 7) or (10 > 11) # True

not_operador = not(10 > 5) # False











































































