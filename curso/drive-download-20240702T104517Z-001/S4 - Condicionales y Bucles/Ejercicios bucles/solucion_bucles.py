# Ejercicio 1 -> Escribe un programa que imprima los números del 1 al 10 utilizando un bucle while.
i = 0 # init
while i < 10: # comp
    print(i+1)
    i += 1 # act

# Ejercicio 2 -> Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.
for i in range(1, 11):
    print(i)

# Ejercicio 3 -> Escribe un programa que imprima los números pares del 2 al 10 utilizando un bucle for.
for i in range(2, 11, 2):
    print(i)

# Ejercicio 4 -> Escribe un programa que imprima los números impares del 1 al 9 utilizando un bucle for.
for i in range(1,11,2):
    print(i)

# Ejercicio 5 -> Escribe un programa que imprima los números del 10 al 1 utilizando un bucle while.
i = 10 # init
while i >= 1: # comp
    print(i)
    i -= 1 # act
# Ejercicio 6 -> Escribe un programa que imprima los números del 10 al 1 utilizando un bucle for.
for i in range(10, 0, -1):
    print(i)

# Ejercicio 7 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle for.
for i in range(1, 20):
    if i <= 10:
        print(i)
    elif i > 10:
        i = 20 - i
        print(i)
# output: 1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1

# Ejercicio 8 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle while.
i = 1
while i <= 20:
    if i <= 10:
        print(i)
        i += 1
    elif i > 10 and i < 20:
        x = 20 - i
        print(x)
        i += 1

# -----------------------------------
i = 1
while i <= 20:
    if i <= 10:
        print(i)
    else:
        print(20 -i)
    i += 1

# Ejercicio 9 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle for y un condicional.
for i in range(1, 20):
    if i <= 10:
        print(i)
    else:
        print(20 -i)

# Ejercicio 10 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle while y un condicional.
i = 1
while i <= 20:
    if i <= 10:
        print(i)
    else:
        print(20 -i)
    i += 1

# Numero primo
numero = 7
# opt while
i = 2
while i < numero:
    if numero % i == 0:
        print(f"{numero} no es primo")
        break
    i += 1
else:  # si no hay interrupciones, entra en el "else" y lo aprovechamos para sacar el msg de que es primo
    print(f"{numero} es primo")

# Ejercicios con listas
# Ejercicio 1 -> Escribe un programa que imprima los elementos de una lista utilizando un bucle for.
lista = [1,2,3,4,5]
for el in lista:
    print(el) 

# Ejercicio 2 -> Escribe un programa que imprima los elementos de una lista utilizando un bucle while.
lista = [1,2,3,4,5]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

# Ejercicio 3 -> Escribe un programa que imprima los elementos de una lista en orden inverso utilizando un bucle for. len() -> devuelve la longitud (cantidad de elementos) de una lista
lista = [1,2,3,4,5]
# opt 1: Imprimiendo la i (no lo pide asi el enun)
for i in range(len(lista), 0, -1):
    print(i)
# opt 2: ok
for i in range(len(lista)-1, -1, -1):
    print(lista[i])
# opt 3: ok
for i in range(len(lista)):
    print(lista[-(i+1)])
# opt 4: ok Imprimiendo la i (no lo pide asi el enun)
for i in lista[::-1]:
    print(i)
# opt 5: 
lista = ["uno", "dos", "tres"]
x = len(lista) - 1
for palabra in lista:
    print(lista[x-lista.index(palabra)])

# Ejercicio 4 -> Escribe un programa que imprima los elementos de una lista en orden inverso utilizando un bucle while.
lista = ["uno", "dos", "tres"]
i = 0
x = len(lista) - 1
while i < len(lista):
    print(lista[x-lista.index(lista[i])])
    i += 1

lista = ["uno", "dos", "tres"]
while lista:
    print(lista.pop(-1))

print(lista)
 
# Ejercicios con diccionarios
# Ejercicio 1 -> Escribe un programa que imprima las claves y valores de un diccionario utilizando un bucle for.
diccionario = {
    "Ana": 30,
    "Juan": 21,
    "Luisa": 33
}
# diccionario.items(): [("Ana",30),("Juan",21),("Luisa", 33)]
for nombre, edad in diccionario.items():
    print(f"Nombre: {nombre}, edad: {edad}")

