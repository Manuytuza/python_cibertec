# sistema de monitoreo, depuracion y analisis de inventario multisede
# autor: manuel ytuza cusirramos

# instruccion:
# colocar en la misma carpeta el archivo: inventario_productos.csv

import pandas as pd
import matplotlib.pyplot as plt

# ---------------- VALIDACIONES ----------------
def leer_entero(msg):
    # valido que sea entero positivo
    while True:
        try:
            val = int(input(msg))
            if val >= 0:
                return val
        except:
            pass
        print("error: ingrese entero valido")

def leer_flotante(msg):
    # valido numero decimal
    while True:
        try:
            return float(input(msg))
        except:
            print("error: ingrese numero valido")

def leer_texto(msg):
    # valido texto no vacio
    while True:
        val = input(msg).strip()
        if val != "":
            return val
        print("error: no puede estar vacio")

# ---------------- CARGA ----------------
def cargar_datos():
    # cargo archivo base csv
    try:
        df = pd.read_csv("inventario_productos.csv")
        print("archivo cargado correctamente")
        return df
    except Exception as e:
        print("error al cargar:", e)
        return None

# ---------------- MOSTRAR ----------------
def mostrar_estructura(df, df_limpio):
    # muestro estructura base (priorizo limpio si existe)
    if df is None:
        print("primero cargue datos")
        return

    base = df_limpio if df_limpio is not None else df

    print("\nestructura:")
    print(base.info())
    print("\nprimeros registros:")
    print(base.head())

# ---------------- LIMPIEZA ----------------
def limpiar_datos(df):
    # limpieza completa con validaciones
    if df is None:
        print("no hay datos")
        return None, None

    temp = df.copy()  # evito modificar original

    # normalizo nombres columnas
    temp.columns = temp.columns.str.lower().str.strip()

    # valido columnas obligatorias (clave en calidad de datos)
    columnas = ["stock_actual","precio_unitario","stock_minimo","ventas_ult_30d","sede","estado_producto","fecha_ultimo_ingreso"]
    for col in columnas:
        if col not in temp.columns:
            print("falta columna:", col)
            return None, None

    total = len(temp)

    # elimino duplicados
    temp = temp.drop_duplicates()
    duplicados = total - len(temp)

    # convierto a numerico
    cols = ["stock_actual","precio_unitario","stock_minimo","ventas_ult_30d"]
    for c in cols:
        temp[c] = pd.to_numeric(temp[c], errors="coerce")

    # fechas
    temp["fecha_ultimo_ingreso"] = pd.to_datetime(temp["fecha_ultimo_ingreso"], errors="coerce")

    # textos
    temp["sede"] = temp["sede"].str.upper().str.strip()
    temp["estado_producto"] = temp["estado_producto"].str.upper().str.strip()

    # reglas de negocio (deteccion de errores reales)
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

    # separo limpio vs errores
    df_invalidos = temp[cond]
    df_limpio = temp[~cond]

    print("total:", total)
    print("validos:", len(df_limpio))
    print("invalidos:", len(df_invalidos))
    print("duplicados:", duplicados)

    return df_limpio, df_invalidos

# ---------------- VARIABLES ----------------
def generar_variables(df):
    # genero indicadores clave de negocio
    if df is None:
        print("no hay base limpia")
        return None

    df = df.copy()

    # cobertura dias (nivel stock vs ventas)
    df["cobertura_dias"] = (df["stock_actual"] / df["ventas_ult_30d"]).replace([float("inf")], 0).fillna(0) * 30

    # valor total inventario
    df["valor_inventario"] = df["stock_actual"] * df["precio_unitario"]

    # margen stock (nuevo indicador clave)
    df["margen_stock"] = df["stock_actual"] - df["stock_minimo"]

    # clasificacion abastecimiento
    df["estado_abastecimiento"] = "adecuado"
    df.loc[df["stock_actual"] < df["stock_minimo"], "estado_abastecimiento"] = "critico"
    df.loc[df["cobertura_dias"] < 15, "estado_abastecimiento"] = "reposicion pronta"
    df.loc[df["cobertura_dias"] > 45, "estado_abastecimiento"] = "sobrestock"

    # rotacion ventas
    df["rotacion"] = "media"
    df.loc[df["ventas_ult_30d"] == 0, "rotacion"] = "sin movimiento"
    df.loc[df["ventas_ult_30d"] < 20, "rotacion"] = "baja"
    df.loc[df["ventas_ult_30d"] > 50, "rotacion"] = "alta"

    print("variables generadas")
    return df

