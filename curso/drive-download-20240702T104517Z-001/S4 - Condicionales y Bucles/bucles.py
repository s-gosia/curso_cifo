# Bucle / Loop
# Def: Estructura de control que nos permite repertir cualquier tipo de intruccion/es
# PASOS CLAVE PARA EL CONTROL DE UN BUCLE
# 1- INICIALIZACION 
# 2- COMPARACION
# 3- ACTUALIZACION

# Bucle while 
# while comp: 
#     bloque de intrucciones SI SE CUMPLE
# while True:
#     print("Soy un bucle infinito")

# Ejemplo de imprimir los nums del 1al9
i = 1 # 1- INICIALIZACION 
while i < 10:  # 2- COMPARACION
    # i = i + 1  # 3- ACTUALIZACION
    print(i)
    i += 1 # lo mismo que i = i + 1

# Ejemplo de imprimir los nums del 1 a 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Ejemplo de imprimir los nums del 10 a 0
i = 10
while i >= 0:
    print(i)
    i -= 1

# bucle for
# Imprimir los numeros del 1 al 5
for i in range(1, 6):
    print(i)

# Bucle for con pasos
# Imprime los numeros pares del 2 al 10
# 2,4,6,8,10
for i in range(2, 11, 2):
    print(i)

# Imprimir los datos de una lista
frutas = ["manzana", "pera", "plátano"]
for fruta in frutas:
    print(fruta)

# Recorrer un diccionario
# Imprimir las claves y los valores
datos = {
    "Juan": 68,
    "Maria": 25,
    "Pedro": 41
}
# Accediendo individualmente a las edades mediante su clave
print(datos["Juan"]) #68
print(datos["Maria"]) #25
print(datos["Pedro"]) #41
# Imprimir las claves (keys)
print(datos.keys()) # ["Juan", "Maria", "Pedro"]

# Para recorrer la lista con un for, primero obtenemos una lista de claves mediante el metodo items()
print(datos.items()) # [("Juan",68), ("Maria",25), (Pedro,41)]

for nombre, edad in datos.items():
    print(nombre, edad)

# Sentencia BREAK y CONTINUE
# Ejemplo con break
# Imprimir los numeros del 1 al 10, y se acaba cuando llega si el numero es 5
for i in range(1, 11):
    if i == 5:
        break # detiene el for y pasa a la linea 76
    print(i)

# Ejemplo con continue
# Imprimir los numeros del 1 al 10, y omitir el num 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
   
# Buncle con ELSE, con un ejemplo que imprimir un mensaje que se completo sin interrupciones
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("Bucle completado sin interrupciones")

# Detectar que el email de un usuario este registrado en nuestra "DB"
emails_DB = ["a@a.com", "b@b.com", "c@c.com", "d@d.com"]
# Quiero conocer si el usuario con email "c@c.com" esta registrado en nuestra DB
email_buscar = "c@c.com"
for email in emails_DB:
    if email == email_buscar:
        print("El email " + email_buscar + " esta registrado")
        break
 









































