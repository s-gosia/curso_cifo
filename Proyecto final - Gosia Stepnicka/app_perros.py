# importar modulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
# modulo database
from database import Database

class ApiPerros(BaseHTTPRequestHandler):
    # metodo que gestiona las cabeceras
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
    def do_GET(self):
        db = Database() # instancia
        if self.path == "/perros":
            resultado = db.query("select * from perros")
            resultadoFormat = [
                {
                    "chip": chip,
                    "nombre": nombre,
                    "raza": raza,
                    "genero": genero
                }
                for chip, nombre, raza, genero in resultado 
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultadoFormat).encode("utf-8"))
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/perro":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            chip = data.get("chip")
            nombre = data.get("nombre")
            raza = data.get("raza")
            genero = data.get("genero")

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("INSERT INTO perros VALUES (%s, %s, %s, %s)", (chip, nombre, raza, genero))
            db.close()
            self.set_headers(201) # envio un 201 (recurso creado) al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Datos almacenados en MySQL ok!"}).encode("utf-8")
            self.wfile.write(response)

        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))
    
    def do_PUT(self):
        if self.path == "/perro":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            nombre = data.get("nombre")
            raza = data.get("raza")
            chip = data.get("chip")

            db = Database()  # instancia en DB
            #llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("UPDATE perros SET nombre = %s, raza = %s WHERE chip = %s", (nombre, raza, chip))
            db.close()
            if rows > 0:
                self.set_headers(200)  # Mandamos 200 (OK) al metodo de cabeceras
                # Devolvemos mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Dato actualizado ok!"}).encode("utf-8")
                self.wfile.write(response)
            else:
                self.set_headers(404)  # 404 (Chip no encontrado)
                self.wfile.write(json.dumps({"error": "Perro no encontrado"}).encode("utf-8"))
        else:
            self.set_headers(404)  # 404 al metodo de cabeceras
            # Devolvemos mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    
    def do_DELETE(self):
        if self.path == "/perro":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            chip = json.loads(post_data)

            db = Database()  # Instancia a DB
            #llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("DELETE FROM perros WHERE chip = %s", (chip["chip"],))
            db.close()

            if rows > 0:
                self.set_headers(200)  # 200 (OK) al metodo de cabeceras 
                # Devolvemos mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Datos borrados ok!"}).encode("utf-8")
                self.wfile.write(response)
            else:
                self.set_headers(404)  # 404 (Chip No Encontrado)
                self.wfile.write(json.dumps({"error": "Datos no encontrados"}).encode("utf-8"))
        else:
            self.set_headers(404)  # 404 (No encontrado)
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))


def run(server_class=HTTPServer, handle_class=ApiPerros, port=3000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handle_class)
    print(f"ApiPerros escuchando por el puerto {port}")
    httpd.serve_forever()

run()




