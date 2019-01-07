import requests
import json

dolar = requests.get('https://economia.uol.com.br/cotacoes/cambio')

#lista = json.loads(dolar.text)

print(dolar.text)