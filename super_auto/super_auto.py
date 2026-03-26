# ======================================
#  ANÁLISIS DE SUPER AUTO S.A.
#  ESPECIALISTA: LEONARDO ANTON RAMIREZ
# ======================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

df = pd.read_excel('Super_Auto.xlsx', sheet_name='BD')

cat_cols = ['Genero_Propietario', 'Tipo_vehiculo', 'Forma_pago', 'Zona', 'Vendedor',
            'Ubicacion', 'Frecuencia_Pago', 'Nivel_Educativo']
for col in cat_cols:
    df[col] = df[col].astype('category')

# CÁLCULO DE COMISIÓN
def calcular_comision(row):
    if row['Forma_pago'] in ['Contado', 'Credito bancario']:
        return row['Precio_vehiculo_dolares'] * 0.01
    elif row['Forma_pago'] == 'Credito concesionaria':
        return row['Precio_vehiculo_dolares'] * 0.03
    return 0

df['Comision'] = df.apply(calcular_comision, axis=1)


#        ╔═══════════════════════════════════════════════╗
#        ║       LIMPIEZA DE ERRORES TIPOGRÁFICOS        ║
#        ╚═══════════════════════════════════════════════╝


# Limpieza de Tipo_vehiculo
def normalizar_vehiculo(v):
    v = str(v).lower().strip()
    if "suv" in v:
        return "SUV"
    elif "cross" in v:
        return "Crossover"
    elif "hatch" in v:
        return "Hatchback"
    elif "sedan" in v:
        return "Sedan"
    elif "coupe" in v or "cope" in v:
        return "Coupe"
    elif "miniv" in v:
        return "Minivan"
    elif "pick" in v or "up" in v:
        return "Pick-Up"
    else:
        return "Otro"

df["Tipo_vehiculo"] = df["Tipo_vehiculo"].apply(normalizar_vehiculo)

# Limpieza de Forma_pago
def normalizar_forma_pago(v):
    v = str(v).lower().strip()
    if "tado" in v:
        return "Contado"
    elif "banc" in v:
        return "Crédito Bancario"
    elif "conces" in v:
        return "Crédito Concesionaria"
    else:
        return "Otro"

df['Forma_pago'] = df['Forma_pago'].apply(normalizar_forma_pago)

# Limpieza de Género del propietario
def normalizar_genero(v):
    v = str(v).lower().strip()
    if "masc" in v or v.startswith("m"):
        return "Masculino"
    elif "fem" in v or v.startswith("f"):
        return "Femenino"
    else:
        return "Otro"

df['Genero_Propietario'] = df['Genero_Propietario'].apply(normalizar_genero)

# Limpieza de Zona

def normalizar_zona(z):
    z = str(z).lower().strip()
    if "norte" in z:
        return "Lima Norte"
    elif "centro" in z:
        return "Lima Centro"
    elif "zona a" in z or z == "a":
        return "Zona A"
    elif "zona b" in z or z == "b":
        return "Zona B"
    elif "zona c" in z or z == "c":
        return "Zona C"
    elif "zona d" in z or z == "d":
        return "Zona D"
    elif "zona e" in z or z == "e":
        return "Zona E"
    else:
        return "Otro"

df['Zona'] = df['Zona'].apply(normalizar_zona)

# COLUMNA DE MES Y AÑO
df['Fecha_compra'] = pd.to_datetime(df['Fecha_compra'])
df['Mes'] = df['Fecha_compra'].dt.to_period('M')
df['Año'] = df['Fecha_compra'].dt.year


#        ╔═══════════════════════════════════════════════╗
#        ║                Visualizaciones                ║
#        ╚═══════════════════════════════════════════════╝


# Análisis 1: Distribución por Zona, Vendedor y Forma de Pago

# Ventas agrupadas por Zona
ventas_zona = df.groupby('Zona')['Precio_vehiculo_dolares'].agg(['count', 'sum'])

# Ventas agrupadas por Vendedor
ventas_vendedor = df.groupby('Vendedor')['Precio_vehiculo_dolares'].agg(['count', 'sum'])
top_vendedores = ventas_vendedor.sort_values(by='sum', ascending=False).head(10)

