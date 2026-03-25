"""
PROBLEMA
En una tienda de tecnología se registran las ventas del día en una lista, donde el iPhone tiene un costo de 400 soles, y se necesita una solución que permita calcular cuántas veces se vendió este producto y el ingreso total generado mediante una sola función.
"""
def control_ventas(lista_ventas, producto, precio):
    cantidad = lista_ventas.count(producto) # Contar cuántas veces se vendió el producto
    
    ingreso = cantidad * precio    # Calcular ingreso total

    return cantidad, ingreso # Retornar resultados


# Lista de ventas del día
ventas = ["iphone", "ipad", "iphone", "macbook", "iphone"]

# Datos del producto a analizar
producto = "iphone"
precio = 400

# Uso de la función
cantidad, ingreso = control_ventas(ventas, producto, precio)

# Resultados
print("Producto:", producto)
print("Cantidad vendida:", cantidad)
print("Ingreso total:", ingreso)



#------------------------------------------------------------

# Lista de notas de estudiantes
notas = []
 
# Función li
def li(op, lista, valor=0):
    if op == "agregar":
        lista.append(valor)
        return lista
    elif op == "promedio":
        if len(lista) == 0:
            return 0
        return sum(lista) / len(lista)
 
# Uso del programa
li("agregar", notas, 15)
li("agregar", notas, 18)
li("agregar", notas, 12)
 
promedio = li("promedio", notas)
 
print("Notas:", notas)
print("Promedio:", promedio)
 
 # Registrar los estudiantes que asisten a clase
# Lista de asistencia
asistencia = []
 
# Función li
def li(lista, nombre):
    lista.append(nombre)
 
# Registrar asistencia
li(asistencia, "Ana")
li(asistencia, "Luis")
li(asistencia, "María")
 
# Mostrar asistencia
print("Asistieron a clase:", asistencia)

#----------------------------------------------------------------------------
#detectar productos faltantes
def productos_faltantes(productos_esperados, stock_actual):
    faltantes = []
   
    for producto in productos_esperados:
        if producto not in stock_actual:
            faltantes.append(producto)
   
    return faltantes
 
 
# Ejemplo
esperados = ["arroz", "azucar", "leche", "huevos"]
stock = ["arroz", "leche"]
 
print(productos_faltantes(esperados, stock))  
#-----------------------------------------------------------------------------------
import pandas as pd

alumnos = []

while True:
    nombre = input("Nombre del alumno: ")
    nota = float(input("Nota: "))

    alumno = {
        "nombre": nombre,
        "nota": nota
    }

    alumnos.append(alumno)

    continuar = input("¿Agregar otro alumno? (s/n): ")
    if continuar.lower() != "s":
        break

df = pd.DataFrame(alumnos)
print(df)

# Filtrar alumnos con nota menor a 11
df_tutoria = df[df["nota"] <= 11]
print(df_tutoria)

# Guardar lista en CSV
df_tutoria.to_csv("alumnos_tutoria.csv", index=False)

#------------------------------------------------------------------------------------------

# Lista de transacciones de hoy. Cada elemento es una pequeña lista: [ID_Cliente, Estado_Compra]
transacciones_hoy = [
    [101, "completada"],
    [102, "fallida"],
    [103, "completada"],
    [101, "completada"],
    [104, "cancelada"],
    [105, "completada"]
]
 
# Lista de clientes VIP del día de ayer
vip_ayer = [103, 105, 106, 107]
 
# Filtrar + unir + eliminar duplicados en menos pasos
lista_final = list({
    t[0] for t in transacciones_hoy if t[1] == "completada"
}.union(vip_ayer))
 
#lista final y limpia para enviar correos
print("Lista final:", lista_final)
 