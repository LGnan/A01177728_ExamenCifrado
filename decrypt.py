# Solicitamos al usuario que ingrese el número
numero = int(input("Por favor, ingresa el número (clave): "))

# Abrimos la imagen encriptada y la convertimos a bytes
with open("imagen_encriptada.jpg", "rb") as file:
    image = bytearray(file.read())

# Aplicamos la operación XOR a cada byte de la imagen para desencriptarla
for i, j in enumerate(image):
    image[i] = j ^ numero

# Guardamos la imagen desencriptada en un archivo llamado "decrypted.jpg"
with open("decrypted.jpg", "wb") as file:
    file.write(image)
