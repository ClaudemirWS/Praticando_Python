print('========== MATRIZ 3 x 3 ==========')
lista = [[[],[],[]],[[],[],[]],[[],[],[]]]
index = 0
while index != 3:
    for count in range (0, 3):
        lista[index][count].append(int(input(f'Digite um valor para [{index}] [{count}]: ')))
    index += 1
print('\n')
print(f'{lista[0]}')
print(f'{lista[1]}')
print(f'{lista[2]}')