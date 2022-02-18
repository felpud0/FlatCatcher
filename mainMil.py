from bs4 import BeautifulSoup
from regex import regex
import requests

from flat import Flat

r = requests.Session()
URL = "https://www.milanuncios.com/alquiler-de-pisos-en-vistalegre-murcia-murcia/?vendedor=part&orden=relevance&fromSearch=1"
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

page = r.get(URL, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")
#print(soup)
tarjetas = soup.find_all("article",class_="ma-AdCard")

i=0
for t in tarjetas:
    #Obtenemos el link
    url = t.find("a", href=True)['href']
    #Obtenemos el id
    id = t.find("p",class_="ma-AdCard-adId").text
    #Obtenemos el titulo del anuncio
    tit = t.find("h2",class_="ma-AdCard-title-text").text
    #Obtenemos la descripcion.
    desc = t.find("p",class_="ma-AdCardDescription-text").text
    #Obtenemos el precio.
    precio = t.find("span",class_="ma-AdPrice-value ma-AdPrice-value--default ma-AdPrice-value--heading--m").text
    
    piso = Flat(id,url,tit,desc+" "+precio)
    print(piso.pretty())