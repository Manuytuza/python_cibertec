#1 funcion isinstance(valor, tipo) es una función que verifica el tipo de dato.
x ="str"
y = 1
def int_detect(x):
    if isinstance(x, (float,int)): 
        print("es float o int")
    else:
        print("no lo es")

int_detect(x)
int_detect(y)
print(type(x))

print()

#2 cuadro comparativo tipos de estructuras
v0_lista =[4,5,6,6,7]
v1_tupla = (1, 2, 3, 1)  # datos inmutables y repetidos
v2_lista = [1, 2, 3, 4,5,6]  # datos modificables y repetidos
v3_set = {1, 1, 1, 1}    # datos agregables y NO repetidos (sin indice)
v4_dic = {"key1": 1, "key2": 2}  # clave:valor (sin indice)

# 🔹 Tupla (NO se puede modificar)
try:
    v1_tupla[0] = 1
except Exception as e:
    print("Error tupla:", e)

# 🔹 Lista (SÍ se puede modificar)
v2_lista[0] = "cambio_list"
v2_lista.append("append") #suma elementos
v2_lista.pop(0) #borra por indice
print("validacion list ")
print(2 in v2_lista) #validacion rapida
#seleccion detallada de listas :
print(v2_lista[1:3+1:2])#inicio:fin(si_el_ultimo):salta

print(set(v2_lista).intersection(set( v0_lista)) , "usando set y intersection")#usando set, habilitas intersection

# 🔹 Set (NO se accede por índice, se usa add)
v3_set.add("cambio_set")

# 🔹 Diccionario (se accede por clave)
v4_dic["key1"] = "cambio_dic"
v4_dic["key4"] = "nuevo" #agregar dic 

# 🔹 Obtener keys correctamente
print(v1_tupla)
print(v2_lista)
print(v3_set)
print(v4_dic)

#3 numeros primos mi version 
num = 1
fin = 3

while (num <= fin):
    es_primo=True #determina si es o no primo
    divisor=2
    while(es_primo)and(divisor<num):
        if num%divisor == 0: #si tiene residuo_0
            es_primo= False
            break
        divisor += 1
    if es_primo and num>1:
        print(num)
    num += 1

print()
#4 for_rango

for n in range(1,2+1):#+1 para incluir el fin
    print(n)

#5 control de errores y creacion de txt
try:
    with open("datos.txt", "x", encoding="utf-8") as crear:
        crear.write("se creo para el ejemeplo de README")
except Exception:
    print("txt creado")

try:
    archivo = open("datos.txt", "r")
except FileNotFoundError:
    print("Archivo no encontrado")
else:
    contenido = archivo.read()
    print("Contenido:", contenido)
finally:
    print("Cerrando proceso")

#6 match revisa casos 
def calculadora(n1,n2,operation):
        match operation :
            case "sum":
                return n1+n2
            case "rest":
                return n1-n2
            case _:
                return "operacion invalid"

try:
    n1 = 3#float(input("ingresa num 1"))
    n2 = 4#float(input("ingresa num 2"))
    operation = "rest" #input("ingresa sum o rest").lower()
except ValueError:
    print(ValueError)
else:
    print(calculadora(n1,n2,operation))
finally:
    print("fin")

#resumen 23/03
#7 funciones de string 
var_lower = "MAYUSCULA".lower() #print("maysucula"), vuelve minuscula
var_strip = "  hola  ".strip() #print("hola"), sin espacios
var_find = "dany,alice manu"
resultado =var_find.find("manu") #devulve indice de encontrarlo y -1 si no
print(resultado)
var_replace= "$ ?Manuel?"
print(var_replace.replace("$","").replace("?","").lower().strip()) #limpia str por caracter
print("")

#8 diccionario y funciones
dic_exam = {
    "nombre": "Manuel",
    "edad": 30,
    "nacionalidad": "peruana",
    "trabajo": "developer",
    "dreams": "helicopters"
}
dic_num ={
    "manuel": 30,
    "dany": 37,
    "alice":5,
    "emile": 13
}

print(dic_exam.keys()) #keys del diccionario
sum_dic = dic_num.values() #valores de cada key del dicionario
print(sum_dic)
print(sum(sum_dic)) #suma de los valores
print(dic_num.items()) #imprime keys + values del dic

#9 open csv and txt
try:
    with open("prueba.txt", "x", encoding="utf-8") as x:
        x.write("first line of the txt \n")
except Exception as e:
    print("archivo creado", e)

with open("prueba.txt", "a", encoding="utf-8") as a:
    for line in range(5):
        a.write(f"linea numero {line} of new txt create \n") #solo imprime un grupo para ams usamos f-string y \n crea salto de linea

with open( "prueba.txt", "r", encoding="utf-8") as r:
    for line in r:
        print(line, end="") # end="", quita separaciones
#10 date 
"""
import datetime as dt
import time

while True:
    hora = dt.datetime.now().strftime("%H:%M:%S")
    print(f"\r🕒 Hora actual: {hora}", end="") 
    #"\r" regresa a al misma linea
    #end=""evita salto de linea
    time.sleep(1) #le da un segundo de espera
"""

#11 limpieza y conteo de palabras 
texto = 'Buenas tardes, he notado consumos no reconocidos en mi tarjeta de crédito que no he realizado. Mis últimos consumos son del 4 de abril pero en el estado de cuenta de mi tarjeta de crédito aparecen consumos posteriores. Espero su pronta ayuda, abonando el monto de los consumos al saldo de mi tarjeta, gracias.'

# 🔹 1. Limpiar texto
lista = texto.replace('.', '').replace(',', '').lower().split()

# 🔹 2. Palabras a ignorar (stopwords)
stopwords = {"de", "la", "el", "en", "y", "que", "a", "los", "del", "mi"}

# 🔹 3. Filtrar palabras útiles
lista_filtrada = [w for w in lista if w not in stopwords]
print(lista_filtrada)

# 🔹 4. Contar frecuencia (forma PRO)
frecuencia = {}
for w in lista_filtrada:
    frecuencia[w] = frecuencia.get(w, 0) + 1
print(frecuencia)
# 🔹 5. Ordenar de mayor a menor
ranking = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

# 🔹 6. Mostrar resultados
print("🔢 Cantidad de palabras distintas:", len(frecuencia))

print("\n📊 Ranking de palabras:")
for palabra, veces in ranking:
    if veces == 1:
        print(f"{palabra} → {veces} vez")
    else:
        print(f"{palabra} → {veces} veces")

# 🔹 7. TOP 5
print("\n🔥 TOP 5 palabras más repetidas:")
for palabra, veces in ranking[:5]:
    print(f"{palabra} → {veces}")