# importar modulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime, date
# modulo database
from database import Database

class ApiRegistro(BaseHTTPRequestHandler):
    # metodo que gestiona las cabeceras
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
    def do_GET(self):
        db = Database() # instancia
        if self.path == "/registro_perros":
            resultado = db.query("select * from registro_perros")
            resultadoFormat = [
                {
                    "id": id,
                    "dni_usuario": dni_usuario,
                    "chip_perro": chip_perro,
                    "fecha_cita": fecha_cita.isoformat() if isinstance(fecha_cita, (datetime, date)) else fecha_cita
                }
                for id, dni_usuario, chip_perro, fecha_cita in resultado 
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultadoFormat).encode("utf-8"))
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/registro_perro":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            id = data.get("id")
            dni_usuario = data.get("dni_usuario")
            chip_perro = data.get("chip_perro")
            fecha_cita = data.get("fecha_cita") # la fecha de la cita concertada

            # Convertir fecha_cita a formato datetime si es necesario
            if isinstance(fecha_cita, str):
                fecha_cita = datetime.fromisoformat(fecha_cita)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("INSERT INTO registro_perros VALUES (%s, %s, %s, %s)", (id, dni_usuario, chip_perro, fecha_cita))
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
        if self.path == "/registro_perro":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            dni_usuario = data.get("dni_usuario")
            chip_perro = data.get("chip_perro")
            fecha_cita = data.get("fecha_cita")

            # Convertir fecha_cita a formato datetime si es necesario
            if isinstance(fecha_cita, str):
                fecha_cita = datetime.fromisoformat(fecha_cita)

            db = Database()  # instancia en DB
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("UPDATE registro_perros SET dni_usuario = %s, fecha_cita = %s WHERE chip_perro = %s", (dni_usuario, fecha_cita, chip_perro))
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
        if self.path == "/registro_perro":
            # recogemos los datos del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            chip_perro = json.loads(post_data)

            db = Database()  # Instancia a DB
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("DELETE FROM registro_perros WHERE chip_perro = %s", (chip_perro["chip_perro"],))
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


def run(server_class=HTTPServer, handle_class=ApiRegistro, port=3000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handle_class)
    print(f"ApiRegistro escuchando por el puerto {port}")
    httpd.serve_forever()

run()
