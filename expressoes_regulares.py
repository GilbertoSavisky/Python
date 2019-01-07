import re
import requests
string_teste = 'luh_cris.savisky@gmail.com'
req = requests.get('https://www.americanas.com.br/')
padrao = re.search(r'r\D', string_teste) # para procurar qualquer coisa (.), qualquer caracter (\w)
                                         # re.search busca somente a primeira incidencia

padrao = re.findall(r'[rpo]+', string_teste) # re.findall busca todas as incidencias

#para testar expressoes regulares em tempo real http://regex101.com

padrao = re.findall(r'[\w\.*-]+@[\w.-]+', req.text)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')