# ---------------- FILTROS ----------------
def filtrar_productos(df):
    # filtros dinamicos
    if df is None:
        print("no hay datos")
        return

    f = df.copy()

    categoria = input("categoria: ")
    if categoria:
        f = f[f["categoria"] == categoria]

    sede = input("sede: ")
    if sede:
        f = f[f["sede"] == sede.upper()]

    precio = input("precio minimo: ")
    if precio:
        f = f[f["precio_unitario"] >= float(precio)]

    estado = input("estado abastecimiento: ")
    if estado:
        f = f[f["estado_abastecimiento"] == estado]

    print("resultados:", len(f))
    print(f.head())

# ---------------- INDICADORES ----------------
def indicadores(df):
    # resumen analitico
    if df is None:
        print("no hay datos")
        return

    print("total productos:", len(df))
    print("valor total:", df["valor_inventario"].sum())

    print("\nranking valor por sede:")
    print(df.groupby("sede")["valor_inventario"].sum().sort_values(ascending=False))

    print("\npromedio precio por categoria:")
    print(df.groupby("categoria")["precio_unitario"].mean())

    print("\ntop productos:")
    print(df.sort_values("valor_inventario", ascending=False).head(5))

# ---------------- GRAFICOS ----------------
def graficos(df):
    # graficos mejorados con estilo
    if df is None:
        print("no hay datos")
        return

    plt.style.use("ggplot")

    # grafico 1: estado abastecimiento
    df["estado_abastecimiento"].value_counts().plot(
        kind="bar",
        title="estado de abastecimiento",
        figsize=(8,5),
        color=["red","orange","green","blue"]
    )
    plt.xlabel("estado")
    plt.ylabel("cantidad")
    plt.show()

    # grafico 2: valor por sede
    df.groupby("sede")["valor_inventario"].sum().plot(
        kind="bar",
        title="valor inventario por sede",
        figsize=(8,5),
        color="skyblue"
    )
    plt.ylabel("valor")
    plt.show()

    # grafico 3: relacion stock vs ventas (clave analisis)
    plt.figure(figsize=(8,5))
    plt.scatter(df["stock_actual"], df["ventas_ult_30d"], color="purple")
    plt.title("relacion stock vs ventas")
    plt.xlabel("stock actual")
    plt.ylabel("ventas 30d")
    plt.grid(True)
    plt.show()

# ---------------- EXPORTAR ----------------
def exportar(df, df_invalidos):
    # guardo resultados finales
    if df is None:
        print("no hay datos")
        return

    if df_invalidos is None:
        print("primero limpiar datos")
        return

    df.to_csv("inventario_limpio.csv", index=False)
    df_invalidos.to_csv("inventario_invalidos.csv", index=False)

    print("exportado correcto")

# ---------------- MENU ----------------
def menu():
    # menu dinamico con diccionario (evita muchos if)
    df = None
    df_limpio = None
    df_invalidos = None

    acciones = {
        1: lambda: cargar_datos(),
        2: lambda: mostrar_estructura(df, df_limpio),
        3: lambda: limpiar_datos(df),
        4: lambda: generar_variables(df_limpio),
        5: lambda: filtrar_productos(df_limpio),
        6: lambda: indicadores(df_limpio),
        7: lambda: graficos(df_limpio),
        8: lambda: exportar(df_limpio, df_invalidos)
    }

    while True:
        print("\n1 cargar | 2 ver | 3 limpiar | 4 variables | 5 filtrar | 6 indicadores | 7 graficos | 8 exportar | 0 salir")

        op = input("opcion: ")

        if not op.isdigit():
            print("ingrese numero valido")
            continue

        op = int(op)

        if op == 0:
            print("fin del programa")
            break

        if op in acciones:
            resultado = acciones[op]()

            # actualizo estados del sistema
            if op == 1:
                df = resultado
            elif op == 3:
                df_limpio, df_invalidos = resultado
            elif op == 4:
                df_limpio = resultado
        else:
            print("opcion invalida")

# ---------------- MAIN ----------------
def main():
    # punto de entrada principal
    menu()
    print("\ngracias profesor")
    print("autor: manuel ytuza cusirramos")

if __name__ == "__main__":
    main()