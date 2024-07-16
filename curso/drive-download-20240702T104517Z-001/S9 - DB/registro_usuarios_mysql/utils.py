import mysql.connector
import re

# Database connection details
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'app'
}

# Validation Functions
def validar_dni(dni):
    return re.match(r'^\d{8}[A-HJ-NP-TV-Z]$', dni) is not None

def validar_nombre(nombre):
    return re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$', nombre) is not None

def validar_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def validar_password(password):
    return re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password) is not None

# Database operations
def set_data_db(usuarioOBJ):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Check if DNI or email already exists
        cursor.execute("SELECT * FROM usuarios WHERE dni = %s OR email = %s", (usuarioOBJ.dni, usuarioOBJ.email))
        result = cursor.fetchone()
        
        if result:
            print("DNI o Email ya registrado")
            return
        
        # Insert new user
        cursor.execute(
            "INSERT INTO usuarios (dni, nombre, email, password) VALUES (%s, %s, %s, %s)",
            (usuarioOBJ.dni, usuarioOBJ.nombre, usuarioOBJ.email, usuarioOBJ.password)
        )
        connection.commit()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def get_data_db():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM usuarios")
        result = cursor.fetchall()
        
        return result
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def delete_data_db(dni):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        cursor.execute("DELETE FROM usuarios WHERE dni = %s", (dni,))
        connection.commit()
        
        return cursor.rowcount > 0
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def find_data_db(dni):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM usuarios WHERE dni = %s", (dni,))
        result = cursor.fetchone()
        
        return result if result else []
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()


