# TIPOS DE FOR EN PYTHON + EJEMPLOS

# 1. FOR DIRECTO (recorre elementos)
numeros = [1, 2, 3, 4]

print("FOR directo:")
for num in numeros:
    print(num)

# 2. FOR CON ÍNDICE (range + len)
# Recorre usando posiciones (índices)
numeros = [10, 20, 30]

print("\nFOR con índice:")
for i in range(len(numeros)):
    print("Posición:", i, "Valor:", numeros[i])

# 3. FOR CON RANGE (contador)
# Sirve para repetir algo varias veces

print("\nFOR con range (contador):")
for i in range(5):
    print(i)

# Variaciones de range
print("\nVariaciones de range:")
for i in range(2, 6):  # desde 2 hasta 5
    print(i)

for i in range(0, 10, 2):  # de 2 en 2
    print(i)

# 4. FOR CON ENUMERATE (índice + valor)
# Forma más profesional de obtener índice y valor

numeros = [5, 9, 12]

print("\nFOR con enumerate:")
for i, num in enumerate(numeros):
    print("Posición:", i, "Valor:", num)

# 5. FOR EN FICHEROS (archivos)
# Lee un archivo línea por línea
# NOTA: Asegúrate de tener un archivo llamado "datos.txt"

print("\nFOR en fichero:")
try:
    with open("datos.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())  # .strip() quita saltos de línea
except FileNotFoundError:
    print("No se encontró el archivo 'datos.txt'")

# RESUMEN 
# - FOR directo → recorre elementos
# - FOR con índice → usa posiciones
# - FOR con range → funciona como contador
# - FOR con enumerate → índice + valor
# - FOR en fichero → recorre líneas de archivo



#Participacion: buscar un ejercicio del for para un array, vector, fichero 
# lista (array)
numeros = [10, 20, 30, 40]

print("array:")
for num in numeros:
    print(num)

# vector (con índice)
print("\nvector:")
for i in range(len(numeros)):
    print(i, numeros[i])

# fichero (archivo)
print("\nfichero:")

with open("datos.txt", "r") as archivo:
   for linea in archivo:
      print(linea.strip())


