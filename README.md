#funcion isinstance(valor, tipo) es una función que verifica el tipo de dato.

def aproub_reproub (nota):
   if not isinstance( nota , (int,float)) :

# cuadro comparativo tipos de estructuras

| Estructura             | Símbolo          | Orden | Modificable | Repetidos   | Uso típico              |
| ---------------------- | ---------------- | ----- | ----------- | ----------- | ----------------------- |
| **Lista (list)**       | `[ ]`            | Sí    | Sí          | Sí          | colecciones que cambian |
| **Tupla (tuple)**      | `( )`            | Sí    | No          | Sí          | datos fijos             |
| **Set (conjunto)**     | `{ }`            | No    | Sí          | No          | eliminar duplicados     |
| **Diccionario (dict)** | `{ clave:valor } | Sí    | Sí          | clave única | datos tipo registro     |

#concepto de variable 

VARIABLE: ES UNA PLABRA QUE GUARDA UN VALOR Y DICHO VALOR PUEDE SER CAMBIADO EN EL TIEMPO. DEPENDIENDO DEL TIPO DE DATO ASOCIADO, LA VARIABLE VA SEPARADO UN ESPACIO DE MEMORIA Y ASIGANARLE EL VALOR MINIMO.

# igual es "==" y uno solo "=" significa ASIGNAR 

#ejercicio #1

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
