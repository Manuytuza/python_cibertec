""""
import random

secret_num = random.randint(1,10)
point = 9

print("Adivina un número del 1 al 10")
print("Tienes 5 intentos y incias con 9 point")
print("Cada error resta 2 y ganar suma 10")
print("Gana >= 10 point")
print("Muere el que quede sin puntos")

for i in range(5):
  print()
  user_num = int(input("ingresa el numero: "))
  if user_num == secret_num:
    point = point + 10
    print("intento",i+1,": acertaste","tu vida es",point)
    print("Ganaste")
    break
  elif user_num < secret_num:
    
    point = point -2
    print("intento",i+1,": te equivocaste tu vida es",point)
    print("pista: el numero es mayor")

  else:
    point = point -2
    print("intento",i+1,": te equivocaste tu vida es",point)
    print("pist: el numero es menor")

  if point < 1 :
    print("morirste")
    break

print("el numero es:", secret_num)
    
"""
# Imprime una "flecha" de asteriscos que sube hasta 6 y luego baja
