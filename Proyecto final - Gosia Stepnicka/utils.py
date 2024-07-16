import re
import bcrypt

# Funciones de validacion
def validar_dni(dni):
    return re.match(r'^\d{8}[A-HJ-NP-TV-Z]$', dni) is not None

def validar_nombre(nombre):
    return re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$', nombre) is not None

def validar_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

def validar_password(password):
    return re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password) is not None

# Encryptacion de contraseña
def hash_password(password):
    # Generar salt
    salt = bcrypt.gensalt()
    # Hash la contraseña
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed