import requests
import json

try:
    req = requests.post('http://www.omdbapi.com/?i=tt3896198&apikey=ebe630f2')
except Exception as err:
    print('Erro: ',err)
dicionario = json.loads(req.text)
print(dicionario)