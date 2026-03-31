"""
x = 1
if isinstance(x , (float,int)):
    print("es float o int")
else:
    print("no es")
#-------------
l1=[1,2,3,4,5,6]
l2=[4,5,"cabeza",8]
l1.append("cabeza")
print(l1)
print(f"slicing {l1[0:4+1:2]}")
print(f"intersection y set vueve conjuntos{set(l1).intersection(set(l2))}")
#--------------
l3=[]
for n in range(1,4+1):
    l3.append(n)
    print(l3)
#for n in range(len(l1)):
    #l1[n] = str(l1[n]) + "r"
#[expresion for elemento in lista if condicion]
l4 = [str(x)+ "r" for x in l1 if x!="cabeza"]
print(l4)
l1.pop(6)#pars que fucnion el for-if, ya que str genera TypeError
l5= [x**2 for x in l1 if x >= 4]
print(l5)
#-------------- 
def calculator(x,y,operation):
    match operation:
        case "+":
            return x+y
        case "-":
            return x-y
        case _:
            return "operacion no generada"

# ValueError: ocurre cuando el valor no es válido (ej: int("hola"))
# TypeError: ocurre cuando mezclas tipos incompatibles (ej: 5 + "a")
# Exception: clase general que captura cualquier error no específico
try:
    x=float(input ("ingresa x"))
    y=float(input("ingresa y"))
    operation=input("ingresa la operacion + o -")

    print(calculator(x,y,operation))
except ValueError as v:
    print(f"ValueErro:  {v}")
except Exception as e:
    print(f" Exception: {e}")

#--------
v1 = "Ejemplo $  "
print(v1)

v1l=v1.replace("$","").lower().strip()#nose guarda automatico #lower()vuelve minuscula #strip()quita espacios
print(v1l)

#----------
import pandas as pd 

dic_m = [
    {
    "nombre": "Manuel",
    "edad": 30,
    "nacionalidad": "peruana",
    "trabajo": "developer",
    "dreams": "helicopters"
    },
    {
    "nombre": "Alice",
    "edad": 5,
    "nacionalidad": "peruana",
    "trabajo": "developer",
    "dreams": "unicornios"   
    },
    {
    "nombre": "mita",
    "edad": 70,
    "nacionalidad": "peruana",
    "trabajo": "developer",
    "dreams": "unicornios"   
    },
    {
    "nombre": "amor",
    "edad": 37,
    "nacionalidad": "peruana",
    "trabajo": "developer",
    "dreams": "unicornios"   
    }
]

#si no puede convetir en ves de botar errore vota errors="coerce"
df =pd.DataFrame(dic_m)
#def dic_def():
   # for n in dic_m:
#crea nueva columna
df["comidas_favorita"] = list(range(4))
#print(df["dreams"])
print("")
#filtrar 
old_age = df[df["edad"]>18]
#print(old_age)
print("")
#ordenar sort
print(df.sort_values("edad", ascending=False))

data = [
    {"vendedor": "Jenny", "producto": "iPhone", "ventas": 5},
    {"vendedor": "Ana", "producto": "iPhone", "ventas": 4},
    {"vendedor": "Jenny", "producto": "Audifonos", "ventas": 3},
    {"vendedor": "Ana", "producto": "Audifonos", "ventas": 1},
    {"vendedor": "Johana", "producto": "iPhone", "ventas": 2}
]

#groupby: agrupa
df1 = pd.DataFrame(data)
print(df1)
print(df1.columns)
print("")
print(df1.groupby("vendedor")["ventas"].sum().sort_values())
print("")

print(df1.groupby("vendedor")["ventas"].agg(["sum", "mean", "count"]))
print("")
#drop :elimina necesita donde almacenar y definir axis = 0,1
f1 = df1.drop([0], axis=0) # elimina FILA
print(f1)  
print ("")

f2 = df1.drop(['vendedor'], axis=1)  # elimina COLUMNA
print(f2)

#crear columna calculada
df1["monto"] = df1["ventas"] *100
print(df1)

df3 = pd.read_excel("panda.xlsx")
print(f"primer 5 filas {df3.head()}") #primer 5
print(f"informacion de todo {df3.info()}") #informacion
print(f" nombres de columnas {df3.columns}") #columnas
print(f" ultimas 10 filas {df3.tail(10)}") #ultima 10 filas
print(f" valores resumidos {df3.values}") #valores resumidos
print(f"suma de vacios por fila {df3.isna().sum()}") #suma de 0 por columna
df3["Score"] = df3["Score"].fillna("fillna -nan")
print(df3["Score"])
print("----------")
print(df3.iloc[0])  # primera fila
dic1 = {
    1: "primo",
    2: "second",
    3: "three"
}
#map usa un dic para actualizar valores, si no encuentra nan
#df3["Attempts"] = df3["Attempts"].astype(int) #convierte a int 
df3["Attempts"] = df3["Attempts"].map(dic1)
print(df3["Attempts"]) #imprime columna
print("")

#apply aplica una funcion def
def multiplicar(x):
    return x * 2

df3["Score"] = df3["Score"]. apply(multiplicar)
print(df3["Score"])

#replace() cambia lo que encuentra 

df3["Score"]= df3["Score"].replace({
    25.00 : "replace",
    18.0 : "replace2"
})

print(f"el temaño es {len(df3)}") #confirma tamaño de filas
print(df3["Score"]) 

df3["brain"] = range(len(df3))
#valida si existe el archivo antes de crear

#imprimir todo el df
print(df3.to_string()) 
import os
import datetime

if os.path.exists("panda_mediano.csv"):
    print("panda_mediano.csv existe y sera modificado")

try:
    df3.to_csv("panda_mediano.csv", index= True, encoding="utf-8")
    print("secreo panda_mediano.csv")
except Exception as e:
    print(f"error al crear csv {e}")
"""
#seguimos 29/03
import pandas as pd
import random

df =pd.read_csv("panda_mediano.csv",  index_col=False)
print(df.axes) #.axes permite ver filas y nombres de columnas

df.sort_values(by=["Name"], inplace=True) 
#ascending=True, ya esta por defecto
print(df)

#eliminar columna , axis=1 columnas y 0 filas
df = df.drop(["Unnamed: 0"], axis= 1)
df = df.drop([4], axis= 0)

#aumentar una columna random
df["new_column"]=[random.randint(1,100) for _ in range(len(df))]
print(df)

#usar funcion mas .apply(def)
def cambio(x):
    if x == "replace":
        return 1
    elif x == "replace2":
        return 2
    else:
        return x

df["Score"] = df["Score"].apply(cambio)
print(df["Score"]) 

