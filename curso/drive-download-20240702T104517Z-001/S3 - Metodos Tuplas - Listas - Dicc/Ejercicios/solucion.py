# Ejercicio con Tuplas:
# Crea una tupla con los números del 1 al 5.
tupla = (1,2,3,4,5)

# Accede al tercer elemento de la tupla.
tercer_elem = tupla[2] # 3

# Cuenta cuántas veces aparece el número 2 en la tupla.
print(tupla.count(2))
conteoNumDos = tupla.count(2)

# Encuentra el índice del número 4 en la tupla.
indice_num_4 = tupla.index(4)

# Ejercicio con Listas:
# Crea una lista con los números del 1 al 5.
lista = [1,2,3,4,5]
# Añade el número 6 al final de la lista.
lista.append(6)
print(lista)
# Inserta el número 0 al inicio de la lista.
lista.insert(0, 0)
print(lista)

# Ordena la lista en orden descendente.
lista.sort(reverse=True)
print(list)

# Elimina el tercer elemento de la lista.
lista.pop(2) # pop() elimina elemento por posicion
print(lista) 

# Ejercicio con Diccionarios:
# Crea un diccionario con las claves "nombre" y "edad", y los valores "Ana" y 25, respectivamente.
diccionario = {
    "nombre": "Ana",
    "edad": 25
}

# Añade una nueva clave "ciudad" con el valor "Barcelona".
diccionario["ciudad"] = "Barcelona" # si la clave "ciudad" ya existe, actualiza el valor, y sino, la crea 
print(diccionario)

# Actualiza el valor de la clave "edad" a 26.
diccionario["edad"] = 26
diccionario.update({"edad": 26})

# Elimina la clave "ciudad" y muestra su valor.
print(diccionario.pop("ciudad"))

# metodos de conversion: tuple, list, dict

# Ejercicio de Conversión de Tipos:
# Convierte una lista 1, 2, 3 en una tupla.
lista = [1,2,3]
lista_conv_tupla = tuple(lista)
print(lista_conv_tupla)

# Convierte una tupla (("clave1", "valor1"), ("clave2", "valor2")) en un diccionario.
tupla = (("clave1", "valor1"), ("clave2", "valor2"))
tupla_conv_dict = dict(tupla)
print(tupla_conv_dict)

lista = [1,2,3]
lista_conv_dict = dict(lista) # error de formato 

lista = [["clave1", "valor1"], ["clave2", "valor2"]]
lista_conv_dict = dict(lista) # ok

# Convierte un diccionario {"a": 1, "b": 2} en una lista de sus claves. result -> ["a", "b"]
dict = {"a": 1, "b": 2}
list_claves = list(dict.keys())
print(list_claves)