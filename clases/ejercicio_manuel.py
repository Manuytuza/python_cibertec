import pandas as pd  # SEXTA CLASE: uso de librería pandas

# =========================
# VARIABLES Y COLECCIONES
# =========================

empresa = "TechStore"  # PRIMERA CLASE: variables (string)
anio = 2026  # PRIMERA CLASE: variables (int)

# LISTA de diccionarios (estructura tipo base de datos)
ventas = [  # PRIMERA CLASE: listas
    {"producto": "iPhone", "ventas": 10, "precio": 4000},  # PRIMERA CLASE: diccionario
    {"producto": "iPad", "ventas": 5, "precio": 2500},  # PRIMERA CLASE
    {"producto": "MacBook", "ventas": 8, "precio": 6000},  # PRIMERA CLASE
    {"producto": "Audifonos", "ventas": 15, "precio": 300},  # PRIMERA CLASE
]

productos_unicos = set()  # TERCERA CLASE: set (sin duplicados)
tupla_ejemplo = ("dato1", "dato2")  # TERCERA CLASE: tupla

# =========================
# FUNCIONES
# =========================

def validar_datos(lista):  # SEGUNDA CLASE: funciones
    for item in lista:  # TERCERA CLASE: bucle for
        if not isinstance(item["ventas"], int):  # SEGUNDA CLASE: condicional if
            return False  # SEGUNDA CLASE: return
        if not isinstance(item["precio"], (int, float)):  # SEGUNDA CLASE: validación
            return False
    return True  # SEGUNDA CLASE: return


def calcular_ingresos(lista):  # SEGUNDA CLASE: funciones
    total = 0  # PRIMERA CLASE: variable
    for item in lista:  # TERCERA CLASE: bucle for
        total += item["ventas"] * item["precio"]  # PRIMERA CLASE: operadores
    return total  # SEGUNDA CLASE: return


def clasificar_producto(ventas):  # SEGUNDA CLASE: funciones
    if ventas >= 10:  # SEGUNDA CLASE: if
        return "ALTA"  # SEGUNDA CLASE
    elif ventas >= 5:  # SEGUNDA CLASE: elif
        return "MEDIA"
    else:  # SEGUNDA CLASE: else
        return "BAJA"


# =========================
# MANEJO DE ERRORES
# =========================

try:  # CUARTA CLASE: try/except

    if not validar_datos(ventas):  # SEGUNDA CLASE: condicional + función
        raise ValueError("Datos incorrectos")  # CUARTA CLASE: raise (errores)

    # =========================
    # PANDAS (DATAFRAME)
    # =========================

    df = pd.DataFrame(ventas)  # SEXTA CLASE: DataFrame

    df["ingresos"] = df["ventas"] * df["precio"]  # SEXTA CLASE: operaciones en columnas
    df["clasificacion"] = df["ventas"].apply(clasificar_producto)  # SEXTA CLASE: apply

    # =========================
    # BUCLE WHILE
    # =========================

    i = 0  # PRIMERA CLASE: variable
    while i < len(df):  # TERCERA CLASE: while
        productos_unicos.add(df["producto"][i])  # TERCERA CLASE: set
        i += 1  # PRIMERA CLASE: incremento

    # =========================
    # CONDICIONALES + FILTROS
    # =========================

    filtro = df[df["ventas"] > 6]  # SEXTA CLASE: filtros en pandas

    # =========================
    # AGRUPACIÓN
    # =========================

    resumen = df.groupby("producto")["ventas"].sum()  # SEXTA CLASE: groupby + sum

    # =========================
    # ARCHIVOS (ESCRITURA)
    # =========================

    with open("reporte.txt", "w", encoding="utf-8") as archivo:  # CUARTA CLASE: archivos
        archivo.write(f"Empresa: {empresa}\n")  # PRIMERA CLASE: strings
        archivo.write(f"Año: {anio}\n")  # PRIMERA CLASE
        archivo.write("Productos únicos:\n")  # PRIMERA CLASE
        
        for p in productos_unicos:  # TERCERA CLASE: for
            archivo.write(p + "\n")  # CUARTA CLASE: escritura archivo

    # =========================
    # OUTPUT
    # =========================

    print("=== DATA ===")  # PRIMERA CLASE: print
    print(df)  # SEXTA CLASE: mostrar DataFrame

    print("\n=== TOTAL INGRESOS ===")  # PRIMERA CLASE
    print(calcular_ingresos(ventas))  # SEGUNDA CLASE: función

    print("\n=== FILTRO (>6 ventas) ===")  # PRIMERA CLASE
    print(filtro)  # SEXTA CLASE

    print("\n=== RESUMEN ===")  # PRIMERA CLASE
    print(resumen)  # SEXTA CLASE

except Exception as e:  # CUARTA CLASE: except
    print("Error:", e)  # PRIMERA CLASE: print

finally:  # CUARTA CLASE: finally
    print("Proceso finalizado")  # PRIMERA CLASE
    