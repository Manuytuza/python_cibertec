#ERRORES - Python usa tipos de errores predefinidos. Uno de ellos es ZeroDivisionError. Hacer uso de este tipo de error para implementar una rutina de manejo de divisiones en general y reconocer la división por cero.

#Funcion para dividir numeros sin errore
def div(n1,n2):
    try:
        resultado = n1 / n2
        residuo = n1 % n2

        print("Resultado:", resultado)
        print("Residuo:", residuo)

    except ZeroDivisionError: #print si el error es por div_0
        print("Error: No se puede dividir entre 0")
    except Exception as e: #imprimimos el error4
       print("Error detectado:", e)

print("Programa para dividir dos numeros")

while True:
    try: # ingresamos los datos a dividir
      user_div_1= int(input("ingresa el primer numero a dividir "))
      user_div_2= int(input("ingresa el segundo numero a dividir "))

    except ValueError: #filtro de tipo de dato
      print("Error: ingresa numeros validos")
      continue

    div(user_div_1 ,user_div_2)

#validamos si el usario quiere continuar
    opcion= input("Quiere realizar otra diviciôn? (s/n): ").strip().lower() #texto sin espacios ni mayusculas
    if opcion not in("s", "si"):
      print("programa finalizado")
      break


#Escribe un programa en Python que le pida al usuario ingresar un número. El programa debe intentar convertir ese valor a un número entero. Usa una estructura try – except para manejar el error en caso de que la conversión falle (por ejemplo, si el usuario ingresa texto en lugar de un número).

print("Convertiremos cualquier numero a entero")

def convertidor(x): #funcion convertidora
  try:
    var_clean = x.strip()   #.strip() quita espacios
    var_conver = int(round(float(var_clean)))
    # float permite ingreso de decimales
    # round redondea el numero
    print(f"El numero convertido es: {var_conver}")
    return False

  except ValueError: #numero ingresado invalido
    print("Error: numero invalido")
    return True

  except Exception as e: #otros errores se almacenan en e
    print("Error detectado: ", e)
    return True

var_continue= True #variable que determina fin de funcion

while var_continue:
  input_user =input("ingresa un numero: ")
  var_continue= convertidor(input_user)
