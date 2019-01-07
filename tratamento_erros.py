import time

try:
    a = 1200/0
except ZeroDivisionError:
    print('Impossível dividir por zero!')
try:
    aaa()
except NameError:
    print('Erro de sintaxe ou digitação!')
try:
    lista = []
    print(lista[3])
except Exception as err:
    print('Aconteceu um erro:',err)

def abre_arquivo():
    try:
        open('arquivo.txt')
        return True
    except Exception as erro:
        print('Aconteceu um erro: ',erro)
        return False
while not abre_arquivo():
    print('Tentando abrir arquivo!!!!\n',time.sleep(5))
print('Consegui abrir o arquivo!!!')
