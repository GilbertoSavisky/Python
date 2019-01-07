'''
exercicio
Faça um programa que pergunte a idade, altura e peso.
Decida se ela pode ou não entrar pro exército
Precisa ter:
+ de 18 anos
+ / = 60kg
+ / = 1,70 altura
'''
print('Pesquisa para saber se você esta apto para entrar no Exército.')
print('Recomendções:\n *Ter mais de 18 anos\n *Pesar mais de 60kgs\n *E ter 1,70 ou mais de altura:')
print('Vamos lá!\n')
idade = int(input('\tQual a sua idade?: '))
peso = input('\tQual o seu peso?: ')
altura = float(input('\tQual a sua altura?: '))

if (idade < 18):
    print('Você não esta apto para entrar no Exército,\nPorque sua idade é menor que 18 anos.')
elif int(peso) <= 59:
    print('Você não esta apto para entrar no Exército,\nPorque você pesa menos de 60kgs.')
elif altura < 1.7:
    print('Você não esta apto para entrar no Exército,\nPara entrar no Exército é obrigatório ter mais de 1,70 de altura.')
else:
    print('Parabéns você esta apto para entrar no Exército')