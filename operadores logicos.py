#comparações: ==, !=, >, >=, <, <=
#comparações: and e or
from _ast import operator

iguais = 'são iguais'
difer = 'são diferentes'
maior_igual = 'é maior ou igual a'
menor_igual = 'é menor ou igual que'
maior = 'é maior que'
menor = 'é menor que'
print('Menu\nDigite 2 opções para comparações:\n\n')
opcao1 = input('Primeira opção: ')
opcao2 = input('Segunda opção: ')
if opcao1 == opcao2:
    print(opcao1, ' e ', opcao2, iguais)
elif opcao1 != opcao2:
    print(opcao1, ' e ', opcao2,difer)
if opcao1 > opcao2:
    print(opcao1, maior, opcao2)
elif opcao1 < opcao2:
    print(opcao1, menor , opcao2)
else:
    print(' ou', maior_igual, ",\n ou", menor_igual)