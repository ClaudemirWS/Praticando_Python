from random import randint
from operator import itemgetter
print('========== SORTEIO DE DADOS =========')
dcrn = {}
ranking = []
for indice in range (1, 5):
    dcrn[f'jogador {indice}'] = randint(1,6)
for indice, valor in dcrn.items():
    print(f'O {indice} tirou o dado {valor}.')
print(dcrn)
print('========== RANKING DOS JOGADORES ==========')
ranking = sorted(dcrn.items(), key=itemgetter(1), reverse=True)
for indice, varreLista in enumerate(ranking):
    indice += 1
    print(f'{indice}º lugar: {varreLista[0]} com o dado {varreLista[1]}')