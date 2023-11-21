# Solicitamos la clave al usuario
numero = int(input("Por favor, ingresa el número (clave): "))

# Leemos la imagen encriptada y la convertimos a bytes
with open("imagen_encriptada.jpg", "rb") as file:
    image = bytearray(file.read())

# Desencriptamos la imagen
for i, j in enumerate(image):
    image[i] = j ^ numero

# Guardamos la imagen desencriptada
with open("decrypted.jpg", "wb") as file:
    file.write(image)
