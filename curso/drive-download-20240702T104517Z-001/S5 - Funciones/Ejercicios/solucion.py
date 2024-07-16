# Ejercicio 1 -> Escribe una función que reciba dos números y devuelva el mayor de los dos.
def mayor(a,b):
    if a > b:
        return a
    else:
        return b
mayor(2,3)    

# Ejercicio 2 -> Escribe una función que reciba dos números y devuelva el menor de los dos.
# Ejercicio 3 -> Escribe una función que reciba un número y devuelva True si es par y False si es impar.
# Ejercicio 4 -> Escribe una función que reciba un número y devuelva True si es impar y False si es par.
# Ejercicio 5 -> Escribe una función que reciba un número y devuelva True si es positivo y False si es negativo.
# Ejercicio 6 -> Escribe una función que reciba un número y devuelva True si es negativo y False si es positivo.
# Ejercicio 7 -> Escribe una función que reciba un número y devuelva True si es cero y False si no lo es.
# Ejercicio 8 -> Escribe una función que reciba un número y devuelva True si es un número entero y False si no lo es.
# Ejercicio 9 -> Escribe una función que reciba un número y devuelva True si es un número decimal y False si no lo es.
# Ejercicio 10 -> Escribe una función que reciba un número y devuelva True si es un número positivo y decimal y False si no lo es. 
# Ejercicio 11 -> Escribe una función que reciba un número y devuelva True si es un número negativo y decimal y False si no lo es. 
# Ejercicio 12 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero y False si no lo es.
# Ejercicio 13 -> Escribe una función que reciba un número y devuelva True si es un número negativo y entero y False si no lo es.
 # Ejercicio 14 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero o decimal y False si no lo es. 
# Ejercicio 15 -> Escribe una función que reciba un número y devuelva True si es un número negativo y entero o decimal y False si no lo es.
# Ejercicio 16 -> Escribe una función que reciba un número y devuelva True si es un número entero o decimal y False si no lo es.


# Más complejos:

# Creamos funcion de filtro de texto (puntuacion y acentos) ya que se repite en varias funciones
def textFilter(text):
    import string
    text = text.translate(str.maketrans('','', string.punctuation))
    text = text.translate(str.maketrans("áéíóú", "aeiou"))
    text = text.lower()
    palabras = text.split()
    return palabras

# Escribe una función contar_palabras que reciba una cadena de texto y devuelva un diccionario con el conteo de cada palabra en el texto.
def contar_palabras(texto):
    palabras = textFilter(texto) # llamada a funcion de filtro de texto
    contar_palabras = {}
    for palabra in palabras:
        if palabra in contar_palabras:
            contar_palabras[palabra] += 1
        else:
            contar_palabras[palabra] = 1

    return contar_palabras

print(contar_palabras("El rápido zorro marrón salta sobre el perro perezoso. El perro no estaba listo para eso."))

# Escribe una función frecuencia_caracteres que reciba una cadena de texto y devuelva un diccionario con el conteo de cada carácter en el texto
def contar_caracteres(texto):
    palabras = textFilter(texto) # llamada a funcion de filtro de texto
    contar_caracteres = {}
    for palabra in palabras:
        for caracter in palabra:
            if caracter in contar_caracteres:
                contar_caracteres[caracter] += 1
            else:
                contar_caracteres[caracter] = 1

    return contar_caracteres

print(contar_caracteres("El rápido zorro marrón salta sobre el perro perezoso. El perro no estaba listo para eso."))

# Escribe una función analizar_palabras que reciba una cadena de texto y devuelva un diccionario con la longitud de cada palabra como clave y la lista de palabras de esa longitud como valor.

def analizar_palabras(texto):
    palabras = textFilter(texto) # llamada a funcion de filtro de texto
    
    resultado = {}

    for palabra in palabras:
        longitud = len(palabra)
        if longitud in resultado:
            resultado[longitud].append(palabra)
        else:
            resultado[longitud] = [palabra]


print(analizar_palabras("El rápido zorro marrón salta sobre el perro perezoso. El perro no estaba listo para eso."))

# Escribe una función contar_vocales_consonantes que reciba una cadena de texto y devuelva un diccionario con el conteo de vocales y consonantes en el texto.

def contar_vocales_consonantes(texto):
    texto = texto.lower()  
    vocales = "aeiouáéíóú"
    consonantes = "bcdfghjklmnpqrstvwxyz"

    contador = {
        "vocales": 0,
        "consonantes": 0
    }

    for caracter in texto:
        if caracter in vocales:
            contador["vocales"] += 1
        elif caracter in consonantes:
            contador["consonantes"] += 1

print(contar_vocales_consonantes("El rápido zorro marrón salta sobre el perro perezoso. El perro no estaba listo para eso."))

