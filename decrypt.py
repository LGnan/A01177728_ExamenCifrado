from cryptography.fernet import Fernet
from PIL import Image
import io
import hashlib
import base64

# Solicitamos al usuario que ingrese la ruta donde guardar la imagen y el número
ruta_imagen = input("Por favor, ingresa la ruta donde guardar la imagen: ")
numero = input("Por favor, ingresa el número: ")

# Generamos la clave de encriptación a partir del número
clave = base64.urlsafe_b64encode(hashlib.sha256(numero.encode()).digest())
cifrado = Fernet(clave)

# Leemos la imagen encriptada
with open("imagen_encriptada", "rb") as f:
    imagen_encriptada = f.read()

# Desencriptamos la imagen
imagen_desencriptada = cifrado.decrypt(imagen_encriptada)

# Convertimos los bytes a imagen
imagen_final = Image.open(io.BytesIO(imagen_desencriptada))

# Guardamos la imagen en el formato JPEG
imagen_final.save(ruta_imagen, "JPEG")
