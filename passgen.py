import random

password = "+-_/*!&$#?=@abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
length = int(input("longitud de la contraseña: "))

#generar la contraseña
def generate_password(length):
    pwd = ""
    for i in range(length):
        pwd += random.choice(password)
    print("tu contraseña es: " + pwd)

generate_password(length)
