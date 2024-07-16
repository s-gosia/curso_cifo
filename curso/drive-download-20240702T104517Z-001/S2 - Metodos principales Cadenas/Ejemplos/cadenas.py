# Metodos principales de cadenas
# upper(): retorna la cadena en mayusculas
cadena = "hola"
print(cadena.upper())

# lower(): retorna la cadena en minusculas
cadena = "HOLA"
print(cadena.lower())

# capitalize(): Convierte el mayuscula la primera letra del str
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

# title(): retorna una cadena con la primera letra de cada palabra en mayusculas
txt = "hello, and welcome to my world."
x = txt.title()
print(x)

# replace(): retorna la cadena que reemplazada por otra subcadena
cadena = "Hola que tal"
str_replace = cadena.replace("que tal", "cómo estás")
print(str_replace)

# split() Retorna una lista de palabras de palabras a partir de una cadena
cadena = "Hola que tal"
txt = "hello, my name is Peter, I am 26 years old"

print(cadena.split())
print(txt.split(", ", 1))

# join(): Retorna una cadena a partir de una lista
cadena = ["Hola", "que", "tal"]
print(" ".join(cadena)) # "Hola que tal"

# strip(): Retorna la cadena eliminando los espacios por el principio y final
cadena = "     Hola que tal          "
print(cadena.strip())

# lstrip(): Retorna la cadena eliminando los espacios por el principio
cadena = "     Hola que tal          "
print(cadena.lstrip())

# rstrip(): Retorna la cadena eliminando los espacios por el final
cadena = "     Hola que tal          "
print(cadena.rstrip())

# startswith(): Retorna un True si la cadena comienza por una subcadena
cadena = "Hola que tal"
print(cadena.startswith("hola")) #False
print(cadena.startswith("Hola")) #True
print(cadena.startswith("H")) #True

# ejemplo validar telefono (comience por 6/7/9)  
telefono_validar = "654987321"
datos_alumnos = {}
if telefono_validar.startswith("6") or telefono_validar.startswith("7") or telefono_validar.startswith("9") :
    print("Telefono OK")
    datos_alumnos["telefono"] = telefono_validar
else: 
    print("Telefono KO")

print(datos_alumnos)

# endswith(): Retorna un True si la cadena acaba por una subcadena
cadena = "Hola que tal"
print(cadena.endswith("tal")) #True

# find(): Retorna la posicion de una subcadena en una cadena
cadena = "Hola que tal"
print(cadena.find("que"))

# count(): retorna el numero de veces que una subcadena aparece en una cadena
cadena = "Hola que tal que tal"
print(cadena.count("que"))









































