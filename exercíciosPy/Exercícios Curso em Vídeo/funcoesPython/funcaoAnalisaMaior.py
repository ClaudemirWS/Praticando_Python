print('========== ANALISA NUMEROS MAIORES ==========')
lista = []
ini = 'S'
def recebeNum(lista):
    print(f'Foram digitados {len(lista)} números, sendo: {lista} ')
    for numeros in lista:
        if (numeros == max(lista)):
            print(f'O maior número digitado foi {numeros}')
    lista.clear()
    return
#INICIO DO PROGRAMA
while ini == 'S':
    qtd = int(input('Quantos números deseja digitar? '))
    for indice in range (0, qtd):
        num = int(input(f'{indice+1}º número: '))
        lista += [num]
    recebeNum(lista)
    ini = str(input('\nDeseja rodar o programa de novo? S/N: ')).strip().upper()[0]
    if (ini == 'N'):
        print('\nObrigado por testar meu programa...')
        break
    