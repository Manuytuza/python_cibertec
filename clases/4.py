#subir tarea a visual antes de siguiente clase = listo
#revisar ejericios del dia martes PDF = falta

def calcu_2(n1,n2,oper_name):
    match oper_name:
      case "suma":
        return n1+n2
      case "resta":
        return n1-n2
      case "multiplicacion":
        return n1*n2
      case "division" if n2 != 0:
        return n1/n2
      case "division": #aqui n2 entendemos que es 0
        return "no se puede div entre 0"
      case _: #similar a else
        return "operacion invalid"

#calcu_2(1,4, "suma")
#vector es rigido mismo tipo de datos, lista es mas flexible
#type : permite ver tipo de dato
print(type([])) 
#VER STREP DE PANDAS, PDF_2
#POR INVESTIGAR. QUE ES UN ESCRAPEO
#LISTA
#.append
li = []
li.append(1)
li.append(2)
li.append(4)
li.append(3)
print(li)

li.pop() #elimina el ultimo element

print(li)

li[0]="cambia posicion 0"
print(li)
print(li[-1]) #ultimo elemento
#------------------------------------------------------------------------
# LISTAS EN PYTHON - RESUMEN RÁPIDO

lista = [1, 2, 3]

# Agregar elementos
lista.append(4)        # agrega al final
lista.insert(1, 100)   # agrega en posición específica

# Eliminar elementos
lista.remove(100)      # elimina por valor
lista.pop()            # elimina último elemento
lista.pop(0)           # elimina por índice

# Ordenar y modificar
lista.sort()           # ordena de menor a mayor
lista.reverse()        # invierte la lista

# Información de la lista
len(lista)             # cantidad de elementos
lista.count(2)         # cuántas veces aparece un valor
lista.index(3)         # posición de un valor

# Acceso a elementos
lista[0]               # primer elemento
lista[-1]              # último elemento

# Verificar si existe un valor
2 in lista             # True o False
#--------------------------------------------------------------------
#li[inicio:fin:paso]
#inicio -> desde donde empieza
#fin -> hasta donde(NO INCLUYE ESE INDICE)
#paso o salta -> cada cuanto avanza

li =[1,2,4,5]
print(li[1:3]) #2,4
print(li[:2]) #empieza desde 0, omite poner comienzo
print(li[:: 2]) #de dos en dos y agarro toda la lista , siempre imprime el 1ro y salta lo que dice

print(li[::-1]) #invierte la lista 
#--------------------------------------------------------
#PARTICIPACION  DE UN CASO DE USO PARA USAR ALGUNA DE ESTAS OPERACIONES, CAPUTARS UNA LISTA Y EJECUTAS ALGUNA DE ESTAS OPERACIOENS PERO CON CONTEXTO USO REAL #######
#--------------------------------------------------------

#VER SI UN EL,MENTO EXITE
print( 1 in li)
print(len(li))

#practica
#de dos listas identificar si existe al menos algun elemento en comun - sin for 
#set: conjunt, ahce que solamente consideres elmentos unicos NO _REPETIDOS
list1 = [1,2,3,4]
list2 = [5,3,7,9]
s1 = set(list1) #PROBAR QUITAR
s2 = set(list2)

ans = s1 & s2
print(ans)

print(s1.intersection(s2))

#ejemplo de set
lix =[1,2,2,2,3,4,4,4] #validar no es como yuna tupla
print(set(lix))

#  | : une listas_ conjuntos
a1_set = {1,2,3,4}
a2_set = {3,4,5,6}

print(a1_set  | a2_set)

#split(): devuelve un lista con la cadena de caracteres por cada indice de la lista, corta
cad = "manuel ytuza cusirramos"
cad.split()

print()
print(cad.split("a")) #corta cuando encuentra la "a"

#devuelve una cadena de carteres convertido a lo opuesto sea MAY o MIN
cad2 = "Luis lopez"
cad2.swapcase ()

##---------------------DICIONARIOS
a1_dict= {"one":1, "two":2, "three":3} #"one"==identificado, "1"==valor
print(a1_dict["one"])

print(a1_dict.keys()) #muestra identificadores
print(a1_dict.values()) # muestra valores


#fin de secion de tarde   

#-------------------------------------------------------------------------------------------------


#asignar valores
a1_dict["four"] = 4
print (a1_dict)
print(a1_dict.items())

#sumar
dict_1 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}

nvalues = dict_1.values()
print(sum(nvalues))
#recordar a profe scrip de PANDAS

#csv y txt, que es
# Abrir y leer un archivo de texto (línea por línea)


#subir txt solo lectura
with open("dog_breeds.txt", "r", encoding="utf-8") as reader:
    for linea in reader:
        print(linea, end="")
#subir csv solo lectura
with open("birthday.csv", "r") as archivo_csv:
    for linea in archivo_csv:
        columnas = linea.strip().split(",")
        print(columnas)

#que es un DATA FREIN,  df
try: 
    with open("example2.txt", "x", encoding= "utf-8") as crear: 
        crear.write("Primer registro\n") 
except FileExistsError:
   print("el archivo ya se creo seguimos")

dic_ventas = {
   "macbook": 600,
   "ipad": 300,
   "iphone_17e":400
}
  
with open("example2.txt", "a", encoding="utf-8") as f:
    for item,key in dic_ventas.items():
      f.write(f"el producto {item} cuesta {key}\n")


with open("example2.txt", "a", encoding="utf-8") as f:
   for lin in range(5):
      f.write(f"linea {lin}\n")
      print()

with open("example2.txt", "r", encoding="utf-8") as reader:
    for linea in reader:
       print(linea, end="")