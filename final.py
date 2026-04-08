# Manuel Ytuza Cusirramos examen final
# sistema de monitoreo, depuracion y analisis de inventario multisede

import pandas as pd
import matplotlib.pyplot as plt

# ---------------- VALIDACIONES ----------------
def leer_entero(msg):
    while True:
        try:
            val = int(input(msg))
            if val >= 0:
                return val
        except:
            pass
        print("error: ingrese entero valido")

def leer_flotante(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("error: ingrese numero valido")

def leer_texto(msg):
    while True:
        val = input(msg).strip()
        if val != "":
            return val
        print("error: no puede estar vacio")

# ---------------- CARGA ----------------
def cargar_datos():
    try:
        df = pd.read_csv("inventario_productos.csv")
        print("archivo cargado correctamente")
        return df
    except FileNotFoundError:
        print("archivo no encontrado")
    except pd.errors.EmptyDataError:
        print("archivo vacio")
    except pd.errors.ParserError:
        print("error en formato o separador")
    except Exception as e:
        print("error:", e)
    return None

# ---------------- MOSTRAR ESTRUCTURA ----------------
def mostrar_estructura(df):
    if df is None:
        print("primero cargue el archivo")
        return
    print(df.info())
    print(df.head())

# ---------------- LIMPIEZA ----------------
def limpiar_datos(df):
    if df is None:
        print("no hay datos")
        return None, None

    temp = df.copy()

    # normalizar columnas
    temp.columns = temp.columns.str.lower().str.strip()

    total_original = len(temp)

    # eliminar duplicados
    temp = temp.drop_duplicates()
    duplicados = total_original - len(temp)

    # conversion de tipos
    cols_num = ["stock_actual","precio_unitario","stock_minimo","ventas_ult_30d"]
    for c in cols_num:
        temp[c] = pd.to_numeric(temp[c], errors="coerce")

    # fechas
    temp["fecha_ultimo_ingreso"] = pd.to_datetime(temp["fecha_ultimo_ingreso"], errors="coerce")

    # estandarizar texto
    temp["sede"] = temp["sede"].str.upper().str.strip()
    temp["estado_producto"] = temp["estado_producto"].str.upper().str.strip()

    # reglas de negocio
    cond = (
        (temp["stock_actual"] < 0) |
        (temp["precio_unitario"] <= 0) |
        (temp["stock_minimo"] < 0) |
        (temp["ventas_ult_30d"] < 0) |
        (temp["stock_minimo"] > 500) |
        (temp["stock_actual"] > 10000) |
        (temp["fecha_ultimo_ingreso"].isna()) |
        (~temp["estado_producto"].isin(["ACTIVO","INACTIVO"])) |
        ((temp["stock_actual"] < temp["stock_minimo"]) & (temp["estado_producto"]=="INACTIVO"))
    )

    df_invalidos = temp[cond]
    df_limpio = temp[~cond]

    print("total registros:", total_original)
    print("validos:", len(df_limpio))
    print("invalidos:", len(df_invalidos))
    print("duplicados eliminados:", duplicados)

    return df_limpio, df_invalidos

# ---------------- VARIABLES ----------------
def generar_variables(df_limpio):
    if df_limpio is None:
        print("no hay base limpia")
        return None

    # cobertura
    df_limpio["cobertura_dias"] = df_limpio.apply(
        lambda x: (x["stock_actual"]/x["ventas_ult_30d"])*30 if x["ventas_ult_30d"] > 0 else 0,
        axis=1
    )

    # valor inventario
    df_limpio["valor_inventario"] = df_limpio["stock_actual"] * df_limpio["precio_unitario"]

    # estado abastecimiento
    def clasificar(row):
        if row["stock_actual"] < row["stock_minimo"]:
            return "critico"
        elif row["cobertura_dias"] < 15:
            return "reposicion pronta"
        elif row["cobertura_dias"] <= 45:
            return "adecuado"
        else:
            return "sobrestock"

    df_limpio["estado_abastecimiento"] = df_limpio.apply(clasificar, axis=1)

    # rotacion
    def rotacion(v):
        if v == 0:
            return "sin movimiento"
        elif v < 20:
            return "baja"
        elif v < 50:
            return "media"
        else:
            return "alta"

    df_limpio["rotacion"] = df_limpio["ventas_ult_30d"].apply(rotacion)

    print("variables generadas correctamente")
    return df_limpio

# ---------------- FILTROS ----------------
def filtrar_productos(df_limpio):
    if df_limpio is None:
        print("no hay base limpia")
        return

    f = df_limpio.copy()

    categoria = input("categoria (enter para omitir): ")
    if categoria:
        f = f[f["categoria"] == categoria]

    sede = input("sede (enter para omitir): ")
    if sede:
        f = f[f["sede"] == sede.upper()]

    precio_min = input("precio minimo: ")
    if precio_min:
        f = f[f["precio_unitario"] >= float(precio_min)]

    print("resultados encontrados:", len(f))
    print(f.head())

# ---------------- INDICADORES ----------------
def indicadores(df_limpio):
    if df_limpio is None:
        print("no hay datos")
        return

    print("total productos:", len(df_limpio))
    print("valor total inventario:", df_limpio["valor_inventario"].sum())
    print("productos por sede:")
    print(df_limpio["sede"].value_counts())
    print("promedio precio por categoria:")
    print(df_limpio.groupby("categoria")["precio_unitario"].mean())

    print("top 5 valor inventario:")
    print(df_limpio.sort_values("valor_inventario", ascending=False).head(5))

# ---------------- GRAFICOS ----------------
def graficos(df_limpio):
    if df_limpio is None:
        print("no hay datos")
        return

    df_limpio["estado_abastecimiento"].value_counts().plot(kind="bar", title="estado abastecimiento")
    plt.show()

    df_limpio.groupby("sede")["valor_inventario"].sum().plot(kind="bar", title="valor inventario por sede")
    plt.show()

    df_limpio["precio_unitario"].plot(kind="hist", title="distribucion precios")
    plt.show()

    plt.scatter(df_limpio["stock_actual"], df_limpio["ventas_ult_30d"])
    plt.title("stock vs ventas")
    plt.show()

# ---------------- EXPORTAR ----------------
def exportar(df_limpio, df_invalidos):
    if df_limpio is None:
        print("no hay datos")
        return

    try:
        df_limpio.to_csv("inventario_limpio.csv", index=False)
        df_invalidos.to_csv("inventario_invalidos.csv", index=False)
        print("archivos exportados correctamente")
    except:
        print("error al exportar")

# ---------------- MENU ----------------
def menu():
    df = None
    df_limpio = None
    df_invalidos = None

    while True:
        print("\n1 cargar archivo")
        print("2 mostrar estructura")
        print("3 limpiar datos")
        print("4 generar variables")
        print("5 filtrar productos")
        print("6 indicadores")
        print("7 graficos")
        print("8 exportar")
        print("9 salir")

        op = input("opcion: ")

        if not op.isdigit():
            print("ingrese numero valido")
            continue

        op = int(op)

        # diccionario de acciones
        acciones = {
            1: lambda: cargar_datos(),
            2: lambda: mostrar_estructura(df),
            3: lambda: limpiar_datos(df),
            4: lambda: generar_variables(df_limpio),
            5: lambda: filtrar_productos(df_limpio),
            6: lambda: indicadores(df_limpio),
            7: lambda: graficos(df_limpio),
            8: lambda: exportar(df_limpio, df_invalidos)
        }

        if op == 9:
            print("fin del programa")
            break

        if op in acciones:
            resultado = acciones[op]()

            # actualizar variables cuando corresponde
            if op == 1:
                df = resultado
            elif op == 3:
                df_limpio, df_invalidos = resultado
            elif op == 4:
                df_limpio = resultado

        else:
            print("opcion fuera de rango")
# ---------------- MAIN ----------------
def main():
    menu()

if __name__ == "__main__":
    main()