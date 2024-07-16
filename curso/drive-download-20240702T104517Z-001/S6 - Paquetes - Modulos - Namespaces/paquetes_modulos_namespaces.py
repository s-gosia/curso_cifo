# En Python, cada uno de nuestros archivos .py se denominan módulos. Estos modulos a la vez, pueden formar parte de paquetes. Un paquete es una carpeta que contiene modulos. Para que esa carpeta pueda ser considerada un paquete, debe contener un archivo de inicio llamado "__init__.py". Este archivo no tiene ninguna intrucción dentro (vacio)

# |___ paquete
#     |______ __init__.py
#     |______ modulo1.py
#     |______ modulo2.py 
#     |______ ......


# Los modulos, no necesariamente, deben pertenecer a un paquete

# |___ paquete
#     |______ __init__.py
#     |______ modulo1.py
#     |______ subpaquete
#            |______ __init__.py
#            |______ modulo1.py


# import modulo1
# import paquete.modulo1
# import paquete.subpaquete.modulo1

# namespace: Es el nombre que se indica detras de la palabra import. Es decir la "ruta" (namespace) del modulo

# Ejemplo
import paquete.modulo1 as m1

m1.funcion1() 
print(m1.diccionario)

# Importar modulo math
import math
print(math.sqrt(16))

# Importar modulo match con alias
import math as m
# redondea a la baja
print(m.floor(4.8)) # 4
print(m.cos(0)) # 1

# Importar una funcion de un modulo
from math import sqrt
print(sqrt(16))

# Importar todas las funciones del modulo
from math import *
print(sin(0))
print(tan(0))



































