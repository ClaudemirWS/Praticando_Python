print('========== DADOS DE UMA LISTA ==========')
lista = []
conta = valor = 0
roda = 'S'
while roda == 'S':
    #adiciona número a lista
    num = int(input('Digite um número: '))
    lista.append(num)
    #conta números digitados
    conta += 1
    #verifica se tem o nº 5 na lista
    if (num == 5 and num in lista):
        valor += 1
    #continuar ou sair do programa
    roda = str(input('Digitar outro valor? S/N: ')).strip().upper()[0]
    if (roda == 'N' or roda != 'S'):
        print('Saindo...')
        break
lista.sort(reverse=True)
print(f'\nVocê digitou {conta} valores.')
print(f'\nSua lista decrescente {lista}.')
if (valor >= 1):
    print(f'\nO número 5 apareceu {valor} vezes na lista.')
else:
    print('\nO número 5 não apareceu na lista.')