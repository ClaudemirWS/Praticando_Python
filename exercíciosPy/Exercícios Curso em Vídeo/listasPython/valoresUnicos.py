print('========== LISTA COM VALORES UNICOS ==========')
lista = []
inicia = 'S'
valor = 0
while True:
    if (inicia == 'S'):
        valor = int(input('Digite um valor: '))
        if valor in lista[0:]:
            print('Já existe, não adicionado.')
        else:
            lista.append(valor)
            print('Adicionando a lista..')
    else: 
        print('Saindo...')
        break
    inicia = str(input('Quer continuar? S/N: ')).strip().upper()
lista.sort()
print(f'Sua lista foi {lista}')