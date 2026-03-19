import random

conv_user = 0

attack_ia = random.randint(1,3)

while True:
    attack_user = input("juguemos escribe: piedra, papel o tijera ").lower() #convierte todo a minuscula

    if attack_user == "piedra":
        conv_user= 1
        break
    elif attack_user == "papel":
        conv_user=2
        break
    elif attack_user == "tijera":
        conv_user=3
        break
    else:
        print("opcion invalida")


if conv_user == attack_ia:
    print(f"empate la ia eligio {conv_user}")
elif conv_user == 1 and attack_ia == 2:
    print("perdiste, elegiste piedra y IA papel")
elif conv_user == 2 and attack_ia == 3:
    print("perdiste, elegiste papel y IA tijera")
elif conv_user == 3 and attack_ia == 1:
    print("perdiste, elegiste tijera y IA piedra")
elif conv_user == 1 and attack_ia == 3:
    print("ganaste, elejiste piedra y la ia tijera")
elif conv_user == 2 and attack_ia == 1:
    print("ganaste, elejiste papel y la ia piedra")
elif conv_user == 3 and attack_ia == 2:
    print("ganaste, elejiste tijera y la ia papel")
else :
    print("imposible")


#juego chat gtp

opciones = {
    "piedra": 1,
    "papel": 2,
    "tijera": 3
}

nombres = {
    1: "piedra",
    2: "papel",
    3: "tijera"
}

attack_ia = random.randint(1, 3)

while True:
    attack_user = input("juguemos escribe: piedra, papel o tijera: ").lower()

    if attack_user in opciones:
        conv_user = opciones[attack_user]
        break
    else:
        print("opcion invalida2")

print(f"La IA eligió: {nombres[attack_ia]}")

# lógica del juego
if conv_user == attack_ia:
    print("Empate")
elif (conv_user == 1 and attack_ia == 3) or \
     (conv_user == 2 and attack_ia == 1) or \
     (conv_user == 3 and attack_ia == 2):
    print("Ganaste")
else:
    print("Perdiste")