# Ejercicio 2 -> Escribe un programa que imprima las claves y valores de un diccionario utilizando un bucle while.
diccionario = {
    "Ana": 30,
    "Juan": 21,
    "Luisa": 33
}
claves = list(diccionario.keys()) # lista con las claves
valores = list(diccionario.values()) # lista con los valores
i = 0
while i < len(diccionario): 
    print(claves[i], valores[i])
    i += 1

# Ejercicio 3 -> Escribe un programa que imprima las claves de un diccionario utilizando un bucle for.
diccionario = {
    "Ana": 30,
    "Juan": 21,
    "Luisa": 33
}
for nombre in diccionario:
    print(nombre)

# Ejercicio 4 -> Escribe un programa que imprima las claves de un diccionario utilizando un bucle while.
diccionario = {
    "Ana": 30,
    "Juan": 21,
    "Luisa": 33
}
claves = list(diccionario.keys())
i = 0
while i < len(claves):
    print(claves[i])
    i += 1

# Más complejos
# Ejercicio 1 -> Conteo de Palabras: Dado un texto, contar la frecuencia de cada palabra y almacenar los resultados en un diccionario (if in)
import string 
texto = "El rápido zorro marrón salta sobre el perro perezoso. El perro no estaba listo para eso."
# https://www.w3schools.com/python/ref_string_maketrans.asp
# elimina puntos
texto = texto.translate(str.maketrans('','', string.punctuation))
# acentos
texto = texto.translate(str.maketrans("áéíóú", "aeiou"))
# minusculas
texto = texto.lower()
print(texto)

palabras = texto.split()
print(palabras)


frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print(frecuencia_palabras)

# 2 manera
for palabra in palabras:
    frecuencia_palabras[palabra] = palabras.count(palabra)

# 3 manera
for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

# Ejercicio 2 -> Promedio de Calificaciones: Dada una lista de estudiantes con sus calificaciones, calcular el promedio de calificaciones por estudiante y almacenar los resultados en un diccionario.
estudiantes = {
   "Ana": [85, 92, 78],
   "Luis": [79, 95, 88],
   "Marta": [92, 88, 84],
   "Carlos": [70, 75, 80]
}

promedios = {}

for estudiante, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    promedios[estudiante] = promedio

# Ejercicio 3 -> Agrupación de Elementos: Dada una lista de números, agrupar los números en un diccionario según su paridad (pares e impares).
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_agrupados = {
    "pares": [],
    "impares": []
}

for numero in numeros:
    if numero % 2 == 0:
        numeros_agrupados["pares"].append(numero)
    else:
        numeros_agrupados["impares"].append(numero)

# Ejercicio 4 -> Conteo de Caracteres: Dada una lista de palabras, contar la frecuencia de cada carácter y almacenar los resultados en un diccionario.
palabras = ["hola", "mundo", "python", "programación"]

frecuencia_caracteres = {}

for palabra in palabras:
    for caracter in palabra:
        if caracter in frecuencia_caracteres:
            frecuencia_caracteres[caracter] += 1
        else:
            frecuencia_caracteres[caracter] = 1

print(frecuencia_caracteres)

# Ejercicio 5 -> Diccionario de Diccionarios: Dada una lista de estudiantes con sus calificaciones en varias asignaturas, crear un diccionario de diccionarios donde cada estudiante tiene un diccionario de asignaturas y sus calificaciones.  (if not in)
datos = [
   ("Ana", "Matemáticas", 85),
   ("Ana", "Ciencias", 92),
   ("Ana", "Historia", 78),
   ("Luis", "Matemáticas", 79),
   ("Luis", "Ciencias", 95),
   ("Luis", "Historia", 88),
   ("Marta", "Matemáticas", 92),
   ("Marta", "Ciencias", 88),
   ("Marta", "Historia", 84),
   ("Carlos", "Matemáticas", 70),
   ("Carlos", "Ciencias", 75),
   ("Carlos", "Historia", 80)
]

calificaciones = {}

for nombre, asignatura, nota in datos:
    if nombre not in calificaciones:
        calificaciones[nombre] = {}
    calificaciones[nombre][asignatura] = nota

print(calificaciones)
