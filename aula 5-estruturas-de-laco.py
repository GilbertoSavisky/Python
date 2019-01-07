
lista_times = [
'América Mineiro','Atlético Mineiro','Atlético Paranaense','Bahia','Botafogo','Ceará','Chapecoense','Corinthians','Cruzeiro','Flamengo','Fluminense','Grêmio','Internacional','Palmeiras','Paraná','Santos','São Paulo','Sport','Vasco da Gama','Vitória']

#for simples
for i in lista_times:
    print(i)
print('--------------------------------------\n')
lista_numeros = range(10) # range retorna uma lista de numeros em ordem crescente iniciando do 0 até o num passado
lista_numeros = range(2,10)#com intervalo de inicio e fim
lista_numeros = range(0,20,2)#com intervalo e qtdade pulada

#range pode ser usado como CONT para o for

for i in range(16):  #cont do 0 ao 16
    print(lista_times[i])

print('---------------------------------\n')
for i in range(4,20):  #cont do 4 ao 20
    print(i,'=',lista_times[i])

print(('---------------------------------\n'))
for i in range(len(lista_times)): #passando o lenght da lista
    print(i,lista_times[i])
'''
print(('---------------------------------\n'))

i = 0;
while i < 10:
    print(i)
    i = i+1;
'''