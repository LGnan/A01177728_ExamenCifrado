# Validamos que el número ingresado sea un entero
while True:
    try:
        numero = int(input("Por favor, ingresa el número (clave): "))
        break
    except ValueError:
        print("Por favor, ingresa un número entero.")

with open("encrypt.jpg", "rb") as file:
    image = bytearray(file.read())

for i, j in enumerate(image):
    image[i] = j ^ numero

with open("decrypted.jpg", "wb") as file:
    file.write(image)
