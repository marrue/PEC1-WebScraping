# Carga de librerías
import requests
from bs4 import BeautifulSoup
import csv
import os

# Carga de la pagina web
page = requests.get("https://www.donostia.eus/Actividad.nsf/frmWeb?ReadForm&idioma=cas")

# Carga del contenido de la pagina web
soup = BeautifulSoup(page.content)

# Busqueda del elemento que contiene la información
data = soup.find(class_= "contenidoTiempo")

# Directorio donde se encuentra el script
directorio_script = os.path.dirname(__file__)

# Definición de la función de extracción de información
def extract_info(day_href):
    day_info = data.find ('a', attrs={"href":day_href})
    day_name = day_info.find(class_="fctDayDate").get_text()
    day_temp = day_info.find(class_="fctHiLow").get_text()
    day_cond = day_info.find(class_="fctDayConditions").get_text()
    day_rain = day_info.find(class_="popValue").get_text()
    day_text = day_info.find(class_="popText").get_text()
    return(day_name,day_temp,day_cond,day_rain,day_text)

# Definición de la función de extracción de imagenes
def load_requests(source_url, dia, directorio):
    r = requests.get(source_url, stream = True)
    if r.status_code == 200:
        aSplit = source_url.split('/')
        filename = "dia%d.gif"%dia
        ruta = os.path.join(directorio, filename)
        print(ruta)
        output = open(ruta,"wb")
        for chunk in r:
            output.write(chunk)
        output.close()

# Creamos y abrimos el archivo csv donde vamos a almacenar la información
with open('tiempo.csv' , 'w' , newline = '') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ";")
    spamwriter.writerow(["dia","temp_max_min","condicion","porcentaje_lluvia","probabilidad_lluvia", "url_imagen"])
    # Extracción de la información de todos los días
    for i in range(1, 8):
        href = "/Actividad.nsf/frmWeb?ReadForm&idioma=cas&dia=%d"%i
        [day_name,day_temp,day_cond,day_rain,day_text] = extract_info(href)
        day_info = data.find('a', attrs={"href":href})
        load_requests("https:" + day_info.find('img').get('src'), i, directorio_script)
        url_imagen = os.path.join(directorio_script, "dia%d.gif"%i)
        spamwriter.writerow([day_name,day_temp,day_cond,day_rain,day_text,url_imagen])





