# Funciones de validacion
#ISBN
def validar_isbn_format(isbn):
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False

def validar_isbn_unique(isbn, libros):
    for libro in libros:
        if libro.isbn == isbn:
            return False
    return True

def validar_dni_format(dni):
    digitosDNI = dni[:8]
    letraDNI = dni[-1] 
    if len(dni) != 9:
        return False
    elif not digitosDNI.isdigit() or not letraDNI.isalpha():
        return False
    else: 
        return True
        
def validar_dni_unique(dni, usuarios):
    for usuario in usuarios:
        if usuario.dni == dni:
            return False
    return True

def exportar_json(databaseLista, nombreFichero):
    import os
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # print(directorio_actual)
    # abspath: devuelve la ruta absoluta del fichero actual
    # dirname: devuelve la ruta del directorio padre/madre
    ruta_carpeta_json = os.path.join(directorio_actual, "json")
    # join: une la ruta absoluta con /json

    # si es la primera vez, creo la carpeta
    if not os.path.exists(ruta_carpeta_json):
        os.makedirs(ruta_carpeta_json)

    # escribir en el fichero json
    ruta_fichero = os.path.join(ruta_carpeta_json, nombreFichero)

    import json
    with open(ruta_fichero, "w") as file:
        json.dump([libro.__dict__ for libro in databaseLista], file, indent=4)


def cargar_json(nombreFichero):
    import os
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_fichero = os.path.join(directorio_actual, "json", nombreFichero)

    if not os.path.exists(ruta_fichero):
        return []
    
    import json
    with open(ruta_fichero, "r") as file:
        return json.load(file)



    

    



