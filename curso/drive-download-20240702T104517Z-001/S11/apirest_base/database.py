import mysql.connector
from mysql.connector import Error

class Database: 
    # constructor: cada vez que se realiza una instancia a esta clase, tenemos una conexion a MySQL en "self.connection"
    def __init__(self):
        #Gestionamos si hay error en la conexion MySQL mediante excepciones
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="apirest_base"
            )
        except Error as e:
            print("Error en MySQL: "+ str(e))

        self.cursor = self.connection.cursor()

    # Metodo consulta
    def query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    
    # Metodo ejecucion
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.rowcount
    
    # Metodo cerrar
    def close(self):
        self.cursor.close()
        self.connection.close()

