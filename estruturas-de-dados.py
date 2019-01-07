pessoa_1= {'nome':'Gilberto Savisky', 'idade': 41, 'peso': 75}
pessoa_2 = {'nome':'João Arruda', 'idade': 28, 'peso': 65}
pessoa_3 = {'nome':'Reinaldo Cavalcante', 'idade': 53, 'peso': 87} # dicionario (dict)

lista_pessoas = [pessoa_1, pessoa_2, pessoa_3] # lista (list)

minha_tupla = ('Amadeu', 'Lourenço') # Tupla (tuple)
conjunto = {'pessoa_1', 'pessoa_2', 'pessoa_3'} # conjunto (set)

print(lista_pessoas[0].values())

for i in lista_pessoas:
    print(i['nome'])

#perguntar se um determindao dado esta dentro da coleção
if 'pessoa_1' in conjunto:
    print("pessoa esta")

print(pessoa_3['nome'])