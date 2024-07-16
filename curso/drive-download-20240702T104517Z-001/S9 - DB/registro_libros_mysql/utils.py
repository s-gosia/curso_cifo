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
def set_data_db(libroOBJ):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Check if ISBN already exists
        cursor.execute("SELECT * FROM libros WHERE isbn = %s", (libroOBJ.isbn,))
        result = cursor.fetchone()
        
        if result:
            print("ISBN ya registrado")
            return
        
        # Insert new book
        cursor.execute(
            "INSERT INTO libros (titulo, autor, isbn, genero) VALUES (%s, %s, %s, %s)",
            (libroOBJ.titulo, libroOBJ.autor, libroOBJ.isbn, libroOBJ.genero)
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
        
        cursor.execute("SELECT * FROM libros")
        result = cursor.fetchall()
        
        return result
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def delete_data_db(isbn):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        cursor.execute("DELETE FROM libros WHERE isbn = %s", (isbn,))
        connection.commit()
        
        return cursor.rowcount > 0
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def find_data_db(isbn):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM libros WHERE isbn = %s", (isbn,))
        result = cursor.fetchone()
        
        return result if result else []
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

