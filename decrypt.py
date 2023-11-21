from cryptography.fernet import Fernet
from PIL import Image
import io

# Solicitamos al usuario que ingrese la ruta donde guardar la imagen
ruta_imagen = input("Por favor, ingresa la ruta donde guardar la imagen: ")

# Leemos la imagen encriptada y la clave
with open('imagen_encriptada', 'rb') as f:
    imagen_encriptada = f.read()
with open('clave', 'rb') as f:
    clave = f.read()

# Creamos el objeto de cifrado
cifrado = Fernet(clave)

# Desencriptamos la imagen
imagen_desencriptada = cifrado.decrypt(imagen_encriptada)

# Convertimos los bytes a imagen
imagen_final = Image.open(io.BytesIO(imagen_desencriptada))
imagen_final.save(ruta_imagen, 'JPEG')  # Guardamos la imagen en formato JPEG

#pip3 install cryptography
#pip3 install Pillow
