from datetime import datetime, timedelta
import os
import time
import io
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# ----------------------------------------------------------
# CONFIGURACIÓN
# ----------------------------------------------------------
# esto deberia estar en el archivo .env y llevarlo a un .bat#
#que el bot duerme o cambiar bpn y iterarlo 10 veces 
URL_SBS = "https://www.sbs.gob.pe/app/pp/EstadisticasSAEEPortal/Paginas/TIActivaTipoCreditoEmpresa.aspx?tip=B"

ID_FECHA     = "ctl00_cphContent_rdpDate_dateInput"
ID_CONSULTAR = "ctl00_cphContent_btnConsultar"

ID_TABLA_MN = "ctl00_cphContent_rpgActualMn_ctl00_DataZone_DT"
ID_TABLA_ME = "ctl00_cphContent_rpgActualMex_ctl00_DataZone_DT"

XPATH_PESTANA_MN = "//a[normalize-space()='Moneda Nacional']"
XPATH_PESTANA_ME = "//a[normalize-space()='Moneda Extranjera']"


# ----------------------------------------------------------
# 1. Fecha de ayer + nombre del archivo
# ----------------------------------------------------------

def crear_fecha_y_nombre(base_dir="Data"):
    ayer = datetime.now() - timedelta(days=1)
    fecha_str = ayer.strftime("%d/%m/%Y")      # para escribir en la web
    fecha_archivo = ayer.strftime("%d_%m_%Y")  # para el nombre del Excel

    if not os.path.isdir(base_dir):
        os.makedirs(base_dir, exist_ok=True)

    ruta_excel = os.path.join(base_dir, f"Reporte_Tasa6_{fecha_archivo}.xlsx")
    return fecha_str, ruta_excel


# ----------------------------------------------------------
# 2. Iniciar Chrome
# ----------------------------------------------------------

def iniciar_driver():
    options = webdriver.ChromeOptions()
    # Si no quieres ver el navegador, descomenta:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()
    return driver


# ----------------------------------------------------------
# 3. Poner fecha y pulsar CONSULTAR
# ----------------------------------------------------------

def escribir_fecha_y_consultar(driver, fecha_str):
    driver.get(URL_SBS)
    wait = WebDriverWait(driver, 20)

    # Campo fecha
    campo_fecha = wait.until(
        EC.element_to_be_clickable((By.ID, ID_FECHA))
    )
    campo_fecha.clear()
    campo_fecha.send_keys(fecha_str)
    campo_fecha.send_keys(Keys.TAB)

    # Botón CONSULTAR
    boton = wait.until(
        EC.element_to_be_clickable((By.ID, ID_CONSULTAR))
    )
    boton.click()

    # Espera a que recarguen los datos
    time.sleep(7)


# ----------------------------------------------------------
# 4. Extraer una tabla por id → DataFrame
# ----------------------------------------------------------

def extraer_tabla_por_id(driver, table_id, timeout=20):
    wait = WebDriverWait(driver, timeout)

    tabla_elem = wait.until(
        EC.presence_of_element_located((By.ID, table_id))
    )

    html_tabla = tabla_elem.get_attribute("outerHTML")
    print("HTML obtenido OK")
    #soup = BeautifulSoup(html_tabla, "lxml")
    soup = BeautifulSoup(html_tabla, "html.parser")
    #df = pd.read_html(str(soup))[0]


    df = pd.read_html(io.StringIO(str(soup)))[0]
    return df


# ----------------------------------------------------------
# 5. Exportar MN y ME al Excel final
# ----------------------------------------------------------

def exportar_mn_me_a_excel(driver, ruta_excel, timeout=20):
    wait = WebDriverWait(driver, timeout)

    # --- Moneda Nacional ---
    pestana_mn = wait.until(
        EC.element_to_be_clickable((By.XPATH, XPATH_PESTANA_MN))
    )
    pestana_mn.click()
    time.sleep(1)
    df_mn = extraer_tabla_por_id(driver, ID_TABLA_MN, timeout=timeout)

    # --- Moneda Extranjera ---
    pestana_me = wait.until(
        EC.element_to_be_clickable((By.XPATH, XPATH_PESTANA_ME))
    )
    pestana_me.click()
    time.sleep(1)
    df_me = extraer_tabla_por_id(driver, ID_TABLA_ME, timeout=timeout)

    # --- Guardar en Excel ---
    with pd.ExcelWriter(ruta_excel, engine="openpyxl") as writer:
        df_mn.to_excel(writer, sheet_name="MN", index=False)
        df_me.to_excel(writer, sheet_name="ME", index=False)

    print(f"✅ Archivo Excel generado: {ruta_excel}")


# ----------------------------------------------------------
# MAIN
# ----------------------------------------------------------

def main(base_dir="Data"):
    fecha_str, ruta_excel = crear_fecha_y_nombre(base_dir)
    print("Fecha usada (ayer):", fecha_str)
    print("Archivo destino:", ruta_excel)

    driver = iniciar_driver()
    try:
        escribir_fecha_y_consultar(driver, fecha_str)
        exportar_mn_me_a_excel(driver, ruta_excel)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
