# =========================================
# EXAMEN FINAL PYTHON - TODO EN UNO
# Autor: Sr Manuel
# =========================================

# =========================
# IMPORTACIÓN DE LIBRERÍAS
# =========================
import pandas as pd  # manejo de datos tipo Excel
import matplotlib.pyplot as plt  # gráficos
import seaborn as sns  # estilos de gráficos

# =========================
# CAPÍTULO 1: VARIABLES
# =========================
empresa = "TechStore"
anio = 2026

# =========================
# CAPÍTULO 3: LISTAS / DICCIONARIOS / SET / TUPLAS
# =========================
ventas = [
    {"producto": "iPhone", "ventas": 10, "precio": 4000},
    {"producto": "iPad", "ventas": 5, "precio": 2500},
    {"producto": "MacBook", "ventas": 8, "precio": 6000},
    {"producto": "Audifonos", "ventas": 15, "precio": 300},
]

productos_unicos = set()  # elimina duplicados
tupla_ejemplo = ("dato1", "dato2")  # inmutable

# =========================
# CAPÍTULO 2: FUNCIONES
# =========================

# validar datos
def validar_datos(lista):
    for item in lista:
        if not isinstance(item["ventas"], int):
            return False
        if not isinstance(item["precio"], (int, float)):
            return False
    return True

# calcular ingresos totales
def calcular_ingresos(lista):
    total = 0
    for item in lista:
        total += item["ventas"] * item["precio"]
    return total

# clasificar productos
def clasificar_producto(ventas):
    if ventas >= 10:
        return "ALTA"
    elif ventas >= 5:
        return "MEDIA"
    else:
        return "BAJA"

# =========================
# CAPÍTULO BONUS: IMPUESTO
# =========================
def calcular_impuesto(ingreso_anual):
    UIT = 4400
    renta_neta = ingreso_anual - (7 * UIT)

    if renta_neta <= 0:
        return 0

    impuesto = 0
    tramos = [
        (5 * UIT, 0.08),
        (15 * UIT, 0.14),
        (15 * UIT, 0.17),
        (10 * UIT, 0.20),
        (float("inf"), 0.30)
    ]

    restante = renta_neta

    for limite, tasa in tramos:
        if restante <= 0:
            break

        monto = min(restante, limite)
        impuesto += monto * tasa
        restante -= monto

    return impuesto

# =========================
# CAPÍTULO 4: MANEJO DE ERRORES
# =========================
try:

    # validar datos
    if not validar_datos(ventas):
        raise ValueError("Datos incorrectos")

    # =========================
    # CAPÍTULO 6: PANDAS
    # =========================

    df = pd.DataFrame(ventas)  # crear DataFrame

    # nuevas columnas
    df["ingresos"] = df["ventas"] * df["precio"]
    df["clasificacion"] = df["ventas"].apply(clasificar_producto)

    # info general (EDA)
    print("=== HEAD ===")
    print(df.head())

    print("\n=== INFO ===")
    print(df.info())

    print("\n=== DESCRIBE ===")
    print(df.describe())

    # =========================
    # BUCLE WHILE + SET
    # =========================
    i = 0
    while i < len(df):
        productos_unicos.add(df["producto"][i])
        i += 1

    # =========================
    # FILTROS
    # =========================
    filtro = df[df["ventas"] > 6]

    # =========================
    # AGRUPACIÓN
    # =========================
    resumen = df.groupby("producto")["ventas"].sum()

    # =========================
    # ARCHIVOS
    # =========================
    with open("reporte.txt", "w", encoding="utf-8") as archivo:
        archivo.write(f"Empresa: {empresa}\n")
        archivo.write(f"Año: {anio}\n")
        archivo.write("Productos únicos:\n")

        for p in productos_unicos:
            archivo.write(p + "\n")

    # =========================
    # CAPÍTULO 7: GRÁFICOS
    # =========================
    sns.set_style("whitegrid")

    plt.figure(figsize=(10, 5))
    plt.plot(df["producto"], df["ingresos"], marker="o", label="Ingresos")

    plt.title("Ingresos por Producto")
    plt.xlabel("Producto")
    plt.ylabel("Ingresos")
    plt.legend()

    #plt.show()

    # =========================
    # OUTPUT FINAL
    # =========================
    print("\n=== DATAFRAME COMPLETO ===")
    print(df)

    print("\n=== TOTAL INGRESOS ===")
    print(calcular_ingresos(ventas))

    print("\n=== FILTRO (>6 ventas) ===")
    print(filtro)

    print("\n=== RESUMEN ===")
    print(resumen)

    # =========================
    # IMPUESTO
    # =========================
    ingreso = 3000 * 12
    impuesto = calcular_impuesto(ingreso)

    print("\n=== IMPUESTO ===")
    print(f"Ingreso anual: {ingreso}")
    print(f"Impuesto a pagar: {impuesto:.2f}")

# =========================
# MANEJO DE ERRORES
# =========================
