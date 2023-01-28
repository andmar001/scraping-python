from bs4 import BeautifulSoup
import requests
import pandas

url = 'https://www.marca.com/claro-mx/futbol/liga-mx/clausura/goleadores.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Goleadores
go = soup.find_all('span', class_='ue-table-ranking__name')

goleadores = list()
contador = 0
numero_goleadores_liga = 10  # just to visualize the first 10 goleadores

for i in go:
  if contador < numero_goleadores_liga:
      goleadores.append(i.text)
      contador += 1
  else:
      break

#Goles
goles = soup.find_all('td', class_='ue-table-ranking__td')

lista_goles = list()
contador = 0
numero_equipos_liga = 20  # just to visualize the first 10 equipos

for i in goles:
  if contador < numero_equipos_liga:
      lista_goles.append(i.text)
      contador += 1
  else:
      break

# omitir si es un numero posicion 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
lista_goles = lista_goles[1::2]

df = pandas.DataFrame({'Goleador': goleadores, 'Goles': lista_goles},index=list(range(1,11)))

# csv 
df.to_csv('goleadores_liga_mx.csv', index=False, encoding='utf-8')

# excel
df.to_excel('goleadores_liga_mx.xlsx', index=False, encoding='utf-8')

# json
df.to_json('goleadores_liga_mx.json', orient='records')