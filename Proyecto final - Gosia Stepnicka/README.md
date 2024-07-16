# API REST (Servidor Web) base para desarrollar el proyecto final de curso de Python - registro de los perros 

# Estructura Proyecto
/proyecto_final/
    |------- /sql               ->  Scripts SQL para la estructura de la DB
    |------- app.py  ->  Punto de entrada al programa
    |------- app_usuarios.py    ->  Punto de entrada de la apirest para gestion de usuarios
    |------- app_perros.py      ->  Punto de entrada de la apirest para gestion de perros
    |------- app_registro.py    ->  Punto de entrada de la apirest para gestion de registro
    |------- utils.py           ->  Archivo que contiene la logica de validaciones de datos de usuario



    |------- database.py        ->  Clase con lógica de interacción a MySQL
    |------- requirements.txt   ->  Archivo que contiene todos los módulos necesarios para la app

## requirements.txt: El comando que ejecutamos para que lea todos los módulos (dependencias) de este archivo y los instale en nuestro proyecto:
```
pip install -r requirements.txt
```

# Crear entorno virtual y activarlo
```
python -m venv venv
```
```
venv\Scripts\activate
```

# PASOS DESARROLLO
1- Crear el archivo "sql/database.sql" que contiene la estructura de la base de datos en MySQL (DB relacional). Esta base de datos contiene solamente tres tablas con las cuales interactuan los API REST. 

2- Desarrollar la Clase "Database" en "/database.py":
    - Constructor: Crea la conexion a MySQL
    - 3 métodos: Que realizan las acciones de "CONSULTA", "EJECUCIÓN" y "CERRAR CONEXIÓN"

3- Desarrollar la API REST en "/app_usuarios.py" 
    1- Añadir los imports que necesita este modulo
    2- Desarrollamos la Clase "ApiUsuarios"
        1- Método que gestiona las cabeceras (informacion que viaja junto al paquete (request, response))
        2- Método que gestiona la peticion GET
        3- Método que gestiona la peticion POST
        3- Método que gestiona la peticion DELETE

# Peticiones CRUD (create/read/update/delete)
# GET: http://localhost:3000/datos -> Devuelve todos los datos de las tablas "usuarios" (cRud)
    - body: None

# POST: http://localhost:3000/dato -> Crea/inserta un dato (str) en la tabla "usuarios" (Crud)
    - body (json): {
                    "dni": "str",
                    "nombre": "str", 
                    "email": "str", 
                    "password": "str"
                    }

# PUT: http://localhost:3000/dato -> Actualiza un dato (str) en la tabla "usuarios" (crUd)
    - body (json): {
                    "dni": "str",
                    "nombre": "str_actualizado", 
                    "email": "str_actualizado", 
                    "password": "str_actualizado"
                    }

# DELETE: http://localhost:3000/dato -> Borra un dato (str) en la tabla "usuarios" (crUd)
    - body (json): { "dni":"dni_usuario_a_borrar" } 

4- Desarrollar la API REST en "/app_perros.py" 
    1- Añadir los imports que necesita este modulo
    2- Desarrollamos la Clase "ApiPerros"
        1- Método que gestiona las cabeceras (informacion que viaja junto al paquete (request, response))
        2- Método que gestiona la peticion GET
        3- Método que gestiona la peticion POST
        3- Método que gestiona la peticion DELETE

# Peticiones CRUD (create/read/update/delete)
# GET: http://localhost:3000/datos -> Devuelve todos los datos de las tablas "perros" (cRud)
    - body: None

# POST: http://localhost:3000/dato -> Crea/inserta un dato (str) en la tabla "perros" (Crud)
    - body (json): {
                    "chip": "str",
                    "nombre": "str", 
                    "raza": "str", 
                    "genero": "str"
                    }

# PUT: http://localhost:3000/dato -> Actualiza un dato (str) en la tabla "perros" (crUd)
    - body (json): {
                    "chip": "str",
                    "nombre": "str_actualizado", 
                    "raza": "str_actualizado", 
                    }

# DELETE: http://localhost:3000/dato -> Borra un dato (str) en la tabla "perros" (crUd)
    - body (json): { "chip":"chip_perro_a_borrar" } 

4- Desarrollar la API REST en "/app_registro.py" 
    1- Añadir los imports que necesita este modulo
    2- Desarrollamos la Clase "ApiRegistro"
        1- Método que gestiona las cabeceras (informacion que viaja junto al paquete (request, response))
        2- Método que gestiona la peticion GET
        3- Método que gestiona la peticion POST
        3- Método que gestiona la peticion DELETE


# Peticiones CRUD (create/read/update/delete)
# GET: http://localhost:3000/datos -> Devuelve todos los datos de las tablas "registro_perros" (cRud)
    - body: None

# POST: http://localhost:3000/dato -> Crea/inserta un dato (str) en la tabla "registro_perros" (Crud)
    - body (json): {
                    "id": "default",
                    "dni_usuario": "str_usuario_existente", 
                    "chip_perro": "str_perro_existente", 
                    "fecha_registro": "0000-00-00"
                    }

# PUT: http://localhost:3000/dato -> Actualiza un dato (str) en la tabla "registro_perros" (crUd)
    - body (json): {
                    "dni_usuario": "str_usuario_existente_para_actualizar", 
                    "chip_perro": "str_perro_existente", 
                    "fecha_registro": "0000-00-00"
                    }


# DELETE: http://localhost:3000/dato -> Borra un dato (str) en la tabla "registro_perros" (crUd)
    - body (json): { "chip_perro":"str_chip_perro_a_borrar" } 