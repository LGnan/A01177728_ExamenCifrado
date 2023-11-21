# Importamos las bibliotecas necesarias
import os  # Para obtener la extensión de la imagen

# Solicitamos al usuario que ingrese la ruta de la imagen y el número
ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")

# Obtenemos la extensión de la imagen
extension = os.path.splitext(ruta_imagen)[1].upper()

# Verificamos si la extensión es válida
while extension not in [".JPEG", ".PNG", ".JPG"]:
    print("Por favor, ingresa una imagen con extensión .JPEG, .PNG o .JPG.")
    ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
    extension = os.path.splitext(ruta_imagen)[1].upper()

numero = int(input("Por favor, ingresa un número: "))

# Abrimos la imagen y la convertimos a bytes
with open(ruta_imagen, 'rb') as file:
    image = bytearray(file.read())

# Aplicamos la operación XOR a cada byte de la imagen
for i, j in enumerate(image):
    image[i] = j ^ numero

# Guardamos la imagen encriptada en un archivo llamado "imagen_encriptada.jpg"
with open("imagen_encriptada.jpg", 'wb') as file:
    file.write(image)