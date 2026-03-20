#ERRORES - Python usa tipos de errores predefinidos. Uno de ellos es ZeroDivisionError. Hacer uso de este tipo de error para implementar una rutina de manejo de divisiones en general y reconocer la división por cero.

#Funcion para dividir numeros sin errore
def div(n1,n2):
    try:
        resultado = n1 / n2
        residuo = n1 % n2

        print("Resultado:", resultado)
        print("Residuo:", residuo)
            
    except ZeroDivisionError:
        print("Error, 0 no es valido para div")
    except Exception as e:
       print("Error detcectado:", e)

print("Programa para dividir dos numeros")

try:
  user_div_1= int(input("ingresa el primer numero a dividir "))
  user_div_2= int(input("ingresa el segundo numero a dividir "))

except ValueError:
  print("Error: ingresa numeros validos")

else:
    div(user_div_1 ,user_div_2)