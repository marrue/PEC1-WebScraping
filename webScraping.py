# Carga de librerías
import requests
from bs4 import BeautifulSoup

# Carga de la pagina web
page = requests.get("https://www.donostia.eus/Actividad.nsf/frmWeb?ReadForm&idioma=cas")

# Carga del contenido de la pagina web
soup = BeautifulSoup(page.content)

# Busqueda del elemento que contiene la información
data = soup.find(class_= "contenidoTiempo")

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
def load_requests(source_url):
    r = requests.get(source_url, stream = True)
    if r.status_code == 200:
        aSplit = source_url.split('/')
        ruta = "C:/Users/Javier/1.-Master/CURSO18-19/1er_cuatri/Tipología y ciclo de vida de los datos/PRAC1/imagenes/"+aSplit[len(aSplit)- 1]
        print (ruta)
        output = open(ruta,"wb")
        for chunk in r:
            output.write(chunk)
        output.close()

# Extradcción de la información del primer dia
href = "/Actividad.nsf/frmWeb?ReadForm&idioma=cas&dia=1"
[day_name,day_temp,day_cond,day_rain,day_text] = extract_info(href)

# Mostramos por pantalla la información extraída
print(day_name)
print(day_temp)
print(day_cond)
print(day_rain)
print(day_text)

# Extracción de la imagen correspondiente al primer día
load_requests("https://www.donostia.eus/taxo/imagenes/chancerain.gif")
