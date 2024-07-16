import mysql.connector

# Database connection details
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'app'
}

# Validation methods

def validar_isbn_format(isbn):
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False

# Database operations
def set_data_db(prestamoOBJ):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Check if ISBN already exists
        cursor.execute("SELECT * FROM prestamos WHERE isbn_libro = %s", (prestamoOBJ.isbn_libro,))
        result = cursor.fetchone()
        
        if result:
            print("Libro ya prestado")
            return
        
        # Insert new book
        cursor.execute(
            "INSERT INTO prestamos (dni_usuario, isbn_libro, fecha_prestamo) VALUES (%s, %s, %s)",
            (prestamoOBJ.dni_usuario, prestamoOBJ.isbn_libro, prestamoOBJ.fecha_prestamo)
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
        
        cursor.execute("SELECT * FROM prestamos")
        result = cursor.fetchall()
        
        return result
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def delete_data_db(isbn_libro):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        cursor.execute("DELETE FROM prestamos WHERE isbn_libro = %s", (isbn_libro,))
        connection.commit()
        
        return cursor.rowcount > 0
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def find_data_db(isbn_libro):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM prestamos WHERE isbn_libro = %s", (isbn_libro,))
        result = cursor.fetchone()
        
        return result if result else []
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

