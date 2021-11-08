print('========== ESTUDANDO ENUMERATE ==========')
lista = []
limite = int(input('Quantos números deseja digitar? '))

for contador in range (1, limite+1):
    lista.append(int(input(f'Digite o {contador}ª número: ')))

print(f'\nVamos ver sua lista: {lista}\n')

for indice, numero in enumerate(lista):
    print(f'Você digitou o número {numero} na {indice+1}ª posição')