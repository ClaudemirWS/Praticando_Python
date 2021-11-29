print('========== MAIOR E MENOR ==========')
lista = []

for count in range (0,5):
    lista.append(int(input('Digite um valor: ')))
    
print(f'\nSua lista de números: {lista}')
print(f'O maior valor foi o {max(lista)} na posição',end=' ')
for indiceNum, varreLista in enumerate(lista): #se o item varrido for igual ao maior, printa
    if (varreLista == max(lista) ):
        print(f'{indiceNum}', end='...')
print(f'\nO menor valor foi o {min(lista)} na posição',end=' ')
for indiceNum, varreLista in enumerate(lista): #se o item varrido for igual ao menor, printa
    if (varreLista == min(lista)):
        print(f'{indiceNum}', end='...')

