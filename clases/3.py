#FUNCIONES_ERRORE_IMPORT
#FUNCIONES
#LO CORRECTO NO ES QUE DEVUELVA PRINT es que devulva RETURN

"""
def name_function(parametros):
    #bloque de codigo
    return resultado 

def sumar(a,b):
    resultado = a + b
    return resultado


def sumar1(a,b):
    return a + b

print(sumar1(1,2))
print(sumar(1,2))
"""
#import
import random
import math
# import pandas #se debe que isntalar previamente 

#$$$$$$$$$$$$$$$$$$$$$$
#examen crea una funcion donde intervenga varias variables 

#ver ejercicoos de estructuras de control
#ver las de hora en pdf 

#COLECCIONES
  #LISTA: datos_mixtos, alterable, lista =[1,2,3,True]
  #DICCIONARIO dic_1 = {"persona":"Manuel","edad": 14}, APIs
  #TUPLAS: no_modificables coordenadas = (123332,222222)
  #VECTOR = ordenado, mismo tipo vec=[10,20,30,40]
  #CONJUNTOS: NO PERMITE DUPLICADOS 

def multiplica_por_5(num):
  print(f"{num} x 5 = {num*5}")
  
# sourcery skip: aug-assign, while-to-for
multiplica_por_5(7)

  
anio = 2005
while anio <= 2018:
    print("informes del año", anio)
    anio += 1       #anio +1


#usando una excepcion
x = "hols"
try:
    if x>5:
        print("mayor5")
    else:
        print("<=5")
except Exception: #es para python
    print(x,"the number is incorrect")


valor = 10
i = 2 

while (i <= valor): #similar a rango
    k = 0 #bandera 0=primo, 1= no primo
    j = 2 #numero con el que se puede dividir
    while (k==0)and(j<i): 
        if i%j == 0: #si es divisible
            k = 1
            break
        j += 1
    if k == 0:
        print(i)
    i = i+1


#tarea para revisar 
# tamaño de la tabla
n = int(input("ingresa un num para mostrar su tabla"))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")  # \t separa en columnas
    print("*") 

"""
try:
    # código que puede fallar
except:
    # si ocurre error
else:
    # si NO ocurre error
finally:
    # siempre se ejecuta
"""