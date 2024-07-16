# Definicion de funciones en Python:
# Bloque de código que se ejecuta cuando es llamado
# La función puede recibir parámetro y retornar un valor
# sintaxis
# def nombre_funcion (param1, param2, ...):
#     #Bloque ed codigo de la funcion
#     return datos
print("------suma_dos_numeros_1------")
# Ejemplo1: Suma dos numeros sin retorno de dato
def suma_dos_numeros_1(a, b):
    suma = a + b
    print(suma)

suma_dos_numeros_1(2, 2)
print("------suma_dos_numeros_2------")
# Ejemplo2: Suma dos numeros con retorno de dato
def suma_dos_numeros_2(a, b):
    suma = a + b
    return suma
# Si en una funcion, existe el return, tenemos que gestionar ese dato en la llamada
resultado = suma_dos_numeros_2(2,2)
print(resultado)
print("------suma_dos_numeros_2_1------")
# Ejemplo2_1: Suma dos numeros con retorno de dato (optimizando codigo)
def suma_dos_numeros_2_1(a, b):
    return a + b

print(suma_dos_numeros_2_1(2,2))
print("------es_positivo------")
# Ejemplo3: Crear una funcion que detecte si un numero es positivo o negativo
def es_positivo(numero):
    if numero >= 0:
        return True
    else:
        return False

print(f"Envia un numero y devuelvo True si es positivo o False si es negativo: {es_positivo(5)}")

print("------SCOPE------")
# SCOPE: El scope o alcance de una variable es el contexto en el que se puede acceder a ella
# Variables locales: Solo se puede acceder a ella dentro de la funcion en la que se declara
# Variables globales: Se puede acceder desde cualquier parte del programa
# A nivel de definición: Una variable local tiene prioridad a una global
# Ejemplos:
def funcion():
   variable_local = "Soy una variable local"
   print(variable_local) 
funcion()
# print(variable_local)
# -------------------------------
variable_global = "Soy una variable global"
def funcion():
    print(variable_global)
funcion()
# -------------------------------
variable_global = "Soy una variable global"
def funcion():
    variable_local = "Soy una variable local"
    print(variable_local)
    print(variable_global)
funcion()

# Para modificar una varible global dentro de una funcion, se debe utilizar la palabra clave "global"
x = 300
def myFunc():
    global x 
    x = 200    

myFunc()
print(x)

# Ejercicios: 
# Ejercicio de simulacion de Login que hicimos en condicionales. Transformarlo a funcion

# simulacion registro previo en DB
emailUserDB = "a@a.com" # global
passwordUserDB = "123456" # global

def userLogin(emailUserLogin, passwordUserLogin):
    if emailUserDB == emailUserLogin and passwordUserDB ==  passwordUserLogin:
        print("Login correcto")
    else: 
        print("Login incorrecto")

emailUserLogin = "a@a.com"
passwordUserLogin = "123456"

# Ejercicio de detectar si un numero es primo o no. Transformarlo a funcion
def esPrimo(n):
    i = 2
    while i < n:
        if n % i == 0:
            # print(n + " no es primo")
            return False
        i += 1
    else:
        # print(n + " es primo")
        return True

x = esPrimo(7)

# Ejercicio mediante funcion que escriba los numeros primos que hay en un rango de numeros
# 10 20: 11, 13, 17, 19
# Con todo el codigo
numeros_primos = []
def esPrimoRango(a,b):
    for i in range(a, b+1): # i: 10,11,12...,20
        if i < 2:
            continue
        j = 2
        while j < i:
            if i % j == 0:  
                break
            j += 1
        else:
            numeros_primos.append(i)

esPrimoRango(1,20)



