from random import randint
lista = []
i = 0
j = 0
total = 0
cont = 0
print('Calculadora de loteria')
cont = input('qual a qtdade de num: ')
while cont == 0:
    cont = input('qual a qtdade de num: ')
    print('cont',cont)
if cont == 5:
    total = 50
elif cont == 6:
    total = 60
elif cont == 15:
    total = 20

while i < int(cont):
    lista.append(randint(1,60))
    j = 0
    while j < i:
        if lista[j] == lista[i]:
            while lista[j] == lista[i] and i !=0 :
                lista[i] = (randint(1,60))
            j = 0
        else:
            j = j+1
    i = i +1
print(lista)

for j in range(len(lista)):
    for i in range(len(lista)-1):
        
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux
print (lista)