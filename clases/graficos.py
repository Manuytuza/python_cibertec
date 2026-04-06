import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# =========================
# 🎨 CONFIGURACIÓN GLOBAL (ESTILO PROFESIONAL)
# =========================
sns.set_style("whitegrid")  # fondo con cuadrícula suave
plt.rcParams.update({
    "font.size": 10,           # tamaño base de letra
    "axes.titlesize": 14,      # tamaño de títulos
    "axes.labelsize": 11       # tamaño de etiquetas
})

# =========================
# 📊 DATAFRAMES (DATOS DE EJEMPLO REALISTA)
# =========================

# Ventas vs costos por mes
df_line = pd.DataFrame({
    "mes": ["ene","feb","mar","abr","may","jun"],
    "ventas": [200, 250, 220, 270, 300, 320],
    "costos": [150, 180, 160, 200, 210, 230]
})

# Ventas por vendedor
df_bar = pd.DataFrame({
    "vendedor": ["Jenny","Ana","Johana"],
    "ventas": [5, 4, 6]
})

# Distribución de productos
df_pie = pd.DataFrame({
    "producto": ["iPhone","Audífonos","Accesorios"],
    "ventas": [50, 30, 20]
})

# Ventas diarias (para análisis estadístico)
df_box = pd.DataFrame({
    "ventas": [100, 120, 130, 150, 160, 200, 220, 90, 80]
})

# Relación marketing vs ventas
df_scatter = pd.DataFrame({
    "marketing": [10, 20, 30, 40, 50],
    "ventas": [100, 180, 260, 300, 400]
})

# Crecimiento semanal
df_sns = pd.DataFrame({
    "semana": [1,2,3,4,5],
    "ventas": [50, 80, 120, 160, 200]
})

# =========================
# 🧠 CREACIÓN DEL DASHBOARD
# =========================
fig, axs = plt.subplots(3, 2, figsize=(16, 14))

# título general del dashboard
fig.suptitle("📊 DASHBOARD DE VENTAS - ANALISIS COMPLETO", fontsize=18, fontweight="bold")

# =========================
# 📈 1. GRÁFICO DE LÍNEAS (VENTAS VS COSTOS)
# =========================
axs[0, 0].plot(
    df_line["mes"], df_line["ventas"],
    marker="o", color="blue", linewidth=2, label="Ventas"
)

axs[0, 0].plot(
    df_line["mes"], df_line["costos"],
    marker="s", linestyle="--", color="red", label="Costos"
)

axs[0, 0].set_title("Ventas vs Costos")
axs[0, 0].set_xlabel("Mes")
axs[0, 0].set_ylabel("Monto")

axs[0, 0].legend()  # leyenda
axs[0, 0].grid(True, linestyle=":")

# anotación en punto importante
axs[0, 0].annotate(
    "Pico de ventas",
    ("may", 300),
    textcoords="offset points",
    xytext=(0,10),
    ha='center',
    color="green"
)

# =========================
# 📊 2. GRÁFICO DE BARRAS
# =========================
axs[0, 1].bar(
    df_bar["vendedor"],
    df_bar["ventas"],
    color=["blue","orange","green"],  # colores personalizados
    edgecolor="black"
)

axs[0, 1].set_title("Ventas por Vendedor")

# mostrar valores encima
for i, v in enumerate(df_bar["ventas"]):
    axs[0, 1].text(i, v + 0.2, str(v), ha="center")

# =========================
# 🥧 3. GRÁFICO DE TORTA
# =========================
axs[1, 0].pie(
    df_pie["ventas"],
    labels=df_pie["producto"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#ff9999","#66b3ff","#99ff99"],  # colores personalizados
    wedgeprops={"edgecolor": "black"}
)

axs[1, 0].set_title("Distribución de Productos")

# =========================
# 📦 4. BOXPLOT (ANÁLISIS)
# =========================
sns.boxplot(
    y=df_box["ventas"],
    ax=axs[1, 1],
    color="lightblue"
)

axs[1, 1].set_title("Distribución de Ventas")

# =========================
# 📍 5. SCATTER + TENDENCIA
# =========================
axs[2, 0].scatter(
    df_scatter["marketing"],
    df_scatter["ventas"],
    color="purple",
    s=100
)

axs[2, 0].set_title("Marketing vs Ventas")
axs[2, 0].set_xlabel("Marketing")
axs[2, 0].set_ylabel("Ventas")

# línea de tendencia (análisis)
sns.regplot(
    data=df_scatter,
    x="marketing",
    y="ventas",
    scatter=False,
    ax=axs[2, 0],
    color="red"
)

# =========================
# 📈 6. SEABORN LINE (PRO)
# =========================
sns.lineplot(
    data=df_sns,
    x="semana",
    y="ventas",
    marker="o",
    ax=axs[2, 1],
    color="black"
)

axs[2, 1].set_title("Crecimiento Semanal")

# =========================
# 🧼 LIMPIEZA VISUAL (PRO)
# =========================
for ax in axs.flat:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# ajustar espacios automáticamente
plt.tight_layout()

# mostrar dashboard
plt.show()

import random
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. SIMULAR LANZAMIENTOS
# =========================
moneda = [ ]

# 50 lanzamientos
lanzamientos = [random.choices(moneda) for _ in range(1,51)]

# crear DataFrame
df = pd.DataFrame({
    "Resultado": lanzamientos
})

print(df)

# =========================
# 2. CONTAR RESULTADOS
# =========================
conteo = df["Resultado"].value_counts()

print("\nConteo:")
print(conteo)

# =========================
# 3. GRÁFICO DE BARRAS
# =========================
conteo.plot(kind="bar", title="Resultados de 50 lanzamientos de moneda")

plt.xlabel("Resultado")
plt.ylabel("Cantidad")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()