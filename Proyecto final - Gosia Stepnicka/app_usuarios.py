# importar modulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt
from utils import validar_dni, validar_email, validar_nombre, validar_password

# modulo database
from database import Database

class ApiUsuarios(BaseHTTPRequestHandler):
    # metodo que gestiona las cabeceras
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
    def do_GET(self):
        db = Database() # instancia
        if self.path == "/usuarios":
            resultado = db.query("select * from usuarios")
            resultadoFormat = [
                {
                    "dni": dni,
                    "nombre": nombre,
                    "direccion": direccion,
                    "email": email,
                    "password": password
                }
                for dni, nombre, direccion, email, password in resultado 
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultadoFormat).encode("utf-8"))
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/usuario":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            dni = data.get("dni")
            nombre = data.get("nombre")
            direccion = data.get("direccion")
            email = data.get("email")
            password = data.get("password")

            # Validar los datos
            valid, error_message = self.validar_datos(dni, nombre, email, password)
            if not valid:
                self.set_headers(400)  # Enviar un 400 (Bad Request) al método de cabeceras
                # Devolver un mensaje de error en formato JSON al cliente
                response = json.dumps({"error": error_message}).encode("utf-8")
                self.wfile.write(response)
                return
            
            # Encryptar contrasena 
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s)", (dni, nombre, direccion, email, hashed_password))
            db.close()
            self.set_headers(201) # envio un 201 (recurso creado) al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Datos almacenados en MySQL ok!"}).encode("utf-8")
            self.wfile.write(response)

        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def validar_datos(self, dni, nombre, email, password):
        if not validar_dni(dni):
            return False, "DNI no válido"
        if not validar_nombre(nombre):
            return False, "Nombre no válido"
        if not validar_email(email):
            return False, "Email no válido"
        if not validar_password(password):
            return False, "Password no válido. Debe contener al menos 8 caracteres, incluyendo letras y números"
        return True, ""
    
    def do_PUT(self):
        if self.path == "/usuario":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            nombre = data.get("nombre")
            email = data.get("email")
            direccion = data.get("direccion")
            password = data.get("password")
            dni = data.get("dni")

            db = Database()  # instancia en DB
            #llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("UPDATE usuarios SET nombre = %s, email = %s, direccion = %s, password = %s WHERE dni = %s", (nombre, email, direccion, password, dni))
            db.close()
            if rows > 0:
                self.set_headers(200)  # Mandamos 200 (OK) al metodo de cabeceras
                # Devolvemos mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Dato actualizado ok!"}).encode("utf-8")
                self.wfile.write(response)
            else:
                self.set_headers(404)  # 404 (DNI no encontrado)
                self.wfile.write(json.dumps({"error": "Usuario no encontrado"}).encode("utf-8"))
        else:
            self.set_headers(404)  # 404 al metodo de cabeceras
            # Devolvemos mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    
    def do_DELETE(self):
        if self.path == "/usuario":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            dni = json.loads(post_data)

            db = Database()  # instancia en DB
            #llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("DELETE FROM usuarios WHERE dni = %s", (dni["dni"],))
            db.close()

            if rows > 0:
                self.set_headers(200)  # Mandamos 200 (OK) al metodo de cabeceras
                # Devolvemos mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Datos borrados ok!"}).encode("utf-8")
                self.wfile.write(response)
            else:
                self.set_headers(404)  # 404 al metodo de cabeceras
                self.wfile.write(json.dumps({"error": "Datos no encontrados"}).encode("utf-8"))
        else:
            self.set_headers(404)  # 404 al metodo de cabeceras
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))


def run(server_class=HTTPServer, handle_class=ApiUsuarios, port=3000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handle_class)
    print(f"ApiUsuarios escuchando por el puerto {port}")
    httpd.serve_forever()

run()




