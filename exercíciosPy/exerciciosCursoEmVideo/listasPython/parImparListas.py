listaNum = []
listaImpar = []
listaPar = []
roda = 'S'
while roda == 'S':
    num = int(input('Digite um número: '))
    if (num > 0):
        listaNum.append(num)
        print('Adicionando a lista ...')
        if (num % 2 == 0):
            listaPar.append(num)
        elif (num % 2 == 1):
            listaImpar.append(num)
    else: 
        print('Tente outro número.')
    roda = str(input('Digitar outro número? S/N: ')).strip().upper()[0]
    if (roda == 'N'):
        print('Saindo...')
        break
listaNum.sort()
listaPar.sort()
listaImpar.sort()
print(f"""Você digitou os números: {listaNum}.
Os pares foram: {listaPar}.
Os ímpares foram {listaImpar}.""")

