from bs4 import BeautifulSoup
from regex import regex
import requests

r = requests.Session()
URL = "https://www.departiculares.com/alquiler/murcia/huerta-de-murcia/murcia"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

page = r.get(URL, headers=headers)

soup = BeautifulSoup(page.text, "html.parser")
tarjetas = soup.find_all("li",class_="list-result-item app-marker app-links")

i=0
for t in tarjetas:
    print(t.text)
    i=i+1
    print(i)
