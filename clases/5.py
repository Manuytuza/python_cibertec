#revisar practica resuelta de examen final 
#PANDAS Y EXCEL

#QUE ES UN RPA
###proxima clase lean el codigo python de superauto data frein revisar########

#data frein as df revisar al detalle, tabla de excel o sql #######

#import pandas as pd
#.head(primeras lineas) .info(columnas,filas,tipos de datos)  .describe(promedio desviacion percentil)

#que es un scrip
#pregunta 5 REVISAR EJERCIOS D EEXAMEN MENOS LA DE LIBRERIA NO USADA RADIAN...
def calcular_impuesto(ingreso_anual):
    UIT = 4400
    # Paso 1: restar 7 UIT
    renta_neta = ingreso_anual - (7 * UIT)
    print(renta_neta)
    if renta_neta <= 0:
        return 0
    impuesto = 0  # aquí se irá acumulando todo lo que se paga
    # TRAMO 1: hasta 5 UIT
    if renta_neta > 0:
        # min evita que tomes más de lo que permite el tramo
        # si renta_neta es menor que 5 UIT → usa renta_neta
        # si es mayor → solo usa 5 UIT
        tramo = min(renta_neta, 5 * UIT)
        # se suma al impuesto total
        impuesto += tramo * 0.08  # 8%
    # TRAMO 2: de 5 UIT a 20 UIT
    if renta_neta > 5 * UIT:
        # restamos lo ya usado en el tramo anterior
        # y usamos min para no pasar el límite del tramo (15 UIT)
        tramo = min(renta_neta - 5 * UIT, 15 * UIT)
        # se acumula (se suma al anterior)
        impuesto += tramo * 0.14  # 14%
    # TRAMO 3
    if renta_neta > 20 * UIT:
        tramo = min(renta_neta - 20 * UIT, 15 * UIT)
        impuesto += tramo * 0.17
    # TRAMO 4
    if renta_neta > 35 * UIT:
        tramo = min(renta_neta - 35 * UIT, 10 * UIT)
        impuesto += tramo * 0.20
    # TRAMO 5
    if renta_neta > 45 * UIT:
        tramo = renta_neta - 45 * UIT  # aquí ya no hay límite
        impuesto += tramo * 0.30
    return impuesto

# 1. Pedir dato al usuario
ingreso = 3000*12#float(input("Ingrese su ingreso anual: "))

# 2. Llamar a la función (aquí se ejecuta todo el cálculo)
resultado = calcular_impuesto(ingreso)

# 3. Mostrar el resultado que devolvió el return
print("El impuesto a pagar es:", resultado)

###que es CALL TO ACTION
###correr superauto como participacion 
##linkiar en ves de usar terminal 
###prompt guia
###cambiar ruta de superauto
###enrutar
### martes 7 examen final 

def calcular_impuesto(ingreso_anual):
    UIT = 4400
    
    # Paso 1: calcular renta neta
    renta_neta = ingreso_anual - (7 * UIT)

    # Si no paga impuesto
    if renta_neta <= 0:
        return 0

    impuesto = 0

    # Tramos: (límite, tasa)
    tramos = [
        (5 * UIT, 0.08),
        (15 * UIT, 0.14),
        (15 * UIT, 0.17),
        (10 * UIT, 0.20),
        (float("inf"), 0.30)
    ]

    acumulado = 0

    # Cálculo del impuesto
    for limite, tasa in tramos:
        if renta_neta > acumulado:
            tramo = min(renta_neta - acumulado, limite)
            impuesto += tramo * tasa
            print(f"impuesto de tramo, {impuesto} y acumulado {acumulado}")
            acumulado += limite 
        else:
            break

    return impuesto


# =========================
# PROGRAMA PRINCIPAL
# =========================

# Pedir ingreso al usuario
ingreso = float(input("Ingrese su ingreso anual: "))

# Calcular impuesto
resultado = calcular_impuesto(ingreso)

# Mostrar resultado
print(f"El impuesto a pagar es: S/ {resultado:.2f}")
