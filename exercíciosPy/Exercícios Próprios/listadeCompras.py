#Em andamento....
print('========== Lista de Compras =========')
def mostraLista(listaCompras):
    print()
    print('-' * 33)
    print(f'{"[ COMPRAR ]":>1} {"[ QTD ]":>20}')
    print('-' * 33)
    for cod, items in enumerate (listaCompras):
        for listarProd in items:
            print(f'{listarProd["item"]} {listarProd["qtd"]:>20}')
            

def registraItem(dcrn, item):
    item.append(dcrn.copy())
    listaCompras.append(item[:])
    item.clear()

#INICIO DO PROGRAMA
dcrn = {}
item = []
listaCompras = []
inicia = 'S'
while (inicia == 'S'):
    dcrn['item'] = str(input('Digite o nome de um item: ')).strip().title()
    dcrn['qtd'] = int(input('Digite a quantidade para comprar: '))
    registraItem(dcrn,item)
    inicia = str(input('Novo item? S/N: ')).strip().upper()[0]
    if (inicia != 'S'):
        print('Saindo...')
        break
mostraLista(listaCompras)
