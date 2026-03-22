README PYTHON-CYBERTEC

1.#funcion isinstance(valor, tipo) es una función que verifica el tipo de dato.
  if isinstance(n, (float,int))

x ="str"
y = 1
def int_detect(x):
    if isinstance(x, (float,int)): 
        print("es float o int")
    else:
        print("no lo es")

int_detect(x)
int_detect(y)


# cuadro comparativo tipos de estructuras

| Estructura             | Símbolo          | Orden | Modificable | Repetidos   | Uso típico              |
| ---------------------- | ---------------- | ----- | ----------- | ----------- | ----------------------- |
| **Lista (list)**       | `[ ]`            | Sí    | Sí          | Sí          | colecciones que cambian |
| **Tupla (tuple)**      | `( )`            | Sí    | No          | Sí          | datos fijos             |
| **Set (conjunto)**     | `{ }`            | No    | Sí          | No          | eliminar duplicados     |
| **Diccionario (dict)** | `{ clave:valor } | Sí    | Sí          | clave única | datos tipo registro     |

| Tipo        | Mutable | Repetidos     | Acceso   |
| ----------- | ------- | ------------- | -------- |
| Tupla       | ❌       | ✔             | índice   |
| Lista       | ✔       | ✔             | índice   |
| Set         | ✔       | ❌             | no tiene |
| Diccionario | ✔       | claves únicas | clave    |


#concepto de variable 

VARIABLE: ES UNA PLABRA QUE GUARDA UN VALOR Y DICHO VALOR PUEDE SER CAMBIADO EN EL TIEMPO. DEPENDIENDO DEL TIPO DE DATO ASOCIADO, LA VARIABLE VA SEPARADO UN ESPACIO DE MEMORIA Y ASIGANARLE EL VALOR MINIMO.

# igual es "==" y uno solo "=" significa ASIGNAR 

#ejercicio #1

valor = 10
i = 2 
while (i <= valor): #similar a rango
    k = 0 #bandera 0=primo, 1= no primo
    j = 2 #numero con el que se puede dividir
    while (k==0)and(j<i): 
        if i%j == 0: #si es divisible
            k = 1
            break
        j = j+1
    if k == 0:
        print(i)
    i = i+1

#ejercicio #2

n = int(input("ingresa un num para mostrar su tabla"))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")  # \t separa en columnas
    print("*") 

#manejo de errores try_excepto

try:
    # código que puede fallar
except:
    # si ocurre error (print(f"mas la variable para trabajarla, {error}"))
else:
    # si NO ocurre error 
finally:
    # siempre se ejecuta ("puede tener una funcion extra, como contador")

#detalle extra 
🔹 except:
❌ Atrapa todos los errores (malo)
❌ Oculta problemas reales

🔹 except Exception:
✅ Más seguro
✅ Evita errores críticos

🔹 except ValueError:
🔥 Mejor práctica
✅ Captura error específico

#📌 COMANDOS BÁSICOS PARA USAR PYTHON EN TERMINAL (VS CODE)

🔹 dir
Muestra los archivos y carpetas dentro de la carpeta actual.

🔹 cd nombre_carpeta
Sirve para entrar a una carpeta.

🔹 cd ..
Sirve para regresar a la carpeta anterior.

#match similar a switch

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
#li[inicio:fin:paso]
#inicio -> desde donde empieza
#fin -> hasta donde(NO INCLUYE ESE INDICE)
#paso o salta -> cada cuanto avanza

li =[1,2,4,5]
print(li[1:3]) #2,4
print(li[:2]) #empieza desde 0, omite poner comienzo
print(li[:: 2]) #de dos en dos y agarro toda la lista , siempre imprime el 1ro y salta lo que dice

print(li[::-1]) #invierte la lista 

#------SET Y X.INTERSECTION(X2)
list1 = [1,2,3,4]
list2 = [5,3,7,9]
s1 = set(list1) #PROBAR QUITAR
s2 = set(list2)

ans = s1 & s2
print(ans)

print(s1.intersection(s2))


# fin de transcripcion del repaso 21/03




# ================================
# FUNCIONES DE STRINGS EN PYTHON
# ================================

# 🔹 split() → divide un texto en partes (lista)
texto = "hola mundo python"
resultado = texto.split()  
# ['hola', 'mundo', 'python']

texto2 = "manzana,pera,uva"
resultado2 = texto2.split(",")  
# ['manzana', 'pera', 'uva']


# 🔹 lower() → convierte a minúsculas
texto = "HOLA MUNDO"
resultado = texto.lower()  
# "hola mundo"


# 🔹 upper() → convierte a mayúsculas
texto = "hola mundo"
resultado = texto.upper()  
# "HOLA MUNDO"


# 🔹 strip() → elimina espacios al inicio y final
texto = "   hola mundo   "
resultado = texto.strip()  
# "hola mundo"


# 🔹 replace() → reemplaza texto
texto = "hola mundo"
resultado = texto.replace("hola", "adios")  
# "adios mundo"


# 🔹 find() → busca y devuelve la posición
texto = "hola mundo"
resultado = texto.find("mundo")  
# 5

# si no encuentra devuelve -1
resultado = texto.find("python")  
# -1


# 🔹 count() → cuenta cuántas veces aparece algo
texto = "hola hola hola"
resultado = texto.count("hola")  
# 3


# ================================
# ⚠️ IMPORTANTE
# ================================

# Estas funciones NO cambian el texto original
texto = "HOLA"
texto.lower()

print(texto)  
# "HOLA" (no cambió)

# ✔ forma correcta
texto = texto.lower()
print(texto)  
# "hola"

##---------------------DICIONARIOS
a1_dict= {"one":1, "two":2, "three":3} #"one"==identificado==KEYS, "1"==valor==VALUES
print(a1_dict["one"])

print(a1_dict.keys()) #muestra identificadores
print(a1_dict.values()) # muestra valores

#asignar valores
a1_dict["four"] = 4

#leer txt y csv

try: 
    with open("example2.txt", "x", encoding= "utf-8") as crear: 
        crear.write("Primer registro\n") 
except FileExistsError:
   print("el archivo ya se creo seguimos")

with open("example2.txt", "a", encoding="utf-8") as f:
   for lin in range(5):
      f.write(f"linea {lin}\n")
      print()

with open("example2.txt", "r", encoding="utf-8") as reader:
    for linea in reader:
       print(linea, end="")
