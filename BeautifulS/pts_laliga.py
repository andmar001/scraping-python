from bs4 import BeautifulSoup
import requests
import pandas

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos
eq = soup.find_all('span', class_='nombre-equipo')

equipos = list()
contador = 0
numero_equipos_liga = 20

for i in eq:
  if contador < numero_equipos_liga:
      equipos.append(i.text)
      contador += 1
  else:
      break
  
print("-"*50,"Documentos creados")

#Puntos

pt = soup.find_all('td', class_='destacado')

puntos = list()
contador = 0
numero_equipos_liga = 20

for i in pt:
    if contador < numero_equipos_liga:
        puntos.append(i.text)
        contador += 1
    else:
        break

df = pandas.DataFrame({'Equipo': equipos, 'Puntos': puntos}, index=list(range(1,21)))

# save in csv
df.to_csv('pts_laliga.csv', index=False, encoding='utf-8')

# save in excel
df.to_excel('pts_laliga.xlsx', index=False)

# save in json
df.to_json('pts_laliga.json', orient='records')
