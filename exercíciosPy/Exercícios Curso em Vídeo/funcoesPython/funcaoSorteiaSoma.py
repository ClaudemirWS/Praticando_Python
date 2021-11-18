from random import randint
print('========== SORTEIO E SOMA DE PARES ==========')
def sorteia(lista): 
    sorteados = 0
    for indice in range (0, 5):
        sorteados = randint(0,10)
        lista.append(sorteados)  
        print(f'{sorteados}', end=' ',)
def somaPar(lista):
    soma = 0
    for numeros in lista:
        if (numeros % 2 == 0):
            soma += numeros
    print(soma)
#INICIO DO PROGRAMA
numeros = []
print(f'Sorteados: ', end='')
sorteia(numeros)
print(f'\nA soma dos pares é: ', end='')
somaPar(numeros)

