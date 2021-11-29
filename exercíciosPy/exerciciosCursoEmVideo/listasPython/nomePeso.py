print('========== NOME E PESO DE PESSOAS ==========')
lista = []
roda = 'S'
maiorPeso = menorPeso = 0

while roda == 'S': #cadastra pessoas
    nome = str(input('\nDigite o primeiro nome: ')).strip().title()
    peso = float(input('Digite o peso em Kg: '))
    lista.append([nome,peso])
    roda = str(input('Deseja cadastrar nova pessoa S/N: ')).strip().upper()[0]
    if (roda == 'N'):
        print('\nSaindo..')
        break

print(f'Você cadastrou {len(lista)} pessoas.') #quantas pessoas foram cadastradas

for indice, pesos in enumerate (lista):
    if (indice == 0): #se for o primeiro cadastrado, vai direto pro maior peso
        maiorPeso = menorPeso = pesos[1]
    else:
        if (pesos[1] > maiorPeso): #se o proximo for maior, se torna o maior peso
            maiorPeso = pesos[1]
        if (pesos[1] < menorPeso): #se o proximo for menor que o menor, se torna o menor peso
            menorPeso = pesos[1]

print(f'\nO maior peso foi {maiorPeso}Kg e pertence a ', end='')
for indice, nome in enumerate (lista):
    if (nome[1] == maiorPeso):
        print([nome[0]], end=' ')
print(f'\nO menor peso foi {menorPeso}kg e pertence a ', end='')
for indice, nome in enumerate (lista):
    if (nome[1] == menorPeso):
        print([nome[0]], end=' ')