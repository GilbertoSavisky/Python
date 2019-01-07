from random import randint
lista = []
i = 0
j = 0
total = 0
cont = 1
print('Calculadora de loteria')
#cont = input('qual a qtdade de num: ')
#cont = int(cont)
while cont != 0:
    while (cont != 5)and cont != 6 and cont != 15:
        cont = input('qual a qtdade de num: ')
        cont = int(cont)
        if cont == 0:
            exit()
        lista = []
    total = input('Qual o total de números: ')
    total = int(total)
    i = 0

    while i < int(cont):
        lista.append(randint(1,total))
        j = 0
        while j < i:
            if lista[j] == lista[i]:
                while lista[j] == lista[i] and i !=0 :
                    lista[i] = (randint(1,total))
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
    print (lista,'\nCont =',cont)
    cont = 1