# Ventas agrupadas por Forma de Pago
ventas_pago = df.groupby('Forma_pago')['Precio_vehiculo_dolares'].agg(['count', 'sum'])

# Visualización de los tres análisis
fig, axs = plt.subplots(1, 3, figsize=(22, 6))

print('\n')
print("Ventas por Zona:\n", ventas_zona)
print('\n')
sns.barplot(x=ventas_zona.index, y=ventas_zona['sum'], ax=axs[0])
axs[0].set_title('Ventas por Zona')
axs[0].tick_params(axis='x', rotation=45)

print('\n')
print("Top 10 Vendedores por Monto Vendido:\n", top_vendedores)
print('\n')
sns.barplot(x=top_vendedores.index, y=top_vendedores['sum'], ax=axs[1])
axs[1].set_title('Top 10 Vendedores por Monto Vendido')
axs[1].tick_params(axis='x', rotation=45)

print('\n')
print("Ventas por Forma de Pago:\n", ventas_pago)
print('\n')
sns.barplot(x=ventas_pago.index, y=ventas_pago['sum'], ax=axs[2])
axs[2].set_title('Ventas por Forma de Pago')
axs[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
print('\n')
plt.show()
print('\n')

# Análisis 2: Distribución por Genero_Propietario
genero_ventas = df.groupby('Genero_Propietario')['Precio_vehiculo_dolares'].agg(['count', 'sum'])
print('\n')
print("Ventas por género del propietario:\n", genero_ventas)
print('\n')
plt.figure(figsize=(8, 5))
sns.barplot(data=genero_ventas.reset_index(), x='Genero_Propietario', y='sum')
plt.title("Ventas Totales por Género del Propietario")
plt.ylabel("Monto Vendido (USD)")
plt.grid(True)
plt.show()

# Análisis 3: Cruce de forma de pago por género
pago_genero = df.groupby(['Forma_pago', 'Genero_Propietario'])['Precio_vehiculo_dolares'].sum().unstack()
print('\n')
print("Ventas por forma de pago y género:\n", pago_genero)
print('\n')
pago_genero.plot(kind='bar', figsize=(10, 6))
plt.title("Forma de Pago por Género del Propietario")
plt.ylabel("Ventas en USD")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title="Género")
plt.tight_layout()
plt.show()

#Análisis 4: Ventas Mensuales
ventas_mensuales = df.groupby('Mes')['Precio_vehiculo_dolares'].sum()
ventas_mensuales.plot(kind='line', figsize=(10, 5), marker='o')
print('\n')
print("Ventas mensuales:\n", ventas_mensuales)
print('\n')
plt.title('Tendencia de Ventas Mensuales')
plt.ylabel('Monto vendido (USD)')
plt.xlabel('Mes')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Análisis 5: Ventas por Tipo de Vehiculo
ventas_por_vehiculo = df.groupby('Tipo_vehiculo')['Precio_vehiculo_dolares'].sum().sort_values()
df.groupby('Tipo_vehiculo')['Precio_vehiculo_dolares'].sum().sort_values().plot(kind='barh', figsize=(10,5))
print('\n')
print("Ventas por tipo de vehículo:\n", ventas_por_vehiculo)
print('\n')
plt.title('Distribución de Ventas por Tipo de Vehículo')
plt.xlabel('Monto Vendido (USD)')
plt.grid(True)
plt.show()

# Análisis 6: Evolución del número de ventas por mes
ventas_mensuales = df.groupby('Mes')['Precio_vehiculo_dolares'].count()
print('\n')
print("Número de ventas por mes:\n", ventas_mensuales)
print('\n')
ventas_mensuales.plot(kind='line', marker='o', figsize=(10, 5))
plt.title('Evolución del Número de Ventas Mensuales')
plt.ylabel('Cantidad de Ventas')
plt.xlabel('Mes')
plt.grid(True)
plt.show()

