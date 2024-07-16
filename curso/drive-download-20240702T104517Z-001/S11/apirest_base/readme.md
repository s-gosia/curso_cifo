# API REST base que nos sirve para desarollar el proyecto final de curso de Python. 

# Estructura de proyecto 
/apirest_base/
    |------- /sql                -> Scripts AQL para la estructura de la DB
    |------- app.py              -> Punto de entrada de la apirest (logica del servidor web)
    |------- database.py         ->  Clase con logica de interaccion a MySQL
    |------- requirements.txt    -> Archivo que contiene todos los modulos necesarios para la app

## requirements.txt: El comando que ejecutamos para que lea todos los modulos (dependencias) de este archivo y los instale en nuestro proyecto 
```
pip install -r requirements.txt
```

# Crear entorno virtual
```
python -m venv venv
```
```
venv\Scripts\activate
```

# Pasos desarollo 
1- Crear el archivo "database.sql" que contine la estructura de la base de datos en MySQL (DB relacional). Esta base de datos contiene una table con un cambo "dato" en el interactura la apirest. 
2- Desarollar la Clase "Database" en "/database.py";
    - Constructor: Crear la conexion a MySQL
    - 3 metodos que realizan las acciones de "consulta", "ejecucion" y "cerrar conexion"
3- Desarrollar la API REST en "/app.py"
    1- Anadir los imports que necesita este modulo
    2- Desarrollamos la clase "ApiRestBase"

# Peticiones CRUD
# GET: http://localhost:3000/datos -> Devuelve todos los datos de la tabla "datos" (Read)
    - body: None
# POST: http://localhost:3000/dato -> Crea/inserta un dato (str) en la tabla "datos" (Create)
    - body (json): {"mensaje": "dato_tipo_texto"}
# PUT: http://localhost:3000/dato -> Actualiza un dato (str) en la tabla "datos" (Update)
    - body (json): {id: "id_del_dato_a_act", "mensaje": "dato_tipo_texto_act"}
# DELETE: http://localhost:3000/dato -> Borra un dato (str) de la tabla "datos" (Delete)
    - body (json): {id: "id_del_dato_a_borrar}


