#inicio 31 ultima clase python 
#se recomeinda poner ruta del archivo en futuros proyectos 
#deepsea es bueno para codigo
#IA https://bolt.new/
#https://antigravity.google/

#GRAFICO DE LINEAS, GENERAR ESQUEMA 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

df = pd.DataFrame(
    {
        "mes": ["ene","feb", "mar","abr","may", "jun"],
        "ventas": [100, 150, 120, 130, 170, 160],
        "unidades": [5,6,7,8,9,9]
    }
)
print(df)   

plt.plot(df["mes"], df["ventas"], label="ventas")
plt.plot(df["mes"], df["unidades"], label="unidades")
plt.title("mi primer plt")
plt.xlabel("nombre ejex")
plt.ylabel("nombre ejey")
plt.legend()
plt.show()
"""
#seaborn es una libreria de graficos que se basa en matplotlib pero con mejores estilos y mas facil de usar
sns.set_style("whitegrid") #estilo de fondo colorado
plt.figure(figsize=(10,6)) #tamaño del grafico 10 ancho y 6 alto
plt.plot(
    df["mes"], #eje x
    df["ventas"], #eje y
    color="blue", #color de la linea
    linewidth=3, #grosor de la linea
    linestyle="--", #linea solida
    marker="o", #marcador en cada punto circulo
    markersize=8, #tamaño del marcador
    markerfacecolor="yellow", #color del marcador
    markeredgecolor="black", #color del borde del marcador
    label="Ventas Mensuales" #etiqueta para la leyenda
)

#agrear titulo y nombre a los ejes
plt.title("Evolucion de Ventas Mensuales", fontsize=16, fontweight="bold") #titulo del grafico
plt.xlabel("Mes del Año", fontsize=12) #nombre del eje x
plt.ylabel("Ventas en soles", fontsize=12) #nombre del eje y

plt.grid(True, linestyle=":", alpha=0.7) #agregar cuadrícula 

plt.legend() #mostrar leyenda

#texto en el grafico diciendo que si sube en el punto pone un titulo 
#text(x, y, "texto", fontsize=10, color="red") #agregar texto en el grafico

plt.text("may", 170, "subida fuerte", fontsize=10, color="green", ha="center") #agregar texto en el grafico 

plt.gca().spines["top"].set_visible(False) #ocultar borde superior
plt.gca().spines["right"].set_visible(False) #ocultar borde derecho
plt.gca().spines["left"].set_visible(False) #ocultar borde izquierdo
plt.gca().spines["bottom"].set_visible(False) #ocultar borde inferior


plt.show() #mostrar el grafico

"""