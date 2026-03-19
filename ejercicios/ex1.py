#ejemplo compañero 1
amigas = ["MaryCarmen", "Estefania", "Lesly", "Carina"]
busqueda=input("Ingrese un nombre: ")
existe=False 
for nombre in amigas:
  if nombre == busqueda:
    existe=True
    print("¡Encontré a {0} en la lista!".format(busqueda))
    break # Detiene el bucle de inmediato
 
if not existe:
  print("No encontré a {0} en la lista".format(busqueda))

#---------------------------------------------------------------------------------
#ejemplo compa_2
#---------------------------------------------------------------------------------
import random
 
# --- CONTROL DE CALIDAD INDUSTRIAL: iterando a través de 10 productos, generando pesos aleatorios, y clasifica si cada producto es "Aceptado" (considerando peso mínimo) o "Rechazado", imprimiendo al final el estado de cada uno.
total_productos = 10
peso_minimo = 500 # Peso mínimo en gramos para aceptación
 
print(f"Iniciando control de calidad para {total_productos} productos...")
 
# --- Bucle FOR con RANGE ---
# range(1, 11) genera números del 1 al 10
for i in range(1, total_productos + 1):
 
    # Genera un peso aleatorio para el producto (entre 450g y 550g)
    peso_producto = random.randint(450, 550)
 
    # --- Estructura IF / ELSE ---
    if peso_producto >= peso_minimo:
        # Se ejecuta si la condición es verdadera
        estado = "✅ Aceptado"
    else:
        # Se ejecuta si la condición es falsa
        estado = "❌ Rechazado"
 
    # Imprime el resultado de cada iteración
    print(f"Producto {i}: Peso {peso_producto}g - Estado: {estado}")
 
print("\nControl de calidad finalizado.")

#---------------------------------------------------------------------------------
#ejemplo compa_3
#---------------------------------------------------------------------------------
numero = input("Ingresa un número: ")
 
contador = 0
 
for digito in numero:
    if digito == "0":
        contador += 1
 
print("Cantidad de ceros:", contador)
#---------------------------------------------------------------------------------
#ejemplo compa_4
#---------------------------------------------------------------------------------
# vector de edades
edades = [19, 20, 28, 32, 21]
 
suma = 0
 
# recorrer el vector
for edad in edades:
    print("Edad:", edad) #la variable suma se conoce como un  acumular
 
    # acumulamos las edades
    suma = suma + edad
 
# calcular promedio
promedio = suma / len(edades)
 
print("Promedio de edades:", promedio)
#---------------------------------------------------------------------------------
#ejemplo compa_5
#---------------------------------------------------------------------------------
numero = int(input("Ingresa un número: "))
 
factorial = 1
 
for i in range(1, numero + 1):
    factorial *= i
 
print("El factorial de", numero, "es:", factorial)

#---------------------------------------------------------------------------------
#ejemplo compa_6
#---------------------------------------------------------------------------------
texto = "Esta es una cadena"
caracter = "a"
z = [i for i, letra in enumerate(texto) if letra == caracter]
print(z)
r = max(z)
print("El tamaño de la cadena es:",r+1)
#---------------------------------------------------------------------------------
#ejemplo compa_7
#---------------------------------------------------------------------------------
notas = [12, 8, 15, 9]
minima = int(input("Ingrese la nota mínima: "))
 
for n in notas:
    if n >= minima:
        print(n, "Aprobado")
    else:
        print(n, "Desaprobado")

#---------------------------------------------------------------------------------
#ejemplo compa_8
#---------------------------------------------------------------------------------

var_pelicula = {'titulo':'Avatar','director':'James Cameron','genero':'ciencia ficcion'}
# si solo quiero ver las claves y valores
for clave,valor in var_pelicula.items():
    print(clave+":",valor)

# si solo quiero ver las claves
for clave in var_pelicula.keys():
    print(clave)

# si solo quiero ver los valores
for valor in var_pelicula.values():
    print(valor)

#---------------------------------------------------------------------------------
#ejemplo compa_9
#---------------------------------------------------------------------------------
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
 
productos = [
    Producto("Laptop", 1200, 3),
    Producto("Mouse", 25, 10),
    Producto("Teclado", 45, 0)
]
 
for producto in productos:
    if producto.stock > 0:
        print(producto.nombre, "tiene stock y cuesta", producto.precio)
    else:
        print(producto.nombre, "no tiene stock")
 
#---------------------------------------------------------------------------------
#ejemplo compa_10
#---------------------------------------------------------------------------------
 