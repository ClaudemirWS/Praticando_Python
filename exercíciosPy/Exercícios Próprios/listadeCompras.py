#Em andamento....
print('========== Lista de Compras =========')
#INICIO DO PROGRAMA
dcrn = {}
lista = []
listaCompras = []
inicia = 'S'
while (inicia == 'S'):
    dcrn['item'] = str(input('Digite o nome de um item: ')).strip().title()
    dcrn['qtd'] = int(input('Digite a quantidade para comprar: '))
    lista.append(dcrn.copy())
    listaCompras.append(lista[:])
    lista.clear()
    inicia = str(input('Novo item? S/N: ')).strip().upper()[0]
    if (inicia != 'S'):
        print('Saindo...')
        break
print(lista)