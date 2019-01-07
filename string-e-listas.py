frase = 'Python é o cara!' #dá para acessar cada caracter pelo indice

lista_times = [
'América Mineiro','Atlético Mineiro','Atlético Paranaense','Bahia','Botafogo','Ceará','Chapecoense','Corinthians','Cruzeiro','Flamengo','Fluminense','Grêmio','Internacional','Palmeiras','Paraná','Santos','São Paulo','Sport','Vasco da Gama']

print('Exemplos:')
print(frase)
print('frase[4]= "',frase[4],'"\n\t=> acessa apenas um caracter da frase')
print('frase[0:3]= "',frase[0:3],'"\n\t=> intervalo entre 2 indices')
print('frase[2:10]= "',frase[2:10],'"\n\t=> intervalo entre 2 indices')
print('frase[0:20:1]= "',frase[0:20:1],'"\n\t=> intervalo entre 2 indices, pulando caracter (padrão de 1 em 1)')
print('frase[0:20:2]= "',frase[0:20:2],'"\n\t=> intervalo entre 2 indices, pulando caracter de 2 em 2')
print('frase[-2]= "',frase[-2],'"\n\t=> acessando do fim para o início')
print('frase[-1:-20:-2]= "',frase[-1:-20:-2],'"\n\t=> acessando do fim para o início, pulando indice')
print('frase[  :   :-1]= "',frase[::-1],'"\n\t=> imprimindo ao contrário')
pausa = input('pausa')
#add mais dados na lista na última posição
lista_times.append('Fortaleza')
#removendo dados da lista case sensitive
lista_times.remove('Paraná')
#inserindo dados na posição especifica
lista_times.insert(1, 'CSA')
#alterar dados
lista_times[0] = 'Goiás'

print('\nExemplos de Lista')
print('lista_times[4]= "',lista_times[4],'"\n\t=> acessa um indice da lista')
print('lista_times[0:3]= "',lista_times[0:3],'"\n\t=> intervalo entre 2 indices')
print('lista_times[7:22]= "',lista_times[7:22],'"\n\t=> intervalo entre 2 indices')
print('lista_times[0:22:1]= "',lista_times[0:22:1],'"\n\t=> intervalo entre 2 indices, pulando indice (padrão de 1 em 1)')
print('lista_times[0:22:2]= "',lista_times[0:22:2],'"\n\t=> intervalo entre 2 indices, pulando indice de 2 em 2')
print('lista_times[-1]= "',lista_times[-1],'"\n\t=> acessando do fim para o início')
print('lista_times[-1:-22:-1]= "',lista_times[-1:-22:-1],'"\n\t=> acessando do fim para o início, pulando indice')

pausa = input('\n\npausa')
#contando dados pelo nome
contador = lista_times.count('Palmeiras')
print(contador)
#contando indices
print('Total caracteres na lista =',len(lista_times))
print('Total caracteres na frase =',len(frase))

#teste pop(), o pop() remove da lista[] pelo indece default do último para o primeiro, ex.
nova = [lista_times.pop(0)] # removendo da lista_times do indice 0 e add na nova lista
nova.insert(1,lista_times.pop()) # removendo da lista_times do ultimo e add na nova lista

print(nova)

frase_nova = frase + ' Não tenho dúvidas!' # cancactenando frases
print(frase.lower()) #retorna minuscula
print(frase_nova.upper()) #retorna maiuscula
frase_separada = frase_nova.split(' ') #separa a frase no demarcador e transforma em lista
print(frase_separada)