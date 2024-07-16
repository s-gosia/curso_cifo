# Ejercicio 1 -> Escribe un programa que pida al usuario un número entero e imprima si es positivo, negativo o cero.
numero = 10
if numero > 0:
    # print(numero + " es positivo")
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es 0")

# Ejercicio 2 -> Introducir el color del semáforo y mostrar si puede pasar, extremar la precaución o no pasar.
color = "rojo" 
color = color.lower()
if color == "rojo":
    print("No puedes pasar!")
elif color == "ambar":
    print("Precaución!")
elif color == "verde":
    print("Puedes pasar!")
else:
    print("Color erróneo!")

# Ejercicio 3 -> Mostrar si un número es par o impar
numero = 4
tipo_dato = type(numero)
if tipo_dato != int:
    print("Dato no numérico")
else:   
    if numero % 2 == 0:
        print(numero + " es par")  
    else:
        print(numero + " es impar")  

# Ejercicio 4 -> Introducir 3 números. Indicar si el tercero es la suma de los dos primeros o no.
num1 = 3
num2 = 1
num3 = 4
 
if num3 == num1 + num2:
    print("num3 es igual a num1 + num2")
else:
    print("num3 NO es igual a num1 + num2")

# Ejercicio 5 -> Introducir un precio a pagar y el dinero disponible y mostrar si le falta dinero, indicarle cuanto, si le sobra indicar cuánto y si esta justo mostrar gracias por la compra
precioPagar = 100
dineroDisponible = 150
if precioPagar > dineroDisponible:
    print(f"Te falta {precioPagar - dineroDisponible}")
elif precioPagar < dineroDisponible:
    print(f"Te sobre {dineroDisponible - precioPagar}")
else:
    print("Tienes el dinero justo!")

# Ejercicio 6 -> Introducir 3 números. Ordenar descendentemente.
num1 = 5
num2 = 6
num3 = 9
lista = [num1, num2, num3]
lista_ord = lista.sort(reverse=True) 

# Ejercicio 7 -> Comprobar la letra del DNI:
# letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
# Para la calcular la letra divide tu número de dni entre 23 y el resto es la posicion de la lista anterior: Ejemplo: 11223344 % 23 = 8 -> letra P
letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

DNI_completo = "11223344A"
print(DNI_completo[:8]) # devuelve los 8 primeros caracteres
print(DNI_completo[8]) # A
print(DNI_completo[-1]) # A

# len() -> devuelve la longitud (cant caracteres) de un str
if len(DNI_completo) != 9:
    print("DNI incorrecto")  
else: 
    digitos = int(DNI_completo[:8])
    letra = DNI_completo[-1]
    letraDNI_Calculo = letras[digitos % 23] 
    if letra == letraDNI_Calculo:
        print("Letra correcta")
    else:
        print("letra incorrecta")
