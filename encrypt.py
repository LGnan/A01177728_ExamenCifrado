# Importamos las bibliotecas necesarias
from cryptography.fernet import Fernet  # Biblioteca para cifrado simétrico
import base64  # Para codificación y decodificación en base64
from PIL import Image  # Biblioteca para manipulación de imágenes
import io  # Para trabajar con streams de bytes
import hashlib  # Para generar hash de la clave

# Solicitamos al usuario que ingrese la ruta de la imagen y el número
ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
numero = input("Por favor, ingresa un número: ")

# Generamos una clave de encriptación a partir del número
clave = base64.urlsafe_b64encode(hashlib.sha256(numero.encode()).digest())
cifrado = Fernet(clave)  # Creamos un objeto Fernet con la clave generada

# Abrimos la imagen y la convertimos a bytes
imagen = Image.open(ruta_imagen)
byte_arr = io.BytesIO()
imagen.save(byte_arr, format="JPEG")  # Guardamos la imagen en un stream de bytes en formato JPEG
imagen_en_bytes = byte_arr.getvalue()

# Encriptamos la imagen utilizando la clave generada
imagen_encriptada = cifrado.encrypt(imagen_en_bytes)

# Guardamos la imagen encriptada en un archivo llamado "imagen_encriptada"
with open("imagen_encriptada", "wb") as f:
    f.write(imagen_encriptada)
