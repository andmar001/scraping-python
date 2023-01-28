from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://mexico.as.com/resultados/futbol/mexico_clausura/clasificacion/?omnil=mpal'
page = requests.get(url) # crear la solicitud
soup = BeautifulSoup(page.content, 'html.parser')  # parsear el contenido de la página, para identificar los elementos de HTML


#Equipos 
eq = soup.find_all('span', class_='nombre-equipo')   # colocar el nombre de la clase que se quiere extraer, nombre-equipo
# print(eq)  prueba de etiquetas extraidas

#crear una lista vacía para almacenar los nombres de los equipos
equipos = list()
contador = 0
numero_equipos_liga = 18   # valor depende de la liga, en este caso es la liga mexicana tiene 18 equipos

# llenar la lista con los nombres de los equipos
for i in eq:
  if contador < numero_equipos_liga:
      equipos.append(i.text)
      contador += 1
  else:
      break

# print(equipos, len(equipos))  # test para ver lso equipos extraidos en consola

print("-"*50)

# Puntos
pt = soup.find_all('td', class_='destacado')   # colocar el nombre de la clase que se quiere extraer, destacado

#crear una lista vacía para almacenar los puntos de los equipos 
puntos = list()
contador = 0
numero_equipos_liga = 18   # valor depende de la liga, en este caso es la liga mexicana tiene 18 equipos

# llenar la lista con los puntos de los equipos
for i in pt:
  if contador < numero_equipos_liga:
      puntos.append(i.text)
      contador += 1
  else:
      break

# uso de pandas para crear un dataframe
df = pd.DataFrame({'Equipos': equipos, 'Puntos': puntos},  index = list(range(1,19)))

# print(df) test para ver el dataframe en consola

## guardar el dataframe en un archivo excel en la misma carpeta del script
df.to_excel('pts_liga_mx.xlsx', sheet_name='pts_liga_mx', index=False)


