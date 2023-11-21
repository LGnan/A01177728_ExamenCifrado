import os

# Solicitamos la ruta de la imagen y la clave al usuario
ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
extension = os.path.splitext(ruta_imagen)[1].upper()

# Validamos la extensión de la imagen
while extension not in [".JPEG", ".PNG", ".JPG"]:
    print("Por favor, ingresa una imagen con extensión .JPEG, .PNG o .JPG.")
    ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
    extension = os.path.splitext(ruta_imagen)[1].upper()

numero = int(input("Por favor, ingresa un número(clave): "))

# Leemos la imagen y la convertimos a bytes
with open(ruta_imagen, "rb") as file:
    image = bytearray(file.read())

# Encriptamos la imagen
for i, j in enumerate(image):
    image[i] = j ^ numero

# Guardamos la imagen encriptada
with open("imagen_encriptada.jpg", "wb") as file:
    file.write(image)
