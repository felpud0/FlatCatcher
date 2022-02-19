from bs4 import BeautifulSoup
from regex import regex
import requests

from flat import Flat
import sched, time

s = sched.scheduler(time.time, time.sleep)
r = requests.Session()
URL = "https://www.idealista.com/alquiler-viviendas/murcia/norte/vista-alegre/?ordenado-por=fecha-publicacion-desc"
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98',
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1"
            }



ultimaLista = []


def comprobarNuevos(sc):
    print("FETCHING....")
    page = r.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    #Asi buscamos los de inmobiliaria
    soup.find_all("article",class_="item  item_contains_branding item-multimedia-container")
    #Asi los de particulares.
    tarjetas = soup.find_all("article",class_="item item-multimedia-container")
    listaActual = parsearTarjetas(tarjetas)
    listaNuevos = diffListas(ultimaLista,listaActual)
    #ultimaLista = listaActual
    if (len(listaNuevos)==0):
        print("==== NO HAY ELEMENTOS NUEVOS ====")
    else:
        print(*listaNuevos, sep="\n")
    s.enter(60, 1, comprobarNuevos, (sc,))
    pass

def diffListas(l1,l2):
    # print("Comparando:")
    # print(*l1, sep="\n")
    # print(*l2,sep="\n")
    return list(set(l2) - set(l1))

def parsearTarjetas(tarjetas):
    listaPisos = []
    for t in tarjetas:
        link = t.find("a",href=True)['href']
        tit=t.find("a",class_="item-link").text
        desc=t.find("p",class_="ellipsis").text.strip()
        precio= t.find("span",class_="item-price h2-simulated").text

        piso = Flat(link,link,tit,desc,precio)
        listaPisos.append(piso)
        #print(piso.pretty())
        #print("==============================")
    return listaPisos

def main():
    #Se ejecuta cada 60 segundos.
    s.enter(10, 1, comprobarNuevos, (s,))
    s.run()

if __name__ == "__main__":
    main()