# Análisis 7: Evolución del monto vendido por mes
monto_mensual = df.groupby('Mes')['Precio_vehiculo_dolares'].sum()
print('\n')
print("Monto total vendido por mes:\n", monto_mensual)
print('\n')
monto_mensual.plot(kind='line', marker='o', color='green', figsize=(10, 5))
plt.title('Evolución del Monto Vendido Mensual')
plt.ylabel('Monto Vendido (USD)')
plt.xlabel('Mes')
plt.grid(True)
plt.show()

# Análisis 8: Ventas por Nivel Educativo
ventas_nivel = df.groupby('Nivel_Educativo')['Precio_vehiculo_dolares'].sum().sort_values()
print('\n')
print("Ventas por nivel educativo:\n", ventas_nivel)
print('\n')
ventas_nivel.plot(kind='barh', figsize=(10, 5), color='purple')
plt.title('Ventas por Nivel Educativo del Propietario')
plt.xlabel('Monto Vendido (USD)')
plt.grid(True)
plt.show()

# Análisis 9: Ventas por Rango de Edad
bins = [18, 30, 40, 50, 60, 100]
labels = ['18-29', '30-39', '40-49', '50-59', '60+']
df['Rango_Edad'] = pd.cut(df['Edad_Propietario'], bins=bins, labels=labels, right=False)
ventas_rango_edad = df.groupby('Rango_Edad')['Precio_vehiculo_dolares'].sum()
print('\n')
print("Ventas por rango de edad:\n", ventas_rango_edad)
print('\n')
ventas_rango_edad.plot(kind='bar', figsize=(10, 5), color='orange')
plt.title('Ventas por Rango de Edad del Propietario')
plt.ylabel('Monto Vendido (USD)')
plt.xlabel('Rango de Edad')
plt.grid(True)
plt.show()

# Análisis 10: Ranking de vendedores por comisiones ganadas
ranking_comisiones = df.groupby('Vendedor')['Comision'].sum().sort_values(ascending=False).head(10)
print('\n')
print("Top 10 vendedores por monto de comisiones:\n", ranking_comisiones)
print('\n')
ranking_comisiones.plot(kind='bar', figsize=(10, 5), color='teal')
plt.title('Top 10 Vendedores por Comisiones Ganadas')
plt.ylabel('Comisión Total (USD)')
plt.xlabel('Vendedor')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


#        ╔═══════════════════════════════════════════════╗
#        ║  SEGMENTACIÓN DE CLIENTES / ZONAS CON KMEANS  ║
#        ╚═══════════════════════════════════════════════╝


# Selección de variables para cluster
df_cluster = df[['Precio_vehiculo_dolares', 'Comision', 'Zona']].copy()
df_cluster = pd.get_dummies(df_cluster, columns=['Zona'], drop_first=True)

# Escalamiento de datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_cluster)

# Evaluación del número óptimo de clusters con silhouette
sil_scores = []
k_range = range(2, 10)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    sil_scores.append(silhouette_score(X_scaled, labels))

# Gráfico para seleccionar mejor k
plt.plot(k_range, sil_scores, marker='o')
plt.title('Silhouette Score vs Número de Clusters')
plt.xlabel('Número de Clusters')
plt.ylabel('Silhouette Score')
plt.grid(True)
plt.show()

# Aplicar clustering con k=3
kmeans_final = KMeans(n_clusters=3, random_state=42)
df_cluster['Cluster'] = kmeans_final.fit_predict(X_scaled)

# Resumen de clusters
print('\n')
print("Resumen promedio por clúster:")
print('\n')
print(df_cluster.groupby('Cluster').mean())

# Visualización
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_cluster,
    x='Precio_vehiculo_dolares',
    y='Comision',
    hue='Cluster',
    palette='Set2'
)
plt.title("Segmentación de Clientes/Zonas según Precio y Comisión")
plt.xlabel("Precio del Vehículo (USD)")
plt.ylabel("Comisión")
plt.grid(True)
plt.legend(title="Cluster")
plt.show()


# Exportar el DataFrame limpio a un archivo Excel
df.to_excel("Super_Auto_LIMPIO.xlsx", index=False)
print("✅ Archivo exportado exitosamente como 'Super_Auto_Optimizado.xlsx'")
