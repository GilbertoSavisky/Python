from random import random, randint

pessoa_1 = {'nome':'Gilberto Savisky', 'nota': 41, 'desempate': 0}
pessoa_2 = {'nome':'João Arruda', 'nota': 28, 'desempate': 0}
pessoa_3 = {'nome':'Reinaldo Cavalcante', 'nota': 53, 'desempate': 0} # dicionario (dict)
pessoa_4 = {'nome':'Paula Amorim', 'nota': 67, 'desempate': 0}
pessoa_5 = {'nome':'André Nogueira', 'nota': 41, 'desempate': 0}
pessoa_6 = {'nome':'Fernando Donizete', 'nota': 53, 'desempate': 0} # dicionario (dict)

lista_pessoas = [pessoa_1, pessoa_2, pessoa_3,pessoa_4, pessoa_5, pessoa_6] # lista (list)

for i in lista_pessoas:
    desempate = randint(80,100)
    cont = len(lista_pessoas)- len(lista_pessoas)
    i['desempate'] = desempate
    for j in lista_pessoas:
        if (lista_pessoas[cont]['nota']) > (lista_pessoas[cont+1]['nota']):
            print((lista_pessoas[cont]['nota']))
        pausa = input()
        cont += 1



