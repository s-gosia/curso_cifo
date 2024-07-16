# Diccionarios: Son colecciones desordenados de pares "clave": "valor"

# Propiedades:
# Mutabilidad
# Desordenados: No mantienen un orden especifico
# Claves únicas: No podemos repetir en nombre de la claves

# Metodos
# get(): A traves del nombre de la clave, nos devuelve el valor
diccionario = {
    "nombre": "Pepe",
    "apellido": "López",
}
print(diccionario["nombre"]) # Pepe
print(diccionario.get("nombre")) # Pepe
# "clave": "valor"
# "key": "value"

# keys() devuelve en una lista las claves del diccionario
print(diccionario.keys()) # ["nombre", "apellido"]
x = diccionario.keys() 
# items(): devuelve una lista de tuplas, cada una con "clave":"valor"
print(diccionario.items()) # [("nombre","Pepe"), ("apellido","Lopez")]

# values(): Devuelve una lista de los valores
print(diccionario.values()) # ["Pepe", "Lopez"]

# pop(): Elimina un elemento con una clave determinada, devuelve el valor
diccionario2 = {
    "nombre": "Maria",
    "apellido": "Sanchez",
    "ciudad": "Barcelona",
    "dato": True
}

print(diccionario2)
dato_eliminado = diccionario2.pop("dato")
print(dato_eliminado)
# update(): Podemos añadir un nuevo par "clave": "valor"
diccionario2.update({"dato": dato_eliminado})
# update(): Podemos modificar una nueva par "clave": "valor" ya existente
diccionario2.update({"dato": False})







