# Condicionales
# Def: Estructrura de control que permite tomar decisiones basadas en el valor de una expresion. 
# En Python, se definen mediante la palabra clave if, se seguida de una expresion booleana y dos puntos :
# Si la expresion boolena es verdadera, se ejecuta el bloque de codigo  que sigue al condicional, sino se ejecuta el siguiente condicional o bloque de codigo

# Ejemplo1
# Condicional simple 
x = 10
if x > 5: 
    print("x es mayor que 5") # comparativa devuelve True 

# Ejemplo 2
# Condicional compuesto. Gestiona la comparacion contraria (no se cumple)
x = 3
if x > 5: 
    print("x es mayor que 5") # comparativa devuelve True 
else:
    print("x es menor o igual que 5") # comparativa devuelve False 

# Ejemplo 3
# Condicional anidado: Vemos el ejemplo anterior gestionando la salida si el valor e igual a 5
x = 3
if x > 5:
    print("x es mayor que 5") # comparativa devuelve True 
else:
    if x==5:
        print("x es igual que 5")
    else:
        print("x es menor que 5")     

# Ejemplo 4
# Condiciona elif
x = 3
if x > 5:
    print("x es mayor que 5") # comparativa devuelve True 
elif x==5:
    print("x es igual que 5")
else:
    print("x es menor que 5")   

# Condicional solo con if y con else
x = 5
if x >= 0:
    print("x es positivo")
if x < 0:
    print("x es negativo")
# ------------------------------
if x >= 0:
    print("x es positivo")
else:
    print("x es negativo")

# Ejemplo5: Detecta si estoy saludando con la palabra hola
# Aceptamos "Hola" "HOLA" "hola"
cadena = "ssss" 
if cadena == "Hola":
    print(cadena + " que tal") # Hola que tal
elif cadena == "HOLA":
    print(cadena + " que tal") # HOLA que tal
elif cadena == "hola":
    print(cadena + " que tal") # hola que tal
else:
    print("No has saludado!")

# Ejemplo5.1: Podemos usar metodos de cadenas para optimizar y validar codigo
# Aceptamos "Hola" "HOLA" "hola"
cadena = input("Introduce el saludo 'Hola'")
cadena = cadena.lower().strip()
if cadena == "hola":
    print(cadena + " que tal")   
else:
    print("No has saludado!")   

#Ejemplo6: Comparadores logicos
# Login
emailDB = "armand@gmail.com" # REGEXP
passwordDB = "1234"
emailUSER = "armand@gmail.com"
passwordUSER = "1234"

if emailDB == emailUSER and passwordDB == passwordUSER:
    print("Login correcto!")
else:
    print("Datos erróneos!")

# Ejemplo7: Detectar si un numero es positivo o negativo
num = 10
if num >= 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

# version2 : Quiero detectar el valor cero
if num > 0:
    print("El numero es positivo")
elif num < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")

# Ejemplo8: Detectar si un numero es par o impar
x = 4
x = "hola" # validar que el dato de variable no es numerica
# int, float, str, bool, list, tuple, dict
xType = type(x)
if xType != int:
    print(x + " no es un numero entero")
else:
    if x%2 == 0:
        print(str(x) + " es par")
    else: 
        print(str(x) + " es impar")
# Ejemplo9: Ordenar 3 numeros de mayor a menor
# forma rapida
numeros = [4,1,8] 
numeros.sort(reverse=True) # [8,4,1]
print(numeros)
# forma condicional
num1 = 4
num2 = 1
num3 = 8
# resultado ok -> num3 > num1 > num2

# num1 es el mayor
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print("num1 > num2 > num3")
    else:
        print("num1 > num3 > num2")
# num2 es el mayor
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print("num2 > num1 > num3")
    else:
        print("num2 > num3 > num1")
# num3 es el mayor
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print("num3 > num1 > num2")
    else:
        print("num3 > num2 > num1")


if num1 > num2 > num3:
    print("num1 > num2 > num3")
elif num1 > num3 > num2:
    print("num1 > num3 > num2")
elif num2 > num3 > num1:
    print("num2 > num3 > num1")
elif num2 > num1 > num3:
    print("num2 > num1 > num3")
elif num3 > num1 > num2:
    print("num3 > num1 > num2")
else:
    print("num3 > num2 > num1")


























