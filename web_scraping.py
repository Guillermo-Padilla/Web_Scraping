import requests
import pandas as pd
from bs4 import BeautifulSoup

url= 'http://127.0.0.1:8000/'
#obtengo la pagina a analizar
html_doc = requests.get(url)
#print(html_doc.text)
#parsear la pagina web
soup = BeautifulSoup(html_doc.text, 'html.parser')

titulo_datos = soup.h1.string
print(titulo_datos)

tabla= soup.find('table')

nombres= []
apellidos= []
emails= []

filas= tabla.find_all('tr')
for fila in filas:
    celdas= fila.find_all('td')
    # datos= [celda.get_text(strip= True) for celda in celdas]
    # print(datos)
    # print(celdas)
    if len(celdas)>0:
        nombres.append(celdas[3].string)
        apellidos.append(celdas[4].string)
        emails.append(celdas[5].string)

print(nombres)
print(apellidos)
print(emails)

df= pd.DataFrame({'Nombre': nombres, 'Apellido': apellidos, 'Email': emails})
df.to_csv('facturas.csv', index=False, encoding='utf-8')




