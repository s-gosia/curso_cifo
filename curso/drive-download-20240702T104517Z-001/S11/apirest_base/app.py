# importar modulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt

# modulo database
from database import Database

class ApiRestBase(BaseHTTPRequestHandler):
    # metodo que gestiona las cabeceras
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
    def do_GET(self):
        db = Database() # instancia
        if self.path == "/datos":
            resultado = db.query("select * from datos")
            resultado_format = [
                {
                    "id": resultado[0],
                    "mensaje": resultado[1]
                }
                for mensaje in resultado
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultado_format).encode("utf-8"))
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = (json.dumps({"error": "Ruta no encontrada"})).encode("utf-8")
            self.wfile.write(response)


    def do_POST(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("insert into datos values (default, %s)", (mensaje["mensaje"],))
            db.close()
            self.set_headers(201) # envio un 201 (recurso creado) al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Dato almacenado en MySQL ok!"}).encode("utf-8")
            self.wfile.write(response)

        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = (json.dumps({"error": "Ruta no encontrada"})).encode("utf-8")
            self.wfile.write(response)


def run(server_class=HTTPServer, handle_class=ApiRestBase, port=3000):
    server_address = ("localhost", port)
    httpd = server_class(server_address, handle_class)
    print(f"ApiRest escuchando por el puerto {port}")
    httpd.serve_forever()

run()
