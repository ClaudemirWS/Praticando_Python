print('========== MAIOR E MENOR ==========')
lista = []
for count in range (0,5):
    lista += [int(input('Digite um valor: '))] 

print(f'\nSua lista de números: {lista}')
print(f'O maior valor foi o {max(lista)} na posição {lista.index(max(lista))+1}') # somei mais um para ficar mais
print(f'O menor valor foi o {min(lista)} na posição {lista.index(min(lista))+1}') # "simples de ler"