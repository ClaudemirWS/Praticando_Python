from random import randint
maior = menor = 0
tupla = (randint(1,10,),randint(1,10,),randint(1,10,),randint(1,10,),randint(1,10,))
print('========== MAIOR E MENOR ==========')
print(f'Tupla: {tupla}')
#print(f'O maior valor sorteado foi: {max(tupla)}')
#print(f'O menor valor sorteado foi: {min(tupla)}')
print(f'O maior valor foi: {sorted(tupla)[-1]}')
print(f'O menor valor foi: {sorted(tupla)[0]}')
