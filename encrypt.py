from cryptography.fernet import Fernet
import base64
from PIL import Image
import io
import hashlib

# Solicitamos al usuario que ingrese la ruta de la imagen y el número
ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
numero = input("Por favor, ingresa un número: ")

# Generamos una clave de encriptación a partir del número
clave = base64.urlsafe_b64encode(hashlib.md5(numero.encode()).digest())
cifrado = Fernet(clave)

# Abrimos la imagen y la convertimos a bytes
imagen = Image.open(ruta_imagen)
byte_arr = io.BytesIO()
imagen.save(byte_arr, format='JPEG')  # Cambiamos el formato a JPEG
imagen_en_bytes = byte_arr.getvalue()

# Encriptamos la imagen
imagen_encriptada = cifrado.encrypt(imagen_en_bytes)

# Guardamos la imagen encriptada
with open('imagen_encriptada', 'wb') as f:
    f.write(imagen_encriptada)
