import requests
import json

cabecalho = {'User-agent':'Windows17', 'Referer':'https://giba.com.br'}
texto = None
try:
    requisicao = requests.get('https://g1.com.br', headers=cabecalho)
    texto = requisicao.text
except Exception as erro:
    print('Erro inesperado: ',erro)
