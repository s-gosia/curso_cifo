# Tuplas: Son colecciones de datos ordenados y mutables

# Mutabilidad: Una vez creada podemos modificar sus datos
# Indexacion: Se puede acceder a los datos mediante indices (valor numerico)
# Ordenadas: Mantienen el orden en el que se insertan los elementos

lista = [1,2,3,4,5,2,2]
# acceso o lectura, y modif
print(lista[4]) #5
lista[3] = 1

# Metodos 
print(lista) # [1,2,3,1,5,2,2]
# append: Inserta un valor en la ultima posicion
lista.append(8) # [1,2,3,1,5,2,2,8]
# insert: Inserta un valor en una determinada posicion
lista.insert(0,8) # [8,1,2,3,1,5,2,2,8]
lista.insert(2,8) # [8,1,8,2,3,1,5,2,2,8]
# remove: Elimina el primer valor que hay en la lista 
lista.remove(2) # [8,1,8,3,1,5,2,2,8]
# pop:  Elimina valor en una determinada posicion
lista.pop(2) # [8,1,3,1,5,2,2,8]
# reverse: Invierte los valores 
lista.reverse() # [8,2,5,1,8,1,8]
# sort: Ordena los valores de menor a mayor
lista.sort()
print(lista)
lista.sort(reverse=True) # Invierte de mayor a menor
# Lista con cadenas
lista_cadena = ["hola","%", "que", "#","tal", "estas", "Estas", ]
lista_cadena.sort()
print(lista_cadena)
