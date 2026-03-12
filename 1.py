print("first day of class to python")
# pasar google colap a visual
# jueves se generara un taller 
#  las tareas son d eun dia para el otro
#sacar el tipo de cambio de sedapar prosible ejemplo o practica
#vers cilicom valey - progresivo 
"""
libreria que mas se debe dominar es pandas -sintaxis
   funcion . Una función es un bloque de código que realiza una tarea específica y que puede reutilizarse varias veces.
   modelos: Un modelo es una representación simplificada de un problema o sistema real para analizarlo o predecir resultados.

NOTA DE PARTICPACION EJEMPLO DE UNA EMPRESA GRANDE Y SEGUN LO INVESTIGADO DONDE USAN EL PYTHON (CLOUD...)
“Netflix usa Python para analizar datos de más de 260 millones de usuarios y generar recomendaciones automáticas. Además, funciona en cloud computing, lo que permite manejar grandes volúmenes de información y mejorar la experiencia del usuario.”
“Instagram usa Python para manejar una plataforma con más de 2 mil millones de usuarios. Python ayuda a analizar datos, recomendar contenido y gestionar servicios en la nube.”

VARIABLE: ES UNA PLABRA QUE GUARDA UN VALOR Y DICHO VALOR PUEDE SER CAMBIADO EN EL TIEMPO. DEPENDIENDO DEL TIPO DE DATO ASOCIADO, LA VARIABLE VA SEPARADO UN ESPACIO DE MEMORIA Y ASIGANARLE EL VALOR MINIMO.

= ES ASIGNAR 

"""
x = 4
print (x)
x = True
print (x)

if (x < 3) : 
   print ("menor que 3")
elif (x > 4) :
   print ("mayor que 10")
else :
   print("es 5")

def sumar (x,y) :
   return x + y 
print(sumar (x,5))

#jupyter notebook de comando en terminal 
# ejercicios if and def
def impar_par (number):
   if number % 2 == 0 : 
      print ("es par")
   else :
      print("es inpar")

impar_par(3)
impar_par(4)

def mayor_menor (edad):
   if edad > 18 :
      print("mayor age")
   else :
      print("menos age")

mayor_menor(20)
mayor_menor(5)

def num_more_less (a,b):
   if a < b :
      print("a<b")
   elif a == b:
      print("son =")
   else:
      print("b>a")

num_more_less(2,3)
num_more_less(1,1)
num_more_less(10,4) 

def aproub_reproub (nota):
   if not isinstance( nota , (int,float)) : # isinstance(valor, tipo) es una función que verifica el tipo de dato.
      print ("debes escribir float or int")
      return #esto detiene def 

   if nota < 11:
      print("reproub")
   elif nota == 11:
      print ("mediocre")
   else :
      print ("aprobado")

aproub_reproub(11)
aproub_reproub(25)
aproub_reproub("hola")

#insistance es como typeof de js, valida el type 

numbers = (1,2,3)
for i in numbers :
   print (i)

## lista = [], se puede cambiar datos
list_1 = [1,2,3,4]
list_1.append(5)
list_1 [0] = 2
print(list_1)

## tuple =(), no se puede cambiar datos
tuple_1 = (1,2,3)
print(tuple_1[1])

## set = {} , los reptidos desaparecen y no tiene indice
set_1 = {1,2,3,3,3,3}
print (set_1)

"""
| Estructura             | Símbolo          | Orden | Modificable | Repetidos   | Uso típico              |
| ---------------------- | ---------------- | ----- | ----------- | ----------- | ----------------------- |
| **Lista (list)**       | `[ ]`            | Sí    | Sí          | Sí          | colecciones que cambian |
| **Tupla (tuple)**      | `( )`            | Sí    | No          | Sí          | datos fijos             |
| **Set (conjunto)**     | `{ }`            | No    | Sí          | No          | eliminar duplicados     |
| **Diccionario (dict)** | `{ clave:valor } | Sí    | Sí          | clave única | datos tipo registro     |

"""

## dicionario dicc = {"x": "rambo", "age":35}

person1 = {
   "nombre" : "Manuel",
   "age" : 30
 }
print(person1["nombre"])

list2 = [1,2,3]

# enumerate permite ver el indice 
for valor, indice in enumerate(list2):
   print (valor, indice)

