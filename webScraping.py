# Carga de librerías
import requests
from bs4 import BeautifulSoup

# Carga de la pagina web
page = requests.get("https://www.donostia.eus/Actividad.nsf/frmWeb?ReadForm&idioma=cas")

# Carga del contenido de la pagina web
soup = BeautifulSoup(page.content)

# Busqueda del elemento que contiene la información
data = soup.find(class_= "contenidoTiempo")

# Extracción de la toda información del primer día
day1 = data.find('a', attrs={"href":"/Actividad.nsf/frmWeb?ReadForm&idioma=cas&dia=1"})

# Selección de la información de interes del primer día

day_name = day1.find(class_="fctDayDate").get_text()
day_temp = day1.find(class_="fctHiLow").get_text()
day_cond = day1.find(class_="fctDayConditions").get_text()
day_rain = day1.find(class_="popValue").get_text()
day_text = day1.find(class_="popText").get_text()

# Mostramos por pantalla el resultado de la extracción
print(day_name)
print(day_temp)
print(day_cond)
print(day_rain)
print(day_text)

# Definición de la función de extracción de imagenes
def load_requests(source_url):
    r = requests.get(source_url, stream = True )
    if r.status_code == 200:
        aSplit = source_url.split('/')
        ruta = "C:/Users/Javier/1.-Master/CURSO18-19/1er_cuatri/Tipología y ciclo de vida de los datos/PRAC1/imagenes/"+aSplit[len(aSplit)- 1]
        print (ruta)
        output = open(ruta,"wb")
        for chunk in r:
            output.write(chunk)
        output.close()

# Extracción de la imagen correspondiente al primer día
load_requests("https://www.donostia.eus/taxo/imagenes/chancerain.gif")
