print('========== ANALISANDO DADOS ==========')
temNove = 0
tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
#mostra num pares
print(f'Os números pares foram: ', end='')
for count in range (len(tupla)):
    #conta quantos 9 existem na tupla
    if (tupla[count] == 9):
        temNove += 1
    #separa os num pares
    if (tupla[count] % 2 == 0):
        print(tupla[count], end=' - ')
#mostra quantos 9 existem na tupla
print(f'\nA tupla tem {temNove} números 9.')
#mostra posição do num 3
print(f'O primeiro número 3 aparece na posição {tupla.index(3)}.')


