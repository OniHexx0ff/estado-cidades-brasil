import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.ibge.gov.br/explica/codigos-dos-municipios.php'

response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tables = soup.findAll('table', {'class': 'container-uf'})
 
    list = {}

    if len(tables) > 0:
        for table in tables:
 
            estado = table.find('thead')
            estado = estado.find('th').text
            if estado != "Distrito Federal":
               estado =  estado[14:]         
            if not estado:
                continue
            list[estado] = []

            rows = table.find_all('tr')

            for row in rows[1:]:
                td = row.find('td')
                city = td.find('a').text
                list[estado].append(city)


jsonList = json.dumps(list, ensure_ascii=False,  indent=4)


with open('municipios.json', 'w', encoding="utf-8") as f:
    f.write(jsonList)
     