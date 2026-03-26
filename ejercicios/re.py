#Escribir una función que genere una lista de números enteros aleatorios (debe ingresar el número de valores a generar) y que devuelva las siguientes salidas: Una lista ordenada con los números pares, una lista ordenada con los números impares y la cantidad de números de cada lista final.

"""
import random

cantidad =int(input("cuantos num aleatorio generamos?"))

def random_f(cantidad):
    nums =[]

    #genera lista random
    for x in range(cantidad):
        nums.append(random.randint(1,100))

    list_par =[]
    list_inpar=[]

    #agraga numeros pares e impares
    for n in nums:
        if n%2 == 0:
            list_par.append(n)
        else:
            list_inpar.append(n)
    
    #ordenar listas
    list_inpar.sort()
    list_par.sort()
    
    print(list_par)
    print(list_inpar)    
    print("numero de impares",len(list_inpar))
    print("numero de pares",len(list_par))  

random_f(cantidad)
##level2

def random_f(cantidad):
    numeros = [random.randint(0, 100) for _ in range(cantidad)]
    
    pares = sorted([n for n in numeros if n % 2 == 0])
    impares = sorted([n for n in numeros if n % 2 != 0])
    
    print("Original:", numeros)
    print("Pares:", pares)
    print("Impares:", impares)
    print("Cantidad pares:", len(pares))
    print("Cantidad impares:", len(impares))

### Pregunta 3 (3 puntos)

Escribir un programa que simule un juego de adivinar una palabra. El programa debe realizar lo siguiente:

* El programa debe preguntar al usuario la palabra a adivinar. A partir de la palabra introducida debe crear una lista con los caracteres de la palabra.
* Después debe ir preguntando al usuario por letras hasta un máximo de 5 fallos o hasta que no queden letras en la lista. En ambos casos el programa terminará pero mostrará el mensaje “Perdiste” si se comenten 5 fallos y el mensaje “Ganaste” si no quedan palabras en la lista.
* La letra debería contar así esté en mayúscula o minúscula.
* Cada vez que el usuario introduzca una nueva letra, si la letra está en la lista se eliminará y mostrará el mensaje “CORRECTO”, mientras que si la letra no está en la lista mostrará el mensaje “FALLO”. Si la letra está más de una vez en la lista, se eliminarán todas las posiciones donde aparezca.
* EXTRA: Cada vez que el usuario acierte una letra debe mostrar la palabra a adivinar con las letras acertadas hasta el momento y el resto reemplazadas por asteriscos.
"""
word = list(input("que palabra adivinaremos: ").lower().strip())
print(word)
secret_word =["*"]*len(word)
print(secret_word)

intentos = 0
while intentos < 5 and any(word):
    user =input("ingresa una letra o vocal").lower()
    if user in word:
        print("correcto")
        for i in range(len(word)):
            if word[i] == user:
                word[i] = False
                secret_word[i] = user
    else:
        print("fallo")
        intentos += 1
        print("te quedan", 5 -intentos)
    
    print("progreso", secret_word)

if intentos == 5:
    print("fin del game")
else:
    print ("ganaste")

#-------codigo de exmane
ingreso = float(input("Ingresa monto total de renta anual: "))
renta = ingreso - 30800

if renta <= 0:
    a = 0

elif renta <= 22000:
    a = renta * 0.08
    print(f"tramo uno {a:.2f}")

elif renta <= 88000:
    a = (renta - 22000) * 0.14 + 22000 * 0.08
    print(f"tramo dos {a:.2f}")

elif renta <= 154000:
    a = (renta - 88000) * 0.17 + 66000 * 0.14 + 22000 * 0.08
    print(f"tramo tres {a:.2f}")

else:
    a = (renta - 154000) * 0.20 + 66000 * 0.17 + 66000 * 0.14 + 22000 * 0.08
    print(f"tramo cuatro {a:.2f}")


