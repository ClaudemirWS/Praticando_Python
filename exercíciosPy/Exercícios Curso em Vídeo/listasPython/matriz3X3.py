print('========== MATRIZ 3 x 3 ==========')
lista = [[[],[],[]],[[],[],[]],[[],[],[]]]
index = 0
somaPar = somaColuna = maiorLinha = 0
while index != 3:
    for count in range (0, 3):
        lista[index][count].append(int(input(f'Digite um valor para [{index}] [{count}]: ')))
    index += 1
print('\n========== MATRIZ ==========')
print(f'{lista[0]}')
print(f'{lista[1]}')
print(f'{lista[2]}')
print('\n ========== SOMAS E VALORES ==========')
for indice, varreLista in enumerate (lista):
    if (indice == 1): #PROCURA O MAIOR NÚMERO DA SEGUNDA LINHA
        for indice, numeros in enumerate (varreLista):
            for indice, numero in enumerate (numeros):
                maiorLinha = numero
                if (numero > maiorLinha):
                    maiorLinha = numero
    for indice, numeros in enumerate (varreLista): #SOMA OS NÚMEROS PARES DA MATRIZ
        for indice, numero in enumerate (numeros):
            if (numero % 2 == 0):
                somaPar += numero
    for indice, numColuna in enumerate (varreLista[2]): #SOMA OS NÚMEROS DA 3º COLUNA
            somaColuna += numColuna
print(f'A soma dos pares é {somaPar}')
print(f'A soma dos números da terceira coluna é {somaColuna}')
print(f'O maior número da segunda linha é o {maiorLinha}')