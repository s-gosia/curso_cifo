import mysql.connector

connex = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="prueba"
)

cursor = connex.cursor()

cursor.execute("truncate table mis_datos")

cursor.execute("insert into mis_datos values(null, 'Hola mundo')")
cursor.execute("insert into mis_datos values(null, 'Hello world')")

connex.commit()
cursor.close()

cursor2 = connex.cursor()
cursor2.execute("select * from mis_datos")
datos = cursor2.fetchall()
print(datos)
print(dict(datos))
