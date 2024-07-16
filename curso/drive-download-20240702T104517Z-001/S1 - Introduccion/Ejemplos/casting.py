# Datos de entrada con el metodo input(), generalmente se reciben en formato str (String/ Cadena), pero a menudo es necesario convertirlos a otros tipos de datos (int) (float),....
# edad_por_consola_str = input("Dime tu edad: ") # str
# edad_conv_numero = int(edad_por_consola_str) # int
# edad_conv_numero_tipo = type(edad_conv_numero)
# print(edad_conv_numero_tipo)


# Comprobar si una persona es mayor de edad
edad = input("Dime tu edad: ")
edad_int = int(edad)

if edad_int >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
 
# Ejemplo que se convierte antes de operar
num1 = "10"
num2 = "5"
print("10" + "5") # el operador suma en Python concatenta si sumamos datos str
suma = int(num1) + int(num2)
print(suma)
print(int(num1) + int(num2)) # lo mismo sin crear variable suma

# CONCATENAR: Util cuando imprimo datos str y datos contenidos en variables. En Python el simbolo de concatenar es +
# ejemplo
miNombre = "Armand"
# output: "Mi nombre es Armand"
print("Mi nombre es " + miNombre)

# Ejemplo de cast str13
pi = 3.14159
print(type(pi))
print("El valor de pi es: " + str(pi))

# Convertir tupla en una lista
tupla = (1,2,3)
# tupla[0] = 1 error
lista = list(tupla)
lista[0] = 0








































































