import os

ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
extension = os.path.splitext(ruta_imagen)[1].upper()

while extension not in [".JPEG", ".PNG", ".JPG"]:
    print("Por favor, ingresa una imagen con extensión .JPEG, .PNG o .JPG.")
    ruta_imagen = input("Por favor, ingresa la ruta de la imagen: ")
    extension = os.path.splitext(ruta_imagen)[1].upper()

# Validamos que el número ingresado sea un entero
while True:
    try:
        numero = int(input("Por favor, ingresa un número(clave): "))
        break
    except ValueError:
        print("Por favor, ingresa un número entero.")

with open(ruta_imagen, "rb") as file:
    image = bytearray(file.read())

for i, j in enumerate(image):
    image[i] = j ^ numero

with open("encrypt.jpg", "wb") as file:
    file.write(image)
